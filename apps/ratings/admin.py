from django.contrib import admin
from .models import Rating

# Register your models here.

class RatingAdmin(admin.ModelAdmin):
    list_display = ["rater", "agent", "rating"]
    list_filter = ["rater", "agent", "rating"]
    search_fields = ["rater", "agent", "rating"]
    list_per_page = 10
    ordering = ["-created_at"]
    
    
admin.site.register(Rating, RatingAdmin)