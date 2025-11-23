from django.shortcuts import render,redirect
from django.http import HttpResponse
from store.models import useddata
#def signup(request):
   # return render(request,'signup.html')
# views.py
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, CartItem

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if not request.session.session_key:
        request.session.create()
    session_key = request.session.session_key
    
    cart_item, created = CartItem.objects.get_or_create(
        product=product,
        session_key=session_key,
        defaults={'quantity': 1}
    )
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('cart')

def cart(request):
    if not request.session.session_key:
        request.session.create()
    session_key = request.session.session_key
    
    cart_items = CartItem.objects.filter(session_key=session_key)
    total = sum(item.total_price() for item in cart_items)
    
    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total
    })
# views.py
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('cart')

def update_quantity(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('cart')
def editdata(request,id):
    d=useddata.objects.get(id=id)
    return render(request,'editdata.html',{'x':d})
def edit(request,id):
    d=useddata.objects.get(id=id)
    d.username=request.GET['a1']
    d.Email=request.GET['a2']
    #d.Gender=request.GET['gender']
    d.password=request.GET['a3']
    d.ConfirmPassword=request.GET['a4']
    d.save()
    return redirect('../display')
def edit(request):
    return render(request,'edit.html')
def display(request):
    a=useddata.objects.all()
    return render(request,'display.html',{'x':a})
def cart(request):
    return render (request,'cart.html')
def index(request):
    return render(request,'index.html')
def form(request):
    return render(request,'form.html')
def fashion(request):
    return render(request,'fashion.html')
def electronic(request):
    return render(request,'electronic.html')
def jewellery(request):
    return render(request,'jewellery.html')
def home(request):
    return render(request,'home.html')
def profile(request):
    return render(request,'profile.html')
def reg(request):
    u=useddata()
    u.username=request.GET['a1']
    u.Email=request.GET['a2']
    u.password=request.GET['a3']
    u.ConfirmPassword=request.GET['a4']
    u.save()
    return render(request,'signup.html')
    return render(request,'form.html')
def signup(request):
    return render(request,'signup.html')
def sign(request):
    a= request.GET['b2']
    b= request.GET['b3']
    if useddata.objects.filter(Email=a,password=b):
     return render(request,'index.html')
    else:
        return redirect('../signup')






# Create your views here.
