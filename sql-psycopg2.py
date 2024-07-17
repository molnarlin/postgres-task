import psycopg2

#connect to chinook 
connection = psycopg2.connect(database="chinook")

#build a cursor object of the database
cursor = connection.cursor()

#Query 1 - select all records from the "Artist" table
#cursor.execute('SELECT * FROM "Artist"')

#Query 2 - select only the "Name" column from the "Artist" table
#cursor.execute('SELECT "Name" FROM "Artist"')

#Query 3 - select only the "Queen" from the "Artist" table
#cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

#Query 4- select only the "ArtistId" #51 from the "Artist" table
#cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

#Query 5- select only the albums with "ArtistId" #51 from the "Album" table
#cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

#Query 6- select all track where the composer is Queen from the Track table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

#fetch the results (multiple)
results = cursor.fetchall()

#fetc the results (single)
#results = cursor.fetchone()

#close the connection
connection.close()

#print results
for result in results:
    print(result)
