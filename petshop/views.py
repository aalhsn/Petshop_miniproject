from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .models import PetModel
from .forms import PetForm, SigninForm, SignupForm, PetCreateForm

def pet_list(request):
	pets = PetModel.objects.filter(available=True)
	context = {
		"pets": pets,
	}
	return render(request, 'pet_list.html', context)


def pet_detail(request,pet_id):
	pet = PetModel.objects.get(id=pet_id)
	context = {
		"pet": pet,
	}
	return render(request, 'pet_detail.html', context)


def pet_create(request):

	if request.user.is_anonymous:
			messages.warning(request, "You need to sign in first")
			return redirect('signin')
	form = PetCreateForm()
	if request.method == "POST":
		form = PetCreateForm(request.POST, request.FILES or None)
		if form.is_valid():
			pet = form.save(commit=False)
			pet.owner = request.user
			pet.save()
			messages.success(request, "Successfully Created!")
			return redirect('pet-list')
	context = {
	"form": form,
	}
	return render(request, 'pet_create.html', context)


def pet_update(request, pet_id):

	pet = PetModel.objects.get(id=pet_id)
	form = PetForm(instance=pet)

	if request.method == "POST":
		form = PetForm(request.POST, request.FILES, instance=pet)
		if form.is_valid():
			form.save()
			messages.success(request, 'pet details updated.')
			return redirect("pet-detail", pet_id)
	context = {
		"pet":pet,
		"form":form
	}
	return render(request, 'pet_update.html', context)


def pet_delete(request, pet_id):
	PetModel.objects.get(id=pet_id).delete()
	messages.warning(request, 'pet was deleted.')
	return redirect("pet-list")


def signup(request):
	form = SignupForm()
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)

			user.set_password(user.password)
			user.save()

			login(request, user)
			return redirect("pet-list")
	context = {
		"form":form,
	}
	return render(request, 'signup.html', context)


def signin(request):
	form = SigninForm()
	if request.method == 'POST':
		form = SigninForm(request.POST)
		if form.is_valid():

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			auth_user = authenticate(username=username, password=password)
			if auth_user is not None:
				login(request, auth_user)
				return redirect('pet-list')
	context = {
		"form":form
	}
	return render(request, 'signin.html', context)

def signout(request):
	logout(request)
	return redirect("signin")
