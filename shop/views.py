from django.shortcuts import render
from django.http import HttpResponse
from math import ceil
from .models import product,Contact,place_Order,OrderUpdate


# Create your views here.
def index(request):
    allProds = []
    catprods = product.objects.values('catagory', 'id')
    cats = {item['catagory'] for item in catprods}
    for cat in cats:
        prod = product.objects.filter(catagory=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds':allProds }
    return render(request, 'shop/index.html', params)
def SearchMatch(query,item):
    if query in item.prod_name.lower() or query in  item.desc.lower() or query in  item.catagory.lower(): 
        return True
    else:
        return False    

def search(request):
    query= request.GET.get('search')
    allProds = []
    catprods = product.objects.values('catagory', 'id')
    cats = {item['catagory'] for item in catprods}
    for cat in cats:
        prodtemp = product.objects.filter(catagory=cat)
        prod=[item for item in prodtemp if SearchMatch(query,item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) !=0:
        
            allProds.append([prod, range(1, nSlides), nSlides])
    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds':allProds,'msg':""}

    if len(allProds)==0 or len(query)<4:
        params={'msg':"we doent able to find you query please make sure you have Search for right product"}

    return render(request, 'shop/Search.html', params)    
    
    
def About(request):  
    return render(request,'shop/about.html')
def contact(request):
    thanks=False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        cont = Contact(  name=name, email=email, phone=phone, desc=desc)
        cont.save()
        thanks=True
    return render(request, 'shop/contact.html',{'thank':thanks})

def Tracker(request):
    return render(request,'shop/Tracker.html')



def viewproduct(request,myid):
    products=product.objects.filter(id=myid)
    print(product)
    return render(request, "shop/viewproduct.html",{'product':products[0]})
def Checkout(request): 
    if request.method=="POST":
        itemsJson= request.POST.get('itemsJson', '')
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone', '')

        order = place_Order(Items_json= itemsJson, Name=name, Email=email, Address= address, City=city, State=state, Zip_code=zip_code, Phone=phone)
        order.save()
        update= OrderUpdate(order_id= order.order_id, update_desc="The order has been placed")
        update.save()
        thank=True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
    return render(request, 'shop/checkout.html')

    
