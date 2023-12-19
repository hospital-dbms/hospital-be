from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.http import Http404, JsonResponse

class AppointmentAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            # If a specific appointment ID is provided, retrieve that appointment
            try:
                appointment = Appointment.get(hash_key=pk)
                serializer = AppointmentSerializer(appointments, many = True)

                return Response(serializer.data)
            except Appointment.DoesNotExist:
                raise Http404("Appointment does not exist")

        # If no appointment ID is provided, check if a phone number is provided in the query parameters
        doctor = request.query_params.get('doctor', None)
        if doctor:
            # Query appointments by phone number
            print('doctor', doctor)
            appointments = Appointment.scan(Appointment.doctor==int(doctor))
            print('appointment',appointments)
            serializer = AppointmentSerializer(appointments, many = True)
            return Response(serializer.data)
        
        # If no specific parameters are provided, return all appointments
        appointments = Appointment.scan()
        serializer = AppointmentSerializer(appointments, many = True)
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
