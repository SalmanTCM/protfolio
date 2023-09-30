from django.contrib import admin
from .models import Hero
# Register your models here.

class HeroAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'image')
    # You can customize the fields displayed in the list view

admin.site.register(Hero, HeroAdmin)