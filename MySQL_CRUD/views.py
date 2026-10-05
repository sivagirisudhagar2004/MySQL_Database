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

def update(request,id):
   data = RegisterForm.objects.get(id = id)
   if(request.method == 'POST'):
      name = request.POST['name']
      age = request.POST['age']
      address = request.POST['address']
      contant = request.POST['contant']
      email = request.POST['email']

      data.name = name
      data.age = age 
      data.address = address
      data.contant = contant
      data.email = email
      data.save()
      messages.success(request,"Update Successfully Completed")
      return redirect("Home")
   
def delete(request,id):
   data = RegisterForm.objects.get(id = id)
   data.delete()
   messages.error(request,"Delete Successfully Completed")
   return redirect("Home")
   
        
   