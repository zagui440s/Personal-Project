from django.urls import path
from .views import get_user_api_location

urlpatterns = [
    path("", get_user_api_location.as_view(), name="get_user_api_location"),
]