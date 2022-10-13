from django.shortcuts import render, redirect
from .forms import ProfileForm, UserForm, UserRegistrationForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from cart.cart import Cart 
from bookshop.views import args_dictionary_book


def registration(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit = False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user = new_user)
            return render(request, 'registration_done.html', {'new_user' : new_user})
        return render(request, 'registration.html', {'user_form' : user_form})
    user_form = UserRegistrationForm()
    return render(request, 'registration.html', {'user_form' : user_form})

@login_required
def profile_edit(request):
    if request.method == "POST":
        user_form = UserForm(instance = request.user, data = request.POST)
        profile_form = ProfileForm(request.POST, request.FILES, instance = request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    cart = Cart(request)
    user_form = UserForm(instance = request.user)
    profile_form = ProfileForm(instance = request.user.profile) 
    return render(request, 'profile_edit.html', {'user_form' : user_form, 'profile_form' : profile_form, 
                                                 'cart' : cart} | args_dictionary_book(request))

@login_required
def profile(request):
    cart = Cart(request)
    user_form = UserForm(instance = request.user)
    profile_form = ProfileForm(instance = request.user.profile) 
    return render(request, 'profile.html', {'user_form' : user_form, 'profile_form' : profile_form, 
                                            'cart' : cart} | args_dictionary_book(request))
