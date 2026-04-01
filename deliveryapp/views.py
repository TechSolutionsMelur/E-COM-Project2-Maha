from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .form import food_form,restaurant_form
from .models import food_details,restaurant_register


# Create your views here.

#Food menus
def view_menu(request,restaurant_id):
    data = get_object_or_404(restaurant_register,id=restaurant_id)
    foods = food_details.objects.filter(restaurant=data)
    return render(request,'foodapp/foodadd.html',{
        'data':data,
        'foods':foods 
     })

#Home Page
def home(request):
    return render(request,'foodapp/base.html')

#Add Food 
def addfood(request,restaurant_id):
    form = food_form()
    data = get_object_or_404(restaurant_register,id=restaurant_id)

    if request.method == 'POST':
        form = food_form(request.POST or None ,request.FILES or None)
        if form.is_valid():
            food = form.save(commit=False)
            food.restaurant  = data
            food.save()
            print("successfully filled")
            return redirect('viewmenu',restaurant_id=data.id)
        else:
            print("error")
    return render(request,'foodapp/form.html',{ 
        'form':form,
         'data':data 
        })

#Food Delete
def delete(request,id):
    dele = get_object_or_404(food_details,id=id)
    if request.method == "GET":
        dele.delete()
        return redirect('viewmenu')
    return render(request,'foodapp/foodadd.html')

#food update
def update(request,id):
    edit = get_object_or_404(food_details,id=id)
    form = food_form(request.POST or None,instance=edit)
    if form.is_valid():
        form.save()
        print("successfully update")
        return redirect('viewmenu')
    
    return render(request,'foodapp/edit.html',{ 'form':form })

# Addrestaurant
def addrestaurant(request):
    register = restaurant_form()
    if request.method == 'POST':
        register = restaurant_form(request.POST or None,request.FILES or None)
        if register.is_valid():
            register.save()
            print('successfully register')
            return redirect('restaurant_list')
        else:
            print('error')
    return render(request,'foodapp/registerform.html',{'register':register})

#View Restaurant
def restaurant_list(request):
    view = restaurant_register.objects.all()
    return render(request,'foodapp/restaurant.html',{ 'view':view })


