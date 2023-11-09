# hospital-be
Back-end of hospital-dbms

Run DynamoDB by Docker:
```bash	
docker pull amazon/dynamodb-local
docker run -p 8000:8000 amazon/dynamodb-local
```

Run Django to create tables in DynamoDB with Python 3.10.0:
```bash
python3 -m pip install -r requirements.txt
python3 .\\dynamodb_migrator.py
aws dynamodb list-tables --endpoint-url http://localhost:8000
```


