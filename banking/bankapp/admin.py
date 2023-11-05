from django.contrib import admin
from . models import Transaction
from . models import Register
# Register your models here.
admin.site.register(Transaction)
admin.site.register(Register)