from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app2/index.html')

def moviesingle(request):
    return render(request, 'app2/moviesingle.html')