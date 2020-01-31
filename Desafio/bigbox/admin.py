################################################################################
from django.contrib import admin
from .models import (
    Activity,
    Box,
    Category,
    Reason
)
################################################################################

# Register your models here.
################################################################################
class ActivityAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Actividad', {'fields': ['name']}),
        ('Nombre interno', {'fields': ['internal_name']}),
        ('Descripcion', {'fields': ['description']}),
        ('Categoria', {'fields': ['category']}),
        ('Razones', {'fields': ['reasons']}),
        ('Estado', {'fields': ['purchase_available']}),
    ]
################################################################################

################################################################################
class BoxAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Box', {'fields': ['name']}),
        ('Precio', {'fields': ['price']}),
        ('Nombre interno', {'fields': ['internal_name']}),
        ('Descripcion', {'fields': ['description']}),
        ('Categoria', {'fields': ['category']}),
        ('Actividades', {'fields': ['activities']}),
        ('Estado', {'fields': ['purchase_available']}),
    ]
################################################################################

################################################################################
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name','order','description')
################################################################################

################################################################################
class ReasonAdmin(admin.ModelAdmin):
    fields = ('name', 'order')
################################################################################

################################################################################
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Box, BoxAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Reason, ReasonAdmin)
################################################################################
