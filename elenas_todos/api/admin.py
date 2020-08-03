from django.contrib import admin
from .models import Todo


class PropertyAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'description', 'done']
    search_fields = ['description']
    list_filter = ['user']


admin.site.register(Todo, PropertyAdmin)
