import csv

print('BEGIN;')

SOURCE = 'GlobalLandTemperaturesByCity.csv'

with open(SOURCE, 'r+', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        city = row[3].replace('\'', ' ')
        country = row[4].replace('\'', ' ')
        date_collected = row[0]
        avg_temp = row[1]
        avg_temp_uncertainty = row[2]
        print(f'INSERT INTO temperature (city, country, date_collected, avg_temp, avg_temp_uncertainty) VALUES(\'{city}\', \'{country}\', \'{date_collected}\', NULLIF(\'{avg_temp}\', \'\')::float, NULLIF(\'{avg_temp_uncertainty}\', \'\')::float);')

print('COMMIT;')
