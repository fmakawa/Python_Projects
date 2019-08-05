import psycopg2
from psycopg2 import Error
from psycopg2.extras import execute_values

connection = psycopg2.connect(user = "recipesapi",
                            password = "recipesapi",
                            host = "postgres",
                            port = "5432",
                            database = "recipesapi")


try:
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

except (Exception, psycopg2.DatabaseError) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

###----------------------------------------- CREATE TABLE - RECIPES -----------------------------------------####
try:
    connection = psycopg2.connect(user = "recipesapi",
                            password = "recipesapi",
                            host = "postgres",
                            port = "5432",
                            database = "recipesapi")
    cursor = connection.cursor()
    print ( connection.get_dsn_parameters(),"\n")

    create_table_query = """CREATE TABLE IF NOT EXISTS recipesseq(
          ID SERIAL PRIMARY KEY,
          NAME          TEXT    NOT NULL,
          PREP_TIME           INT    NOT NULL,
          DIFFICULTY           INT    NOT NULL,
          VEGETARIAN          BOOLEAN    NOT NULL
          ); """

    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")
except (Exception, psycopg2.DatabaseError) as error :
    print ("Error while creating PostgreSQL table", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

###----------------------------------------- ADD INITIAL RECIPE -----------------------------------------####
connection = psycopg2.connect(user = "recipesapi",
                            password = "recipesapi",
                            host = "postgres",
                            port = "5432",
                            database = "recipesapi")
try:
    cursor = connection.cursor()
    print ( connection.get_dsn_parameters(),"\n")

    records_to_insert = [('salad', 30, 2, True),
                       ('tasty goulash', 60, 3, False),
                       ('stew', 95, 2, False),
                       ('sadza', 45, 1, True),
                       ('salad and chips', 30, 2, True)]

    sql_insert_query = """ INSERT INTO recipesseq (name, prep_time, difficulty, vegetarian)
                    SELECT * FROM (VALUES %s) s
                    WHERE NOT EXISTS (SELECT 1 FROM recipesseq) """

    cursor = connection.cursor()
    execute_values(cursor,sql_insert_query, records_to_insert)
    #result  = execute_values(cursor,sql_insert_query, records_to_insert)
    connection.commit()
    print (cursor.rowcount, "Record(s) inserted successfully into recipe table")
except (Exception, psycopg2.DatabaseError) as error :
    print("Failed inserting record into recipe table {}".format(error))
finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

###----------------------------------------- ADD RECIPE -----------------------------------------####
def dbAddRecipe(name, prep_time, difficulty, vegetarian):
    connection = psycopg2.connect(user = "recipesapi",
                            password = "recipesapi",
                            host = "postgres",
                            port = "5432",
                            database = "recipesapi")
    try:
       postgres_insert_query_one = """ INSERT INTO recipesseq (NAME, PREP_TIME, DIFFICULTY, VEGETARIAN) VALUES ('%s',%d,%d,%s)""" % (name, prep_time, difficulty, vegetarian)
       #postgres_insert_query_two = """ INSERT INTO recipesseq (NAME, PREP_TIME, DIFFICULTY, VEGETARIAN) VALUES ('sadza',30,5,True)"""
       cursor = connection.cursor()
       cursor.execute(postgres_insert_query_one)
       #cursor.execute(postgres_insert_query_two)
       connection.commit()
       print ("Records inserted successfully into recipe")
    except (Exception, psycopg2.DatabaseError) as error :
        if(connection):
            connection.rollback()
        print("Failed inserting record into recipe table {}".format(error))
    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

###----------------------------------------- UPDATE RECIPE -----------------------------------------####
def dbUpdateRecipe():
    try:
       cursor = connection.cursor()
       print ("Table Before updating record ")
       sql_select_query = """select * from recipe where id = 1"""
       cursor.execute(sql_select_query)
       record = cursor.fetchone()
       print (record)
       # Update single record now
       sql_update_query = """Update recipe set price = 1000 where id = 1"""
       cursor.execute(sql_update_query)
       print ("Table Record Updated successfully ")
       print("Table After updating record ")
       cursor.execute(sql_select_query)
       record = cursor.fetchone()
       print(record)
    except (Exception, psycopg2.DatabaseError) as error :
        print ("Error while connecting to PostgreSQL", error)
    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
###----------------------------------------- DELETE RECIPE -----------------------------------------####
def dbDeleteRecipe():
    try:
       cursor = connection.cursor()
       # Delete single record now
       ps_delete_query = """Delete from recipe where id = 5"""
       cursor.execute(ps_delete_query)
       print (" Record deleted successfully ")
    except (Exception, psycopg2.DatabaseError) as error :
        print ("Error while connecting to PostgreSQL", error)
    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
###----------------------------------------- FIND RECIPE -----------------------------------------####

def dbFindRecipe():
    PostgreSQL_select_Query = "select * from recipe"
    cursor = connection.cursor()
    cursor.execute(PostgreSQL_select_Query)
    recipe_records_one = cursor.fetchone()
    print ("Printing first record", recipe_records_one)
    recipe_records_two = cursor.fetchone()
    print("Printing second record", recipe_records_two)
    cursor.close()
    connection.close()
###----------------------------------------- ALL RECIPES -----------------------------------------####

def dbGetAllRecipes():
    try:
       PostgreSQL_select_Query = "select * from recipe"
       cursor = connection.cursor()
       cursor.execute(PostgreSQL_select_Query)
       # use fetchall method to fetch all the rows from database table
       recipe_records = cursor.fetchall()
       print ("Displaying rows from recipe table using cursor.fetchall")
       for row in recipe_records:
           print (row)
    except (Exception, psycopg2.DatabaseError) as error :
        print ("Error while connecting to PostgreSQL", error)
    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
###----------------------------------------- RATINGS -----------------------------------------####
