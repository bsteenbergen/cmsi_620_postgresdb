import csv

print('BEGIN;')

SOURCE = 'GlobalLandTemperaturesByCity.csv'
with open(SOURCE, 'r+', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        id = row[0]
        if row[1] == '' or row[2] == '':
            continue
        else:
            avg_temp = row[1]
            avg_temp_uncertainty = row[2]
        print(f'INSERT INTO temperature VALUES(\'{id}\', {avg_temp}, {avg_temp_uncertainty});')

print('COMMIT;')
