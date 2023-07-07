from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.generic import DetailView
# from myapp.models import FirstYearForm 
from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')

def courses(request):
    return render(request, 'myapp/courses.html')

def search(request):
    query = request.GET.get('query')
    # Perform search functionality based on the query parameter
    # Add your search logic here
    context = {
        'query': query
    }
    return render(request, 'myapp/search.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('dashboard')  # Replace 'dashboard' with your actual dashboard URL
    else:
        form = UserCreationForm()
    return render(request, 'myapp/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('dashboard')  # Replace 'dashboard' with your actual dashboard URL
    else:
        form = AuthenticationForm()
    return render(request, 'myapp/login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('login')  # Replace 'login' with your actual login URL

# def first_year(request):
#     if request.method == 'POST':
#         form = FirstYearForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#     else:
#         form = FirstYearForm()
    
#     first_year_data = FirstYearForm.objects.first()
#     context = {
#         'form': form,
#         'first_year_data': first_year_data,
#     }
#     return render(request, 'myapp/first_year.html', context)

