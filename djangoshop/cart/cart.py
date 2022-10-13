from django.conf import settings
from bookshop.models import Book
from decimal import Decimal

class Cart:
    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.get(settings.CART_SESSION_ID, {})
    
    def add(self, book, quantity = 1):
        book_id = str(book.id)
        if book_id not in self.cart:
            self.cart[book_id] = {'quantity' : 0, 'price' : str(book.price)}
        self.cart[book_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, book):
        book_id = str(book.id)
        if book_id in self.cart:
            del self.cart[book_id]
            self.save()
    
    def update(self, book, quantity = 1, update_quantity = False):
        book_id = str(book.id)
        if book_id not in self.cart:
            self.cart[book_id] = {'quantity' : 0, 'price' : str(book.price)}
        if update_quantity:
            self.cart[book_id]['quantity'] = quantity
        else:
            self.cart[book_id]['quantity'] = 0 + quantity
        self.save()

    def __iter__(self):
        book_ids = self.cart.keys()
        books = Book.objects.filter(id__in = book_ids)

        for book in books:
            self.cart[str(book.id)]['book'] = book
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def get_total_price(self):
        price_list = [item['total_price'] for item in self.cart.values()]
        return sum(price_list)

    def get_total_quantity(self):
        total_quantity = [item['quantity'] for item in self.cart.values()]
        return sum(total_quantity)
    
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
    