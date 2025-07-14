#1
import sqlite3

# Connect to (or create) a database file
conn = sqlite3.connect('roster.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the Roster table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
''')

print("✅ Table 'Roster' created successfully!")

# Commit changes and close connection
conn.commit()
conn.close()

#2
import sqlite3

# Connect to the database
conn = sqlite3.connect('roster.db')
cursor = conn.cursor()

# Insert data into Roster table
data = [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
]

cursor.executemany('''
    INSERT INTO Roster (Name, Species, Age)
    VALUES (?, ?, ?)
''', data)

print("✅ Data inserted successfully!")

# Commit and close connection
conn.commit()
conn.close()

#3
import sqlite3

conn = sqlite3.connect('roster.db')
cursor = conn.cursor()

cursor.execute('''
    UPDATE Roster
    SET Name = ?
    WHERE Name = ?
''', ("Ezri Dax", "Jadzia Dax"))

conn.commit()
print("✅ Name updated successfully!")

conn.close()

#4
import sqlite3

conn = sqlite3.connect('roster.db')
cursor = conn.cursor()

cursor.execute('''
    SELECT Name, Age
    FROM Roster
    WHERE Species = ?
''', ("Bajoran",))

rows = cursor.fetchall()

print("🖖 Bajoran Members:")
for name, age in rows:
    print(f"Name: {name}, Age: {age}")

conn.close()
