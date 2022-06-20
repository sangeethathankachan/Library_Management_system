from django.contrib import admin
from libraryApp.models import category,books,selectedbook,customer

# Register your models here.
admin.site.register(category)
admin.site.register(books)
admin.site.register(selectedbook)
admin.site.register(customer)
#admin.site.register(cart)