import sqlite3,app
import csv 

con = sqlite3.connect('gps.db')
cursor = bd.cursor()

with open('database/rutas.csv') as f:
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
            datos = (row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8], row[9])
            cursor.execute('''INSERT INTO data(id,lat,lon,velo,angu,fecha,hora,onoff,nsat) VALUES (?,?,?,?,?,?,?,?,?)''',datos)

con.commit()
cursor.close()