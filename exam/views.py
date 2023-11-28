from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.http import Http404, JsonResponse

class AppointmentAPIView(APIView):
    def get(self, request):
        appointments = Appointment.scan()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            appointment = Appointment(**serializer.validated_data)
            appointment.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            appointment = Appointment.get(hash_key=pk)
        except Appointment.DoesNotExist:
            raise Http404("Appointment does not exist")

        serializer = AppointmentSerializer(appointment, data=request.data)
        if serializer.is_valid():
            for attr, value in serializer.validated_data.items():
                setattr(appointment, attr, value)
            appointment.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            appointment = Appointment.get(hash_key=pk)
        except Appointment.DoesNotExist:
            raise Http404("Appointment does not exist")

        appointment.delete()
        return JsonResponse({'message': 'Appointment deleted successfully.'}, status=200)
