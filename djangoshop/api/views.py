from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import generics
from .serializers import BookSerializer
from bookshop.models import Book


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()  
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        self.objects = self.get_queryset()
        return Response({'books' : self.objects}, template_name = 'books.html')