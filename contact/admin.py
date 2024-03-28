from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'created_date')
    search_fields = ('first_name', 'last_name', 'email', 'created_date')
    ordering = ('last_name', 'first_name')
    list_per_page = 15
