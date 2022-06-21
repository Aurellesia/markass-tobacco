from django.shortcuts import render

from web.forms import LoginForm


def login(request):
    form = LoginForm()
    context = {
        'title': 'Login',
        'header_title': 'FDR Tire',
        'form': form,
    }
    return render(request, "web/login.html", context)