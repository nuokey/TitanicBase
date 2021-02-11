import sqlite3
import csv

def create_database():
	data = sqlite3.connect('data.db')
	cursor = data.cursor()
	try:
		cursor.execute('''CREATE TABLE people (
			name TEXT,
			age TEXT,
			job TEXT,
			survived TEXT
		)''')
	except:
		pass

	with open('titanic.csv') as csvfile:
		titanic = csv.reader(csvfile)
		for line in titanic:
			if line != ['Name', 'Age', 'Class/Dept', 'Fare', 'Joined', 'Job', 'Survived']:
				print(line)
				try:
					cursor.execute(f'INSERT INTO people VALUES ("{line[0]}", "{line[1]}", "{line[5]}", "{line[6]}")')
				except:
					pass

create_database()

survived = 0
not_survived = 0
for i in cursor.execute('SELECT survived FROM people'):
	if i[0] == 'TRUE':
		survived += 1
	elif i[0] == 'FALSE':
		not_survived += 1

print(survived)
print(not_survived)

data.commit()