from plantree.models import Category
from django.contrib import admin

class CategoryAdmin(admin.ModelAdmin):
    fields = ['task', 'finished', 'finished_time']

admin.site.register(Category, CategoryAdmin)
