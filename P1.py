import MySQLdb as my

def order_history_generator():

    try:
        db = my.connect("localhost","root","Coder100","northWindDB")
    except my.Error as e:
        print(f"Cannot connect to database: {e}")
    
    cursor = db.cursor()

    cursor.execute(' SELECT * FROM Orders WHERE CustomerID="VINET" ')

    for row in cursor.fetchall():
        yield row
    
def main():
    # use next() to get a row
    print(order_history_generator().next())  #pylint: disable=maybe-no-member

    # or can iterate through all with a for loop
    for row in order_history_generator():
        print(row)

if '__main__'== __name__:
    main()
