from typing import Optional

import yaml
import requests
import os
import sys
from datetime import datetime
import csv
import psycopg2
from pathlib import Path

DB_USER=os.environ.get('DB_USER')
DB_PASSWORD=os.environ.get('DB_PASSWORD')

if DB_USER is None or DB_PASSWORD is None:
    print("No DB_USER or DB_PASSWORD env variables have been found, exiting", file=sys.stderr)
    sys.exit(1)

class Processor:
    def __init__(self):
        self.url = None
        self.conn = None
        self.process_manifest()
        self.init_conn_to_db()

    def process_manifest(self):
        with open(Path("manifest.yaml")) as f:
            self.url = yaml.safe_load(f.read())['deaths']['url']

    def get_deaths_raw(self):
        data = requests.get(self.url).text
        path = Path("file_with_data")
        if path.exists():
            return
        with open(path,'w') as f:
            f.write(data)

    def insert_records(self):
        cursor = self.conn.cursor()
        cursor.execute("select max(timestamp) from deaths;")
        count = cursor.fetchone()
        if count[0] is None:
            self.insert_all(cursor)
        else:
            self.insert_until(cursor,count[0])



    def init_conn_to_db(self):
        self.conn = psycopg2.connect(dbname="covid", user=DB_USER, password=DB_PASSWORD, host="localhost")

    def insert_all(self, cursor):
        with open(Path("file_with_data"), newline='') as f:
            for row in csv.DictReader(f):
                latitude = row['Lat']
                longitude = row['Long'],
                location = "-".join([row['Country/Region'],row['Province/State']])
                for k,v in row.items():
                    if k not in ('Lat', 'Long', 'Country/Region', 'Province/State'):
                        cursor.execute('insert into deaths values (%s,%s,%s,%s,%s)', (location, latitude, longitude,k, v))
        self.conn.commit()
        cursor.close()
        self.conn.close()

    def insert_until(self,cursor, count:datetime):
        format = f'{count.month}/{count.day}/{str(count.year)[-2:]}'
        with open(Path("file_with_data"), newline='') as f:
            for row in csv.DictReader(f):
                if list(row.keys())[-1:][0] == format:
                    cursor.close()
                    self.conn.close()
                    return


if __name__ == '__main__':
    processor = Processor()
    processor.get_deaths_raw()
    processor.insert_records()


