import psycopg2
try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "Jasper",
                                  host = "localhost",
                                  port = "5432",
                                  database = "jeopardy")

    cursor = connection.cursor()
    select_query = '''SELECT * FROM questions'''
    cursor.execute(select_query)
    print("selecting")
    records = cursor.fetchall()
    print("printing")
    for row in records:
        print(row[0])
        print(row[1])
        print(row[2])
        print(row[3])
        print(row[4])
        print(row[5])
        print(row[6])
except (Exception, psycopg2.Error) as error :
    print("Error whiel fetching data from PostgreSQL", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")