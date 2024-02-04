from django.shortcuts import render,redirect
from .models import User
from .forms import MyUserCreationForm,UserForm
# Create your views here.
def index(request):
  users = User.objects.all()
  return render(request,'main/index.html',{
    'users':users
  })

def create(request):
  forms = MyUserCreationForm()

  if request.method == 'POST':
    forms = MyUserCreationForm(request.POST)
    if forms.is_valid():
      forms.save()
      return redirect('/users')

  return render(request,'main/create.html',{
    'forms':forms
  })

def update(request,id):
  user=User.objects.get(id=id)
  form = UserForm(instance=user)

  if request.method == 'POST':
    form = UserForm(request.POST,instance=user)
    if form.is_valid():
      form.save()
      return redirect('/users')
    
  return render(request,'main/update.html',{
    'form':form
  })

def get(request,id):
  user=User.objects.get(id=id)
  return render(request,'main/get.html',{
    'user':user
  })

def delete(request,id):
  user=User.objects.get(id=id)
  user.delete()
  return redirect('/users')