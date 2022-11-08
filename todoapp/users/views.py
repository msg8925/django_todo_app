from django.shortcuts import render
from .forms import UserRegistrationForm

# Create your views here.
def register(request):

    form = UserRegistrationForm()

    context = {
        "form": form
    }

    return render(request, 'users/register.html', context)

