from django.shortcuts import render,HttpResponse
from .models import login
# Create your views here.
def lg( request):
    if request.method == "POST":
        username = request.POST.get( 'username')
        password = request.POST.get( 'password')
        
        s =login()
        s.username = username
        s.password = password
        s.save()
    
    return render( request, 'lg.html')
   

def home( request):
    l = login.objects.all()
    data = {
        'l':l
    }

    return render( request, 'home.html',data)