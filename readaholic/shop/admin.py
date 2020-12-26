from django.contrib import admin
from .models import *
from django.utils.datetime_safe import datetime

class EntryAdmin(admin.ModelAdmin):
    # Overide of the save model
    def save_model(self, request, obj, form, change):
        obj.cart.total += obj.quantity * obj.book.price
        obj.cart.count += obj.quantity
        obj.cart.updated = datetime.now()
        obj.cart.save()
        super().save_model(request, obj, form, change)

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Cart)
#admin.site.register(Entry, EntryAdmin)
admin.site.register(Count)
