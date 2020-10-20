from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Item
from blog.forms import Itemform

def index(request):
    
    return render(request,"base.html")

def veg(request):
    item_list= Item.objects.all()
    context={"item_list":item_list}
    return render(request,"blog/select_food.html",context)

def non_veg(request):
    mukul = "sorry we don't take orders, for non veg department call mukul pahuja services"
    context={"mukul":mukul}
    return render(request,"blog/non_veg.html", context)


def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context= {
        "item":item
    }
    return render(request,"blog/food_detail.html",context)



def create(request):
    form = Itemform()
    context ={
        "form":form
    }
    if request.method=="POST":
        form=Itemform(request.POST)
        if form.is_valid():
            form.save()
            return redirect ("home")
    return render(request,"blog/item-form.html",context)



def update(request,id):
    item= Item.objects.get(id=id)
    form = Itemform()
    context={
        "form":form,
        "item":item
    }
    if request.method=="POST":
        form=Itemform(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request,"blog/update.html",context)

