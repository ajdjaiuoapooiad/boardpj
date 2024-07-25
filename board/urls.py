from django.urls import path
from . import views


app_name='board'

urlpatterns = [
    path('signup/',views.signupfunc,name='signup'),
    path('login/',views.loginfunc,name='login'),
    path('logout/',views.logoutfunc,name='logout'),
    path('list/',views.listfunc,name='list'),
    
]
