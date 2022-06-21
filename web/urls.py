from django.urls import path
from web.views.auth import login

urlpatterns = [
    path('login/', login, name="login"),
]