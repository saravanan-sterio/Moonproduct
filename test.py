import psycopg2
from faker import Faker
import random,string
connection = psycopg2.connect(host='localhost', database='moonproduct', user='postgres', password='steriowolf')
cursor = connection.cursor()
print(connection.closed)
fake=Faker()
for i in range(1,101):
    name=fake.name()
    Contact_number=int(''.join(random.choice(string.digits) for _ in range(5)))
    Contact_emailId=fake.email()
    cursor.execute('Insert into retailer ("name","Contact_number","Contact_emailId") VALUES (%s,%s,%s)',(name,Contact_number,Contact_emailId))
    connection.commit()
