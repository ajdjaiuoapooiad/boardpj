from django.urls import path,include
from .views import signupfunc


app_name='board'

urlpatterns = [
    path('',signupfunc,name='signup'),
]
