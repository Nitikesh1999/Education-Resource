from django.urls import path
from . import views
# from myapp.views import first_year

app_name = 'myapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('search/', views.search, name='search'),
    path('signup/', views.signup, name='signup'),  # Add this line
    path('login/', views.login, name='login'),  # Add this line
    path('logout/', views.logout, name='logout'),
    # path('firstyear/', first_year, name='first_year'),
    
]
