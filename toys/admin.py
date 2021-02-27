from django.contrib import admin

from toys.models import Address, Tag, Toy, User, Company, Employee

admin.site.register(User)
admin.site.register(Toy)
admin.site.register(Tag)
admin.site.register(Address)
admin.site.register(Company)
admin.site.register(Employee)
