from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.http import Http404, JsonResponse
from user.models import UserModel

class AppointmentAPIView(APIView):
    def get(self, request, phoneNumber=None):
        if not phoneNumber:
            appointments = Appointment.scan()
        else:
            appointments = Appointment.scan(Appointment.phoneNumber == phoneNumber)

        result_list = []

        for appointment in appointments:
            doctor_id = appointment.doctor
            user = UserModel.get(doctor_id)

            if user:
                # Step 4: Combine the results
                result = dict(appointment.attribute_values)
                result['doctor_name'] = user.name
                result_list.append(result)

        return Response(result_list)

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
