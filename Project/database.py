import mysql.connector 
mydb = mysql.connector.connect(
   host="localhost",
   user="root", 
   password="", 
   database="ebike"
)

c = mydb.cursor()

def create_table(): 
   c.execute('CREATE TABLE IF NOT EXISTS DEALER(dealer_id TEXT, dealer_name TEXT, dealer_city TEXT, dealer_pin TEXT, dealer_street TEXT)')

# def add_data(dealer_id, dealer_name, dealer_city, dealer_pin, dealer_street): 
#    c.execute('INSERT INTO DEALER(dealer_id, dealer_name, dealer_city, dealer_pin, dealer_street) VALUES (%s,%s,%s,%s,%s)',(dealer_id, dealer_name, dealer_city, dealer_pin, dealer_street))
#    mydb.commit()

# def view_all_data(): 
#    c.execute('SELECT * FROM DEALER') 
#    data = c.fetchall()
#    return data

# def view_only_dealer_names(): 
#    c.execute('SELECT dealer_name FROM DEALER') 
#    data = c.fetchall()
#    return data

# def get_dealer(dealer_name): 
#    c.execute('SELECT * FROM DEALER WHERE dealer_name="{}"'.format(dealer_name)) 
#    data = c.fetchall()
#    return data

# def edit_dealer_data(new_dealer_id, new_dealer_name, new_dealer_city, new_dealer_pin, new_dealer_street, dealer_id, dealer_name, dealer_city, dealer_pin, dealer_street): 
#    c.execute("UPDATE DEALER SET dealer_id=%s, dealer_name=%s, dealer_city=%s, dealer_pin=%s, dealer_street=%s WHERE dealer_id=%s and dealer_name=%s and dealer_city=%s and dealer_pin=%s and dealer_street=%s", (new_dealer_id, new_dealer_name, new_dealer_city, new_dealer_pin, new_dealer_street, dealer_id, dealer_name, dealer_city, dealer_pin, dealer_street)) 
#    mydb.commit()
#    data = c.fetchall()
#    return data

def delete_data(dealer_name): 
   c.execute('DELETE FROM DEALER WHERE dealer_name="{}"'.format(dealer_name))