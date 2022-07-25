from multiprocessing import AuthenticationError
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationError(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")

    
class HomeListView(ListView):
    template_name = 'home.html'

    def get(self, request):
        cats = Category.objects.all()
        return render(request, self.template_name, {'cats':cats})


class CategoryListView(ListView):
    template_name = 'home_detail.html'

    def get(self, request, id):
        categorys = Category.objects.filter(pk=id)
        return render(request, self.template_name, {'id':id, 'categorys':categorys})

class CategoryDetailView(DetailView):
    template_name = 'home_detail_detail.html'

    def get(self, request, id):
        car = Car.objects.get(pk=id)
        return render(request, self.template_name, {'car':car})




