from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, ProfileUpdateForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Profile successfully created.')
            return redirect('todo-home')


    else:
        form = UserRegistrationForm()
        
        # context = {
        #     "form": form
        # }

    return render(request, 'users/register.html', {"form": form})


@login_required
def profile(request):

    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        u_form = UserUpdateForm(request.POST, instance=request.user)
          
        if p_form.is_valid and u_form.is_valid:
            p_form.save()
            u_form.save()  

            messages.success(request, "Profile successfully updated.")

            return redirect("profile")

    else:

        p_form = ProfileUpdateForm(instance=request.user.profile)
        u_form = UserUpdateForm(instance=request.user)

        context = {
            "p_form": p_form,
            "u_form": u_form
        }

    return render(request, "users/profile.html", context)