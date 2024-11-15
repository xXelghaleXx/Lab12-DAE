from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Serie
from .serializers import SerieSerializer

class IndexView(APIView):
    def get(self, request):
        context = {'mensaje': 'Servidor activo'}
        return Response(context, status=status.HTTP_200_OK)


class SeriesView(APIView):
    def get(self, request):
        """Obtiene todas las series."""
        dataSeries = Serie.objects.all()
        serSeries = SerieSerializer(dataSeries, many=True)
        return Response(serSeries.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Crea una nueva serie."""
        serSerie = SerieSerializer(data=request.data)
        if serSerie.is_valid(raise_exception=True):
            serSerie.save()
            return Response(serSerie.data, status=status.HTTP_201_CREATED)
        return Response(serSerie.errors, status=status.HTTP_400_BAD_REQUEST)


class SerieDetailView(APIView):
    def get(self, request, serie_id):
        """Obtiene una serie por ID."""
        dataSerie = get_object_or_404(Serie, pk=serie_id)
        serSerie = SerieSerializer(dataSerie)
        return Response(serSerie.data, status=status.HTTP_200_OK)

    def put(self, request, serie_id):
        """Actualiza una serie por ID."""
        dataSerie = get_object_or_404(Serie, pk=serie_id)
        serSerie = SerieSerializer(dataSerie, data=request.data)
        if serSerie.is_valid(raise_exception=True):
            serSerie.save()
            return Response(serSerie.data, status=status.HTTP_200_OK)
        return Response(serSerie.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, serie_id):
        """Elimina una serie por ID."""
        dataSerie = get_object_or_404(Serie, pk=serie_id)
        dataSerie.delete()
        return Response({'mensaje': 'Serie eliminada'}, status=status.HTTP_204_NO_CONTENT)
