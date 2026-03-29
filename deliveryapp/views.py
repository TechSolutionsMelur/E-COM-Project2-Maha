from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .form import food_form,register_form
from .models import food_details,register_models


# Create your views here.
def viewfood(request):
    data = food_details.objects.all()
    return render(request,'foodapp/foodadd.html',{'data':data})

def home(request):
    return render(request,'foodapp/base.html')

def form(request):
    form = food_form()

    if request.method == 'POST':
        form = food_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print("successfully filled")
            return redirect('viewfood')
        else:
            print("error")
    return render(request,'foodapp/form.html',{ 'form':form })

def delete(request,id):
    dele = get_object_or_404(food_details,id=id)
    if request.method == "GET":
        dele.delete()
        return redirect('viewfood')
    return render(request,'foodapp/foodadd.html')

def register(request):
    register = register_form()

    if request.method == 'POST':
        register = register_form(request.POST)

        if register.is_valid():
            register.save()
            print('successfully register')
            redirect('viewhotal')
        else:
            print('error')
    return render(request,'foodapp/registerform.html',{'register':register})

def viewhotal(request):
    view = register_models.objects.all()
    return render(request,'foodapp/hotalview.html',{ 'view':view })


