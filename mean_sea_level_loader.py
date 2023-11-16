import csv
from datetime import datetime

def format_date(input_date_str):
    month = int(input_date_str[1:3])
    day = int(input_date_str[4:6])
    year = int(input_date_str[7:])
    
    input_date = datetime(year, month, day)

    formatted_date = input_date.strftime("%Y-%m-%d")

    return formatted_date

print('BEGIN;')

SOURCE = 'Change_in_Mean_Sea_Levels.csv'

with open(SOURCE, 'r+', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        id = row[0]
        unit = row[5]
        sea_name = row[10]
        date_measured = format_date(row[11])
        sea_level = row[12]
        print(f'INSERT INTO mean_sea_level VALUES(\'{id}\', \'{unit}\', \'{sea_name}\', \'{date_measured}\', \'{sea_level}\');')

print('COMMIT;')