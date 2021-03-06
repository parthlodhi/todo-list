from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
# Create your views here.
def index(request):
    if request.method == 'POST':
        form=ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, ('Item has been added to the list'))
            return render(request, 'index.html',{'all_items':all_items})
        else:
            messages.success(request, ('Please write something to be added in to the list'))
            return redirect('index')    
    else:
        all_items=List.objects.all
        return render(request, 'index.html', {'all_items':all_items})

def delete(request, list_id):
    item= List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item has been deleted'))
    return redirect('index')

def cross_off(request, list_id):
    item=List.objects.get(pk=list_id)
    item.completed= True
    item.save()
    return redirect('index')

def uncross(request, list_id):
    item=List.objects.get(pk=list_id)
    item.completed=False
    item.save()
    return redirect('index')
