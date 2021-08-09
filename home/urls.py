
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('package',views.package, name='package'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name= 'signup')
]