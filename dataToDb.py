import psycopg2
from crawler import facebook
import time
import csv
from dotenv import load_dotenv
import os


try:
    print('start connection')
    connection_string = f"user={os.getenv('DB_USER')} " \
                     f"password={os.getenv('DB_PASSWORD')} " \
                     f"host={os.getenv('DB_HOST')} " \
                     f"port={os.getenv('DB_PORT')} " \
                     f"database={os.getenv('DB_NAME')}"

# Establish the connection
    connection = psycopg2.connect(connection_string)


    cursor = connection.cursor()
    print('start crawling')
    fb = facebook(depth=1)
    fb.login()
    if fb.verifyLogin():
        print("login successful")
    else:
        print("login failed")
        exit()

    with open('group.txt') as csv_file:
            groupName = []
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                groupName.append(row[0])
            # print(groupName)
    
    while True:
        for group in groupName:
            print("Crawling group: ", group)

            isTest = False
            fb.group(group, isTest)
            fb.write2DBOnlyNew(cursor, connection)
            #fb.write2File('output.txt')
        print("waiting for next loop...")
        time.sleep(2*60*60)

    print("Close driver")
    fb.driver.close()

except (Exception, psycopg2.Error) as error:
    print("Error pgadmin: ", error)
finally:
    # closing database connection.
    if(connection):
        cursor.close()
        connection.commit()
        connection.close()
        print("PostgreSQL connection is closed")