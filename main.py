import sqlite3
import csv

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
			try:
				cursor.execute(f'INSERT INTO people VALUES ("{line[0]}", "{line[1]}", "{line[5]}", "{line[6]}")')
			except:
				pass
data.commit()