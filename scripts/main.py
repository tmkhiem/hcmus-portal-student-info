import os
import pyodbc
import json
import datetime

connection_string = os.environ['DB_CONNECTION_STRING']
print('Script started.')
print(connection_string[0:44])
conn = pyodbc.connect(connection_string) 

with conn.cursor() as cursor:
    cursor.execute(os.environ['DB_QUERY'])
    records = cursor.fetchone()

portal_stats = {
    'Portal 1': records[0],
    'Portal 2': records[1],
    'Portal 3': records[2],
    'Portal 4': records[3],
    'Portal 5': records[4],
    'Portal 6': records[5],
    'Portal 7': records[6],
    'Portal 8': records[7],
    'Portal 9': records[8],
    'Portal 10': records[9],
    'Portal 11': records[10],
    'Portal 12': records[11],
    'Portal 13': records[12],
    'Portal 14': records[13],
    'Portal 15': records[14],
    'Portal 16': records[15],
    'Portal 17': records[16],
    'Portal 18': records[17],
    'Portal 19': records[18],
    'Portal 20': records[19]                
}

utc_timestamp = datetime.datetime.now(datetime.timezone.utc)
vn_time = utc_timestamp + datetime.timedelta(hours=7)
formatted_time = vn_time.strftime("%b %d %Y, %H:%M")

with open('template.html', 'r') as file:
    template = file.read()

template = template.replace('{{stats}}', json.dumps(portal_stats)).replace('{{timestamp}}', formatted_time)

with open('index.html', 'w') as file:
    file.write(template)
