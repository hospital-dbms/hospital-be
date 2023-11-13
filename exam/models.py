import os
from pynamodb.models import Model
from pynamodb.attributes import *
from dotenv import load_dotenv

load_dotenv()

class Appointment(Model):
    class Meta:
        table_name = "appointment"
        host = os.environ.get('DYNAMODB_HOST')
    id = NumberAttribute(hash_key=True)
    date = UTCDateTimeAttribute(null=True)
    customer = NumberAttribute(null=True)
    doctor = NumberAttribute(null=True)
    
class PaymentMethod(Model):
    class Meta:
        table_name = "payment_method"
        host = os.environ.get('DYNAMODB_HOST')
    name = UnicodeAttribute(hash_key=True)