import mysql.connector
import time
import os

# db = mysql.connector.connect(host="localhost", user="root", password="skilover1!", database="testdatabase")
db = mysql.connector.connect(
    host=os.getenv('MYSQLHOST'),
    user=os.getenv('MYSQLUSER'),
    port=os.getenv('MYSQLPORT'),
    password=os.getenv('MYSQLPASSWORD'),
    database=os.getenv('MYSQLDATABASE'))


# # Creating a cursor object
cursor = db.cursor()
# cursor.execute("DROP TABLE Grid")
cursor.execute("CREATE TABLE Grid (id INT PRIMARY KEY AUTO_INCREMENT, lat FLOAT, lon FLOAT, forecast JSON, nextUpdateTime TIMESTAMP)")
query = "INSERT INTO Grid (lat, lon, forecast, nextUpdateTime) VALUES (%s, %s, %s, %s)"
values = (38.88, -77.1, '{"temperature": 72, "humidity": 50}', '2023-04-10 13:00:00')
cursor.execute(query, values)

# cursor.execute("SELECT * FROM Grid")
# rows = cursor.fetchall()
# for row in rows:
#   print(row)

db.commit()
# cursor.close()
db.close()

while True:
    print('hi')
    time.sleep(10)
