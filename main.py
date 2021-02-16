import sqlite3
import csv

def readImage(file):
	file = open(file, 'rb').read()
	return file

data = sqlite3.connect('data.db')
cursor = data.cursor()
try:
	cursor.execute('''CREATE TABLE people (
		name TEXT,
		age TEXT,
		job TEXT,
		survived TEXT,
		avatar BLOB
	)''')

	male = sqlite3.Binary(open('male.jpg', 'rb').read())
	female = sqlite3.Binary(open('female.jpg', 'rb').read())
	child = sqlite3.Binary(open('child.jpg', 'rb').read())

	with open('titanic.csv') as csvfile:
		titanic = csv.reader(csvfile)
		for line in titanic:
			if line != ['Name', 'Age', 'Class/Dept', 'Fare', 'Joined', 'Job', 'Survived']:
				try:
					if float(line[1]) < 18:
						avatar = child
					elif 'Mr' in line[0] or 'Sir' in line[0] or 'Dr' in line[0]:
						avatar = male
					elif 'Mrs' in line[0] or 'Miss' in line[0] or 'Lady' in line[0]:
						avatar = female
					else:
						avatar = male
					cursor.execute(f'INSERT INTO people VALUES ("{line[0]}", "{line[1]}", "{line[5]}", "{line[6]}", "{avatar}")')
				except:
					pass
except:
	pass
survived = 0
not_survived = 0
for i in cursor.execute('SELECT survived FROM people'):
	if i[0] == 'TRUE':
		survived += 1
	elif i[0] == 'FALSE':
		not_survived += 1

print("Дети:")
for q in cursor.execute('SELECT name, age FROM people WHERE age < 18'):
	print(q)

print('-------------------------------')
print("Выжило:"+str(survived))
print("Не выжило:"+str(not_survived))

print('-------------------------------')
print("Палубная команда:")
for z in cursor.execute('SELECT * FROM people WHERE job = "Seaman"'):
	print(z)

data.commit()