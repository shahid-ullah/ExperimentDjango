from django.contrib import admin
from django.db import models
from django.urls import path
from events.admin import event_admin_site

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('entity-admin/', admin.site.urls),
    path("event-admin/", event_admin_site.urls),
]

admin.site.site_header = "Tappware Administration"
admin.site.index_title = "Tappware Administration"
# admin.site.index_title = "Welcome to UMSRA Researcher Portal"
