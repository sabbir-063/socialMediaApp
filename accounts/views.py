# Authentication Views in accounts/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .forms import SignupForm, LoginForm

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            
            # Authenticate the user after saving
            authenticated_user = authenticate(username=user.username, password=form.cleaned_data['password1'])
            
            if authenticated_user:
                login(request, authenticated_user)
                return redirect('home')
    else:
        form = SignupForm()
    
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)  # Pass request explicitly
        if form.is_valid():
            user = form.get_user()  # AuthenticationForm has this method
            login(request, user)
            return redirect('home')
        else:
            print("Form is invalid. Errors:", form.errors)

    else:
        form = LoginForm(request)  # Pass request to the form

    return render(request, 'accounts/login.html', {'form': form})



@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request, username):
    user_profile = get_object_or_404(CustomUser, username=username)
    is_following = request.user.is_following(user_profile)
    return render(request, 'accounts/profile.html', {'user_profile': user_profile, 'is_following': is_following})

@login_required
def follow_user(request, username):
    user_to_follow = get_object_or_404(CustomUser, username=username)
    request.user.follow(user_to_follow)
    return redirect('profile', username=username)

@login_required
def unfollow_user(request, username):
    user_to_unfollow = get_object_or_404(CustomUser, username=username)
    request.user.unfollow(user_to_unfollow)
    return redirect('profile', username=username)