from django.shortcuts import render
from .models import Book, Author
from cart.cart import Cart 

def args_dictionary_book(req):
    cart = Cart(req)
    visits = req.session.get('visits', 0)
    books = Book.objects.all()
    books_amount = Book.objects.count()
    author_amount = Author.objects.count()
    return {'visits' : visits, 
            'books' : books, 
            'books_amount' : books_amount, 
            'author_amount' : author_amount, 
            'cart' : cart}

def index(request):
    request.session['visits'] = request.session.get('visits', 0) + 1
    return render(request, 'index.html', args_dictionary_book(request))

def book(request, id):
    book = Book.objects.get(id = id)
    return render(request, 'view.html', {'book' : book} | args_dictionary_book(request))


