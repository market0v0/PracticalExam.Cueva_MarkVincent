
from django.contrib import admin

# Register your models here.
from .models import Employee, Waiter, Manager, Seating, Table, TipsEarned

admin.site.register(Employee)
admin.site.register(Waiter)
admin.site.register(Manager)
admin.site.register(Seating)
admin.site.register(Table)
admin.site.register(TipsEarned)