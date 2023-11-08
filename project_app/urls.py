from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register, name='register'),
    path('login',views.login_view, name='login'),
    path('dashboard/',views.dashboard),
    path('logout_view',views.logout_view,),
    path('myassignlist/',views.myassignlist),
    path('deletetask/<str:action>/<int:id>/',views.deletetask),
    path('login_page',views.login_page),
    path('register_page',views.register_page),
    path('assigntask',views.assigntask),
    path('assignuser',views.assignuser),
    path('mytask',views.mytask),
    path('userlist',views.userlist)
]