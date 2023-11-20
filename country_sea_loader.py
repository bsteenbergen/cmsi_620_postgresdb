import csv

print('BEGIN;')

SOURCE = 'country_sea.csv'

locations = set()
with open(SOURCE, 'r+', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        country = row[0].replace('\'', '')
        sea = row[1]
        print(f'INSERT INTO country_sea VALUES(\'{country}\', \'{sea}\');')
print(f"INSERT INTO country_sea VALUES('Côte D Ivoire', 'N/A');")
print(f"INSERT INTO country_sea VALUES('Czechia', 'N/A');")
print('COMMIT;')