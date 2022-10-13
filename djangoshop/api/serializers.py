from rest_framework import serializers
from bookshop.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'description', 'amount', 'price', 'image']
