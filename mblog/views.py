from django.shortcuts import render ,redirect
from .models import List
from .forms import Listform
from django.contrib import messages


# Create your views here.


def home(request):
      if request.method == 'POST':
            form = Listform(request.POST)
            if form.is_valid():
                  form.save()
                  contex = List.objects.all()
                  messages.success(request , ('Item has been added to the list'))
                  return  render(request, 'mblog/home.html', {'contex': contex})
      
                 
      else:
            contex = List.objects.all()
            return render (request ,'mblog/home.html' , {'contex':contex})




def about(request):
      return render (request ,'mblog/about.html' , {})

def delete(request , list_id):
    item = List.objects.get(pk = list_id)
    item.delete()
    messages.success(request, ('Item has been deleted from the list'))
    return redirect('home')


def edit(request, list_id):
    if request.method == 'POST':
          item = List.objects.get(pk=list_id)
          form = Listform(request.POST , instance=item )
          if form.is_valid():
                  form.save()
                  contex = List.objects.all()
                  messages.success(request, ('Item has been edited'))
                  return redirect( 'home')


    else:
        item = List.objects.get(pk=list_id)
        return render (request ,'mblog/edit.html' , {'item':item})