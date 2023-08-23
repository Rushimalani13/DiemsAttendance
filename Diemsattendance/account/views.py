from django.shortcuts import render

# Create your views here.
def home_login(request):
    return render(request, 'account/login.html')

