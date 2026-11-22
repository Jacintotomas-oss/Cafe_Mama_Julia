from django.shortcuts import render
from datetime import date
from django.db.models import Prefetch
from rest_framework import generics, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Categoria, Producto, Promocion, Info_Local

# Create your views here.

#clases de vistas con Serializer para los modelos 

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ["id", "nombre", "descripcion", "precio", "foto", "destacado"]

class InfoLocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info_Local
        fields = ["Direccion","Telefono","horario","instagram","mapa_url"]

class CategoriaSerializer(serializers.ModelSerializer):
    productos = ProductosSerializer(many=True, read_only=True)

    class Meta:
        model = Categoria
        fields = ["id","nombre","orden","productos"]

class PromocionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promocion
        fields = ["id","titulo","descripcion","image","fecha_inicio","fecha_fin","PromoActiva"]

#clases views 

class MenuView(generics.ListAPIView):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.prefetch_related(
        Prefetch("productos", queryset=Producto.objects.filter(disponible=True))
    )

class PromocionActivaView(APIView):
    def get(self, request):
        hoy = date.today()
        promo = Promocion.objects.filter(
            PromoActiva=True, fecha_inicio__lte=hoy, fecha_fin__gte=hoy
        ).first()
        if promo is None:
            return Response({"message": "No hay promociones activas en este momento."}, status=404)
        return Response(PromocionSerializer(promo, context={"request": request}).data)


class InfoLocalView(APIView):
    def get(self, request):
        info = Info_Local.objects.first()
        if info is None:
            return Response({"message": "Aún no hay información del local."}, status=404)
        return Response(InfoLocalSerializer(info, context={"request": request}).data)