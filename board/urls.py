from django.urls import path
from . import views


app_name='board'

urlpatterns = [
    path('',views.signupfunc,name='signup'),
    path('login/',views.loginfunc,name='login'),
    
]
