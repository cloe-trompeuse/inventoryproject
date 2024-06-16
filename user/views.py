from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .form import CreateUserForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages

# Create your views here
"""
handle user registration
handle POST requests for form submission:
- Validate CreateUserForm
- Save form data upon validation
- Display success message upon successful registration
"""
def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully created for user {username}. Please Login')
            return redirect('user-login')
    else:
        form = CreateUserForm()

    context = {
        'form':form,
    }

    return render(request, 'user/register.html', context)

"""
display user profile info
"""
def profile(request):
    return render(request, 'user/profile.html')

"""
handles POST requests for form submission:
- Validates UserUpdateForm and ProfileUpdateForm
- Updates user and profile data upon successful validation

handles GET requests to display the update forms:
- Initializes UserUpdateForm and ProfileUpdateForm instances with current user data
"""
def profile_update(request):
    if request.method=='POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user-profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form':user_form,
        'profile_form':profile_form,
    }
    return render(request, 'user/profile_update.html', context)