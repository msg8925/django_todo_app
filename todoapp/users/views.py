from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
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

