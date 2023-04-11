import mysql.connector
import time

# Establishing a connection to the MySQL database
db = mysql.connector.connect(
  host="containers-us-west-14.railway.app",
  user="root",
  password="bMaIkMPFghZRelELXvD1",
  database="railway"
)

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
