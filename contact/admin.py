from django.contrib import admin
from .models import Contact, Category

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone', 'show',)
    search_fields = ('first_name', 'last_name', 'email',)
    ordering = ('last_name', 'first_name',)
    list_per_page = 15
    list_editable = ('first_name', 'last_name', 'show',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)