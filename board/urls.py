from django.urls import path
from . import views


app_name='board'

urlpatterns = [
    path('signup/',views.signupfunc,name='signup'),
    path('login/',views.loginfunc,name='login'),
    path('list/',views.listfunc,name='list'),
    
]
