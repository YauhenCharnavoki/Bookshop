from django.shortcuts import render, redirect, get_object_or_404
from bookshop.models import Book
from .cart import Cart 
from .forms import PurchaseForm
from bookshop.views import args_dictionary_book
from django.views.decorators.http import require_POST
from .forms import UpdateForm



def add(request, id):
    cart = Cart(request)
    book = get_object_or_404(Book, id = id)
    cart.add(book)
    return redirect('catalog') 

def remove(request, id):
    cart = Cart(request)
    book = get_object_or_404(Book, id = id)
    cart.remove(book)
    return redirect('cart')

@require_POST
def update(request, id):
    cart = Cart(request)
    book = get_object_or_404(Book, id = id)
    form = UpdateForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.update(book = book, quantity = cd['quantity'], update_quantity = cd['update'])
    return redirect('cart')

def clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart')

def cart(request):
    return render(request, 'cart.html', args_dictionary_book(request))

def buy(request):
    if request.method == "POST":
        purchase_form = PurchaseForm(request.POST)
        if purchase_form.is_valid():
            purchase_form.save()
            return render(request, 'buy_done.html')
    purchase_form = PurchaseForm() 
    return render(request, 'buy.html', {'purchase_form' : purchase_form} | args_dictionary_book(request))