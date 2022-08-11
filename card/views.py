from django.shortcuts import render,HttpResponse,redirect
from .models import login
# Create your views here.
def lg( request):
    
    
    return render( request, 'lg.html')
   
def about( request):
    return redirect(home)
def home( request):
   

    return render( request, 'home.html')


def logout(request):
    if request.method == "POST":
        username = request.POST.get( 'username')
        password = request.POST.get( 'password')
        
        s =login()
        s.username = username
        s.password = password
        s.save()
    
    l = login.objects.all()
    data = {
        'l':l
    }
    return render( request, 'logout.html',data)