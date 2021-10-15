from django.contrib import admin
from django.urls import path
from second import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('',views.home, name='home' ),
    #path('signup', views.signup, name='signup'),
    #path('signin', LoginView.as_view(template_name='signin.html'),name='signin'),
    #path('signout', LogoutView.as_view(template_name='signout.html'),name='signout'),

    path('setsession', views.setSession, name='setsession'),    
    path('getsession', views.getSession, name='getsession'),
    path('delsession', views.deleteSession, name='deletesession'),
    path('flushSession', views.flushSession, name='flushSession')
]
