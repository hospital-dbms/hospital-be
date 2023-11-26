from .models import *

class AppointmentSerializer:
    @staticmethod
    def serialize(appointment: Appointment) -> dict:
        return {
            'id': appointment.id,
            'date': appointment.date.isoformat() if appointment.date else None,
            'customer': appointment.customer,
            'doctor': appointment.doctor
        }

    @staticmethod
    def deserialize(data: dict) -> Appointment:
        return Appointment(
            id=data.get('id'),
            date=data.get('date'),
            customer=data.get('customer'),
            doctor=data.get('doctor')
        )
    
class PaymentMethodSerializer:
    def __init__(self, data=None):
        self.data = data

    def is_valid(self):
        # Add your validation logic here
        # If the data is invalid, add the errors to self.errors and return False
        # If the data is valid, return True
        if 'name' not in self.data:
            self.errors['name'] = 'This field is required.'
            return False
        return True

    def serialize(self, payment_method: PaymentMethod) -> dict:
        return {
            'name': payment_method.name,
        }

    def deserialize(self) -> PaymentMethod:
        return PaymentMethod(
            name=self.data.get('name'),
        )