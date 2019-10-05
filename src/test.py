from pprint import pprint
import json
import mysql.connector as mysql


with open('/home/varun/Desktop/data.json') as f:
    data = json.load(f)

pprint(type(data))

config = {
  'user': 'root',
  'password': '0404',
  'host': '127.0.0.1',
  'database': 'solutionsxhackathon',
  'raise_on_warnings': True
}

cnx = mysql.connection.MySQLConnection(**config)
cursor = cnx.cursor()

cursor.execute("SHOW TABLES")

cnx.close()
