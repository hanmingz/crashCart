import mysql.connector

cnx = mysql.connector.connect(user = 'masterUsername', password = 'Ambulance',
	host = 'crashcart.cf5ytddocao2.us-east-1.rds.amazonaws.com', database = 'CrashCart')
cursor = cnx.cursor()

#To add a cart
# add_cart = ("INSERT INTO cartTable "
# 	"(cartId, cartStatus)"
# 	"VALUES (%s, %s)")

# data_cart = (2, 0)
# cursor.execute(add_cart, data_cart)
# cnx.commit()

#change entry
# changeCartId = 1
# changeCartStatus = 1
# cursor.execute("""
# 	UPDATE cartTable
# 	SET cartStatus = %s
# 	WHERE cartId = %s
# 	""", (changeCartStatus, changeCartId))

cursor.execute("SHOW TABLES")
for x in cursor:
	print(x)

# cursor.execute("""CREATE TABLE cart1(medicine VARCHAR(30) PRIMARY KEY, 
# 	quantity INT, description VARCHAR(30), FOREIGN KEY(description) REFERENCES pharmacy(name))""")

# add_ibuprofen = ("""INSERT INTO pharmacy (name, quantity, description)
# 	VALUES(%s, %s, %s)""")
# ibuprofen = ("ibuprofen", 100, "kills pain")
# cursor.execute(add_ibuprofen, ibuprofen)

# cnx.commit()

# add_ibuprofen = ("""INSERT INTO cart1 (medicine, quantity, description)
# 	VALUES(%s, %s, %s)""")
# ibuprofen = ("ibuprofen", 3, "ibuprofen")
# cursor.execute(add_ibuprofen, ibuprofen)
# cnx.commit()
query = ("""SELECT name, quantity, description FROM pharmacy
	WHERE name = 'ibuprofen'""")
cursor.execute(query)

for (name, quantity, description) in cursor:
	print("{}, {}, {}".format(name, quantity, description))


#Print out all carts
# query = ("SELECT cartId, cartStatus FROM cartTable")
# cursor.execute(query)

# for(cartId, cartStatus) in cursor:
# 	print("{}, {}".format(cartId, cartStatus))

cursor.close()
cnx.close()