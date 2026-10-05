from django.shortcuts import render,redirect
from .models import RegisterForm
from django.contrib import messages
from .forms import MyRegisterForm

# Create your views here.
def home(request):
    data = RegisterForm.objects.all()
    if(data != ''):
        return render(request,"home.html",{'data':data})
    else:
     return render(request,"home.html")
    
def insert(request):
   if(request.method == "POST"):
      form = MyRegisterForm(request.POST)
      if(form.is_valid()):
        try:
            form.save()
            messages.success(request,"Registration Successfully Completed")
            return redirect("Home")
        except:
           pass
   else:
     form = MyRegisterForm
     return render(request,"register.html",{'form':form})
        
   