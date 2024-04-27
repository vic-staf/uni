import psycopg2
from config import load_config

def insert(name, phone):

    sql = """INSERT INTO phonebook(name, phone)
             VALUES(%s, %s) RETURNING id;"""
    
    id = None
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(sql, (name, phone,))

                # get the generated id back                
                rows = cur.fetchone()
                if rows:
                    id = rows[0]

                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return id

def updname(phone, name):
    """ Update name based on the phone """
    
    updated_row_count = 0

    sql = """ UPDATE phonebook
                SET name = %s
                WHERE phone = %s"""
    
    config = load_config()
    
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                
                # execute the UPDATE statement
                cur.execute(sql, (name, phone))
                updated_row_count = cur.rowcount

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return updated_row_count
    

def updphone(name, phone):
    """ Update phone based on the name """
    
    updated_row_count = 0

    sql = """ UPDATE phonebook
                SET phone = %s
                WHERE name = %s"""
    
    config = load_config()
    
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                
                # execute the UPDATE statement
                cur.execute(sql, (phone, name))
                updated_row_count = cur.rowcount

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return updated_row_count
    
def get(name = None, phone = None):
    """ Retrieve data from the phonebook table """
    config  = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                if name: cur.execute("SELECT phone FROM phonebook WHERE name = %s", (name,))
                elif phone: cur.execute("SELECT name FROM phonebook WHERE phone = %s", (phone,))
                else: cur.execute("SELECT name, phone FROM phonebook ORDER BY name")
                rows = cur.fetchall()

                print("The number of parts: ", cur.rowcount)
                print("--------------------------------------------")
                for row in rows:
                    print('\t', *row)
                print("--------------------------------------------")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def delete(name = None, phone = None):
    """ Delete entry by name or phone """

    rows_deleted  = 0
    sql = 'DELETE FROM parts WHERE part_id = %s'
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the UPDATE statement
                if name: cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
                else: cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
                rows_deleted = cur.rowcount

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return rows_deleted

print("QUERIES:")
print(" insert name phone")
print(" delname name")
print(" delphone phone")
print(" updname phone name")
print(" updphone name phone")
print(" get")
print(" getphone name")
print(" getname phone")

while True:
    s = input()
    a = s.split()
    if a[0] == "exit":
        break
    if a[0] == "insert":
        insert(a[1], a[2])
        print(f"INSERTED {a[1]}, {a[2]}")
    if a[0] == "delname":
        delete(name = a[1])
        print(f"DELETED {a[1]}")
    if a[0] == "delphone":
        delete(phone = a[1])
        print(f"DELETED {a[1]}")
    if a[0] == "updname":
        updname(a[1], a[2])
        print(f"UPDNAME {a[1]}, {a[2]}")
    if a[0] == "get":
        get()
    if a[0] == "getname":
        get(phone = a[1])
    if a[0] == "getphone":
        get(name = a[1])




