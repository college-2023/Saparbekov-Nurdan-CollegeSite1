from django.contrib import admin
from .models import *


class ItemAdmin(admin.ModelAdmin):
    search_fields = 'title description'.split()
    list_display_links = ['title']
    list_display = 'title price category type company material'.split()
    list_editable = 'price'.split()
    ordering = ['price']
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 10
    list_filter = 'category type company material'.split()


class CommonAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Item, ItemAdmin)
admin.site.register(Images)
admin.site.register(Company, CommonAdmin)
admin.site.register(Category, CommonAdmin)
admin.site.register(Material, CommonAdmin)
admin.site.register(Type, CommonAdmin)
admin.site.register(Color, CommonAdmin)
