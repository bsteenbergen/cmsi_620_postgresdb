import csv
import re

print('BEGIN;')

SOURCE = 'GlobalLandTemperaturesByCity.csv'
with open(SOURCE, 'r+', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    count = 0
    while count < 5:
        for row in reader:
            if '' in row:
                continue
            else:
                city = row[3]
                country = row[4]
                latitude = row[5]
                longitude = row[6]
            print(f'INSERT INTO location VALUES(\'{city}\', \'{country}\', \'{latitude}\', \'{longitude}\');')
    count += 1

print('COMMIT;')