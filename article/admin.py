from django.contrib import admin

from .models import M2M, Designation, Group, M2Mthrough, Membership, Person

admin.site.register(Person)
admin.site.register(Group)
admin.site.register(Membership)
admin.site.register(M2M)
admin.site.register(Designation)
admin.site.register(M2Mthrough)
