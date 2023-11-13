import os
from pynamodb.models import Model
from pynamodb.attributes import *
from dotenv import load_dotenv

load_dotenv()

class UserModel(Model):
    class Meta:
        table_name = "user"
        host = os.environ.get('DYNAMODB_HOST')

    id = UnicodeAttribute(hash_key=True)
    email = UnicodeAttribute(null=True)
    first_name = UnicodeAttribute(null=True)
    last_name = UnicodeAttribute(null=True)

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





