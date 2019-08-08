from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from django.contrib.auth import login,authenticate
def accounts_home_view(request):
    if(request.user.is_authenticated):
        return HttpResponseRedirect("http://127.0.0.1:8000/admin")
    if(request.method=='POST'):
        if(request.POST):
            username=request.POST['username']
            pwd=request.POST['pwd']
            user=authenticate(request,username=username,password=pwd)

            if user:
                login(request,user)
                return HttpResponseRedirect("http://127.0.0.1:8000/admin")

    return render(request,'accounts/login.html')
