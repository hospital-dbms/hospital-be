from django.urls import path
from .views import PaymentMethodList, PaymentMethodDetail

urlpatterns = [
    path('payment_methods/', PaymentMethodList.as_view()),
    path('payment_methods/<str:name>/', PaymentMethodDetail.as_view()),
]