import getpass
import csv
import pandas as pd
import json
import sqlite3


class Config:
    database = "Cities.db"
    tableName = 'city'
    jsonFile = "/home/" + getpass.getuser() + "/Desktop/cities.json"


try:
    connection = sqlite3.connect(Config.database)
    conn = connection.cursor()
except Exception as e:
    print(e)


def create_table():
    with open(Config.jsonFile) as file:
        data = json.load(file)
    df = pd.DataFrame(data)
    try:
        df.to_sql(Config.tableName, connection)
        print("table created successfully")
    except ValueError:
        conn.execute(f"SELECT * FROM {Config.tableName} WHERE id=2")
        print(conn.fetchall())


def convert_csv():
    try:
        data = conn.execute(f"SELECT id,name,state FROM {Config.tableName}")
        with open('../output.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['id', 'name', 'state'])
            writer.writerows(data)
    except:
        print("table does not exist")


create_table()
convert_csv()
