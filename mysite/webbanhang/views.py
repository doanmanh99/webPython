from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Category
from django.db.models import F, Count
from django.template.loader import render_to_string


def index(request):
    menu = Category.objects.all();
    return render(request, 'pages/index.html', {'menu': menu})


def sanpham(request):
    list_product = Product.objects.all()
    sale = list_product.filter(promo_price__gt=0)
    menu = Category.objects.all()
    dem = list_product.count()

    return render(request, 'pages/shop-grid.html', {
        'listpro': list_product,
        'sale': sale,
        'menu': menu,
        'dem': dem
    })


def detail(request, id):
    detail = Product.objects.get(id=id)
    return render(request, 'pages/shop-details.html', {'detail': detail})


def danhmucsp(request, id):
    pro = Product.objects.filter(category=id)
    dem = pro.count()
    menu = Category.objects.all()
    return render(request, 'pages/cate_pro.html', {
        'pro': pro,
        'menu': menu,
        'dem': dem
    })


def contact(request):
    return render(request, 'pages/contact.html')
    
cart = {}
def addCart(request):
    if request.is_ajax():
        id = request.POST.get('id')
        unit = request.POST.get('unit')


        proDetail = Product.objects.get(id = id)
        if id in cart.keys():
            itemCart = {
                'name': proDetail.title,
                'price': proDetail.price,
                'image': str(proDetail.product_img),
                'unit': int(cart[id]['unit'])+int(unit),
            }
        else:
            itemCart = {
                'name': proDetail.title,
                'price': proDetail.price,
                'image': str(proDetail.product_img),
                'unit': unit,
            }

        cart[id] = itemCart
        request.session['cart'] = cart
        cartInfo = request.session['cart']

        total = 0;
        count = 0
        for key, value in cartInfo.items():
            total += int(value['price']) * int(value['unit'])
            count +=1
        request.session['total'] = total
        request.session['count'] = count

    return render(request, 'pages/addcart.html', {'cart': cartInfo, 'total': total})
  

def viewcart(request):
    total =0
    carts = request.session.get('cart')
    if carts is None:
        return render(request, 'pages/shoping-cart.html',{'total':total})
    for key,value in carts.items():
        total += int(value['price']*int(value['unit']))
        
    return render(request, 'pages/shoping-cart.html',{'total':total})
