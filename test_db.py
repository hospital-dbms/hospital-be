from exam.models import Appointment
from pynamodb.connection import Connection

# Connect to DynamoDB running in a Docker container
conn = Connection(host="http://localhost:8000")

# Assuming the Appointment table is already created
# ...

# Scan and print all items in the Appointment table
appointments = Appointment.scan(connection=conn)
for appointment in appointments:
    print(appointment.attribute_values)

# If you want to print specific attributes of each item, you can do something like this:
for appointment in appointments:
    print(f"Appointment ID: {appointment.id}, Date: {appointment.date}, Customer: {appointment.customer}, Doctor: {appointment.doctor}")
