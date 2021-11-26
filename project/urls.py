from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('entity-admin/', admin.site.urls),
]

admin.site.site_header = "Tappware Administration"
admin.site.index_title = "Tappware Administration"
# admin.site.index_title = "Welcome to UMSRA Researcher Portal"
