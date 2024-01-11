from django.shortcuts import render
from django.contrib.auth.models import User, auth
# Create your views here.

def dashboardFunction(request):
    # user = auth.authenticate(username=username,password=password)
    return render(request,'dashboard.html')
