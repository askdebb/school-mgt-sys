from django.urls import path
from .views import signIn, register, registerSchool

urlpatterns = [
    # path ('', home, name='home'),
    path ('login/', signIn, name='sign-in'),
    path ('register/', register, name='register'),
    path ('register-school/', registerSchool, name='register-school'),
]
