#Install mysql on computer


import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'dlehrjs1207'
    
    )

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE storeproj")
print("All Done!")