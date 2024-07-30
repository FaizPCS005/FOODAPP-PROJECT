from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Items1
from FoodApp.forms import ItemForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    item_list=Items1.objects.all()
    context={
        'item_list':item_list
    }
    return render(request,'FoodApp/home.html',context)
def details(request,item_id):
    item_list=Items1.objects.get(pk=item_id)
    context={
        'item_list':item_list
    }
    return render(request,'FoodApp/details.html',context)
def add_item(request):
    form=ItemForm(request.POST or None)
    if form.is_valid():
            form.save()
            return redirect('FoodApp:home')
    return render(request,'FoodApp/item-form.html',{'form':form})
def update_item(request,id):
    item=Items1.objects.get(pk=id)
    form=ItemForm(request.POST or None,instance=item)
    if form.is_valid():
               form.save()
               return redirect('FoodApp:home')
    return render(request,'FoodApp/item-form.html',{'form':form})
def delete_item(request,id):
      item=Items1.objects.get(pk=id)
      if request.method=='POST':
         item.delete()
         return redirect('FoodApp:home')
      return render(request,'FoodApp/delete_msg.html',{'item':item}) 
   
