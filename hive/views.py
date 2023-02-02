from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.db.models import Count
from django.views import View
from . models import *
from . forms import CreateUserForm, ProfileForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    products = Product.objects.all()
    context ={'products':products}
    return render (request, 'hive/home.html',context )

def signup(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'hive/register.html', context)

	

def signin(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
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
	return render(request=request, template_name="hive/login.html", context={"login_form":form})
class Profile(View):
	def get(self , request):
		form = ProfileForm
		return render(request, 'hive/profileform.html', locals())
		
            
	def post(self, request):
		form = ProfileForm(request.POST)
		if form.is_valid():
			user =request.user
			name =form.cleaned_data['name']
			address =form.cleaned_data['address']
			city =form.cleaned_data['city']
			state =form.cleaned_data['state']
			mobile =form.cleaned_data['mobile']
			reg = Customer(user=user,name=name,address=address,city=city,state=state,mobile=mobile)
			reg.save()
			messages.success(request,"Successfully updated profile.")
			return redirect('account')
		else:
			messages.warning(request,"Not Successfully updated profile.")
		return render(request, 'hive/profileform.html', locals())
class Account(View):
    def get(self, request):
            acc = Customer.objects.filter(user=request.user)
            
            return render(request, 'hive/profile.html', locals())
class Category(View):
    def get(self, request, val):
        product = Product.objects.filter(category__contains=val)
        title = Product.objects.filter(category__contains=val).values('name')
        return render (request, 'hive/category.html', locals())
class Filter(View):
    def get(self, request, val):
        product = Product.objects.filter(name__contains=val) | Product.objects.filter(description__contains=val)
        title = Product.objects.filter(category__contains=val).values('name')
        return render (request, 'hive/filter.html', locals())
class Productdetail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render (request, 'hive/productdetail.html', locals())

