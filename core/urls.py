from django.urls import path
from core.views import CustomAuthToken


urlpatterns = [

    path('token/', CustomAuthToken.as_view())
]