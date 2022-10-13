from django.contrib import admin
from .models import Author, Genre, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    list_filter = ('last_name', )

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'amount', 'price', 'image')
    list_filter = ('author', )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(Book, BookAdmin)
