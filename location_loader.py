import csv
import re

print('BEGIN;')

SOURCE = 'GlobalLandTemperaturesByCity.csv'

locations = set()
with open(SOURCE, 'r+', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)

    rows = []
    for row in reader:
        rows.append(tuple(row))
    
    list(set([r for r in rows]))

    for row in rows:
        if '' in row:
            continue
        else:
            city = row[3]
            country = row[4]
            latitude = row[5]
            longitude = row[6]
            location_key = (city, country)
            if location_key in locations:
                print("HELLOEF:OEHFIAEFHAOEI")
                continue
            else:
                locations.add(location_key)
                print(f'INSERT INTO location VALUES(\'{city}\', \'{country}\', \'{latitude}\', \'{longitude}\');')

print('COMMIT;')