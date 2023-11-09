import boto3
import os

region = 'us-east-1'
aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')


def create_table(ddb, table_name, key_attribute, read_capacity, write_capacity):
    return ddb.create_table(
        TableName=table_name,
        KeySchema=[{'AttributeName': key_attribute, 'KeyType': 'HASH'}],
        AttributeDefinitions=[{'AttributeName': key_attribute, 'AttributeType': 'S'}],
        ProvisionedThroughput={'ReadCapacityUnits': read_capacity, 'WriteCapacityUnits': write_capacity}
    )

def show_all_tables(ddb):
    return [table.name for table in ddb.tables.all()]

def show_all_items(ddb, table_name):
    table = ddb.Table(table_name)
    items = table.scan()['Items']
    for item in items:
        print(item)

def delete_table(ddb, table_name):
    table = ddb.Table(table_name)
    if table.name in show_all_tables(ddb):
        table.delete()
        table.wait_until_not_exists()
        print(f"Deleted table: {table_name}")
    else:
        print(f"Table {table_name} does not exist")

def main():
    ddb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000', region_name=region, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

    create_table(ddb, 'Article', 'article_id', 10, 10)
    create_table(ddb, 'Tag', 'tag_id', 10, 10)
    create_table(ddb, 'Doctor', 'user_id', 10, 10)
    create_table(ddb, 'Customer', 'user_id', 10, 10)
    create_table(ddb, 'Admin', 'user_id', 10, 10)
    create_table(ddb, 'Appointment', 'appointment_id', 10, 10)
    create_table(ddb, 'PaymentMethod', 'payment_method_id', 10, 10)

    show_all_tables(ddb)

if __name__ == "__main__":
    main()