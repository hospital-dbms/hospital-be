import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'hospital_be.settings'  # replace 'myproject.settings' with your actual settings module
django.setup()

from pynamodb.models import Model
from pynamodb.attributes import *
from dotenv import load_dotenv
from pynamodb.attributes import UnicodeAttribute, BooleanAttribute, UTCDateTimeAttribute
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

load_dotenv()

class UserModel(Model):
    class Meta:
        table_name = 'user'  # replace with your DynamoDB table name

    username = UnicodeAttribute(hash_key=True)
    password = UnicodeAttribute()
    is_staff = BooleanAttribute(default=False)

class Doctor(UserModel):
    class Meta:
        table_name = "doctor"
        host = os.environ.get('DYNAMODB_HOST')

class Customer(UserModel):
    class Meta:
        table_name = "customer"
        host = os.environ.get('DYNAMODB_HOST')

class Admin(UserModel):
    class Meta:
        table_name = "admin"
        host = os.environ.get('DYNAMODB_HOST')





