from django.contrib import admin

from .models import Author, Book, Publisher, Store

admin.site.register(Author)
# admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Store)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
