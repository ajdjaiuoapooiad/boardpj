from django.urls import path
from . import views


app_name='board'

urlpatterns = [
    path('signup/',views.signupfunc,name='signup'),
    path('login/',views.loginfunc,name='login'),
    path('logout/',views.logoutfunc,name='logout'),
    path('list/',views.listfunc,name='list'),
    path('detail/<int:pk>',views.detailfunc,name='detail'),
    path('good/<int:pk>',views.goodfunc,name='good'),
    path('read/<int:pk>',views.readfunc,name='read'),
    
]
