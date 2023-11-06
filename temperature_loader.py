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
            city = row[3].replace('\'', ' ')
            country = row[4].replace('\'', ' ')
            date_collected = row[0]
            avg_temp = row[1]
            avg_temp_uncertainty = row[2]
            location_key = (city, country)
            if location_key in locations:
                continue
            else:
                locations.add(location_key)
                print(f'INSERT INTO temperature VALUES(\'{city}\', \'{country}\', \'{date_collected}\', \'{avg_temp}\', \'{avg_temp_uncertainty}\');')

print('COMMIT;')
