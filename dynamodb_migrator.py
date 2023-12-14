from user.models import *
from article.models import *
from exam.models import *

UserModel.create_table(read_capacity_units=5, write_capacity_units=1)
# Doctor.create_table(read_capacity_units=5, write_capacity_units=1)
# Customer.create_table(read_capacity_units=5, write_capacity_units=1)
# Admin.create_table(read_capacity_units=5, write_capacity_units=1)

Article.create_table(read_capacity_units=10, write_capacity_units=1)
Tag.create_table(read_capacity_units=10, write_capacity_units=1)

Appointment.create_table(read_capacity_units=10, write_capacity_units=1)
PaymentMethod.create_table(read_capacity_units=10, write_capacity_units=1)


# test database created
from pynamodb.connection import Connection

# Connect to DynamoDB
conn = Connection(host="http://localhost:8000")

# List all tables
tables = conn.list_tables()
print("Tables:", tables)

appointments = Appointment.scan()
for appointment in appointments:
    print(appointment.attribute_values)

# If you want to print specific attributes of each item, you can do something like this:
for appointment in appointments:
    print(f"Appointment ID: {appointment.id}, Date: {appointment.date}, Customer: {appointment.customer}, Doctor: {appointment.doctor}")