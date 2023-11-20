import csv

print('BEGIN;')

SOURCE = 'owid-co2-data.csv'

with open(SOURCE, 'r+', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        country = row[0].replace('\'', ' ')
        year_measured = row[1]
        population = row[3]
        co2 = row[7]
        cumulative_co2 = row[25]
        print(f'INSERT INTO emissions (country, year_measured, population, co2, cumulative_co2) VALUES(\'{country}\', \'{year_measured}\', \'{population}\', \'{co2}\', \'{cumulative_co2}\');')

print('COMMIT;')