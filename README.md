# hospital-be
Back-end of hospital-dbms

Run DynamoDB by Docker:
```bash	
docker pull amazon/dynamodb-local
docker run -p 8000:8000 amazon/dynamodb-local
```

Run Django project with Python 3.10.0:
```bash
python3 -m pip install -r requirements.txt
python3 manage.py runserver
```
