# hospital-be
Back-end of hospital-dbms

Run DynamoDB by Docker:
```powershell
docker pull amazon/dynamodb-local
docker run -p 8000:8000 amazon/dynamodb-local
```

Set up .env file:
```powershell
AWS_ACCESS_KEY_ID = <aws_access_key_id>
AWS_SECRET_ACCESS_KEY = <aws_secret_access_key>
REGION = us-east-1
DYNAMODB_HOST = http://localhost:8000
```

Run Django to create tables in DynamoDB with Python 3.10.0:
```powershell
python3 -m pip install -r requirements.txt
python3 .\dynamodb_migrator.py
```

Run Django server:
```powershell
python3 .\manage.py runserver
```
