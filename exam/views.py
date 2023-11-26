from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import *
from .serializers import *

class PaymentMethodList(APIView):
    def get(self, request, format=None):
        payment_methods = PaymentMethod.scan()  # use scan() to get all items
        serializer = PaymentMethodSerializer(payment_methods)  # pass the data to the serializer
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PaymentMethodSerializer(data=request.data)
        if serializer.is_valid():
            payment_method = PaymentMethod(**serializer.validated_data)
            payment_method.save()  # use save() to create a new item
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PaymentMethodDetail(APIView):
    def get_object(self, name):
        try:
            return PaymentMethod.get(name)  # use get() to get a single item
        except PaymentMethod.DoesNotExist:
            raise Http404

    def get(self, request, name, format=None):
        payment_method = self.get_object(name)
        serializer = PaymentMethodSerializer(payment_method)  # pass the data to the serializer
        return Response(serializer.data)