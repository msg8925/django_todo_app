from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, ProfileUpdateForm, UserUpdateForm
from django.contrib import messages

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


def profile(request):

    p_form = ProfileUpdateForm(instance=request.user.profile)
    u_form = UserUpdateForm(instance=request.user)

    context = {
        "p_form": p_form,
        "u_form": u_form
    }

    return render(request, "users/profile.html", context)