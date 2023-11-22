from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['pkid','id','user','city','country']
    list_display_links = ['id','pkid','user']
    list_filter = ['user','city','country']
    search_fields = ['user','city','country']
    list_per_page = 25
    
    
    
admin.site.register(Profile, ProfileAdmin)