from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Entry, Cart, Count 
from django.contrib.auth.models import User
# Create your views here.
from django.db.models import F


def home(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request,'shop/shop-home.html',context)

def detail(request, book_id):
    mycart = Cart.objects.get(user=User.objects.get(username = request.user.username))
    # Get entries in the cart
    # my_carts_current_entries = Entry.objects.filter(cart=my_cart)
    # Get a list of your products
    book = Book.objects.get(pk=book_id)
    context = {
        'book': book
    }
    # name = Book.objects.get(pk=book_id)

    if request.POST:
        if request.user.is_authenticated:
            my_cart = Cart.objects.get(user=User.objects.get(username = request.user.username))
            
            #if mycart.books.get(pk = book.id):
            counter, created = Count.objects.get_or_create(cart=mycart,book=book)
            counter.count = F('count') +1
            counter.save()
                #Count.objects.filter(cart=mycart,book=book).update(count=F('count')+1)
            #else:
               # print('something')
        #return HttpResponse(something)
        #Entry.objects.create(cart=my_cart, book=Book.objects.get(pk=book_id), quantity=1)
        else:
            print('somethinf')

    return render(request, 'shop/product.html',context)
    #  return HttpResponse("You're looking at book %s."% name)