from dynamorm import DynaModel
from marshmallow import fields
from django.conf import settings
from django.contrib.auth.models import User


class Doctor(DynaModel):
    class Table:
        resource_kwargs = {
            'endpoinnt_url': settings.DB_ENDPOINT
        }
        name = 'DoctorTable'
        hash_key = 'user_id'
        read = 25
        write = 5
    
    class Schema:
        user_id = fields.Integer()

class Customer(DynaModel):
    class Table:
        resource_kwargs = {
            'endpoinnt_url': settings.DB_ENDPOINT
        }
        name = 'CustomerTable'
        hash_key = 'user_id'
        read = 25
        write = 5
    
    class Schema:
        user_id = fields.Integer()

class Admin(DynaModel):
    class Table:
        resource_kwargs = {
            'endpoinnt_url': settings.DB_ENDPOINT
        }
        name = 'AdminTable'
        hash_key = 'user_id'
        read = 25
        write = 5
    
    class Schema:
        user_id = fields.Integer()

class Appointment(DynaModel):
    class Table:
        resource_kwargs = {
            'endpoinnt_url': settings.DB_ENDPOINT
        }
        name = 'AppointmentTable'
        hash_key = 'appointment_id'
        read = 25
        write = 5
    
    class Schema:
        appointment_id = fields.Integer() 

class PaymentMethod(DynaModel):
    class Table:
        resource_kwargs = {
            'endpoinnt_url': settings.DB_ENDPOINT
        }
        name = 'PaymentMethodTable'
        hash_key = 'payment_method_id'
        read = 25
        write = 5
    
    class Schema:
        payment_method_id = fields.Integer() 

class Article(DynaModel):
    class Table:
        resource_kwargs = {
            'endpoinnt_url': settings.DB_ENDPOINT
        }
        name = 'ArticleTable'
        hash_key = 'article_id'
        read = 25
        write = 5
    
    class Schema:
        article_id = fields.Integer()

class Tag(DynaModel):
    class Table:
        resource_kwargs = {
            'endpoinnt_url': settings.DB_ENDPOINT
        }
        name = 'TagTable'
        hash_key = 'tag_id'
        read = 25
        write = 5
    
    class Schema:
        tag_id = fields.Integer()