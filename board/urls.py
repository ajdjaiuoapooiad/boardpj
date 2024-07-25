from django.urls import path
from .views import signupfunc,loginfunc


app_name='board'

urlpatterns = [
    path('',signupfunc,name='signup'),
    path('login/',loginfunc,name='login'),
]
