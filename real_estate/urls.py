from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path("secretsite/", admin.site.urls),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


admin.site.site_header = "Real Estate Admin"
admin.site.site_title = "Real Estate Admin Portal"
admin.site.index_title = "Welcome to Real Estate Portal"