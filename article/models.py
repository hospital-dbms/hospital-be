import os
from pynamodb.models import Model
from pynamodb.attributes import *
from dotenv import load_dotenv

load_dotenv()

class Article(Model):
    class Meta:
        table_name = "article"
        host = os.environ.get('DYNAMODB_HOST')
    id = NumberAttribute(hash_key=True)
    title = UnicodeAttribute(null=False)
    tag = UnicodeAttribute(null=True)
    content = UnicodeAttribute(null=True)

class Tag(Model):
    class Meta:
        table_name = "tag"
        host = os.environ.get('DYNAMODB_HOST')
    name = UnicodeAttribute(hash_key=True)