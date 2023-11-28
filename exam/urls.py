from django.urls import path
from .views import *

urlpatterns = [
    path('appointments/', AppointmentAPIView.as_view()),
]