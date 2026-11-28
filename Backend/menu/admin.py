from django.contrib import admin
from .models import Categoria, Producto, Promocion, Info_Local


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "orden")
    list_editable = ("orden",)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "precio", "disponible", "destacado")
    list_filter = ("categoria", "disponible")
    list_editable = ("precio", "disponible", "destacado")
    search_fields = ("nombre",)


@admin.register(Promocion)
class PromocionAdmin(admin.ModelAdmin):
    list_display = ("titulo", "fecha_inicio", "fecha_fin", "PromoActiva")
    list_editable = ("PromoActiva",)


@admin.register(Info_Local)
class InfoLocalAdmin(admin.ModelAdmin):
    list_display = ("Direccion", "Telefono")

    def has_add_permission(self, request):
        return not Info_Local.objects.exists()


admin.site.site_header = "Mamá Julia Café"
admin.site.site_title = "Panel de Mamá Julia"
admin.site.index_title = "Administrar el menú"