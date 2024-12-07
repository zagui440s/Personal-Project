from django.urls import path
from .views import ChildListCreateAPIView, LocationListCreateAPIView, APIInfoAPIView

urlpatterns = [
    path('', APIInfoAPIView.as_view(), name='api-info'),  # Root API endpoint
    path('children/', ChildListCreateAPIView.as_view(), name='child-list-create'),
    path('locations/', LocationListCreateAPIView.as_view(), name='location-list-create'),
]