from django.urls import path
from .views import IndexView, SeriesView, SerieDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('series/', SeriesView.as_view(), name='series'),
    path('series/<int:serie_id>/', SerieDetailView.as_view(), name='serie_detail'),
]
