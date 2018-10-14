from functions import *

ID = 1
(cnx, cursor) = connectSQL()


initCart(cnx, cursor, ID)
thisMac = getMac()
cartStatus(cnx, cursor, ID, 3, thisMac)

name = findName(cnx, cursor, "123")
print(name)



cursor = getAllMedicine(cnx, cursor, ID)
for(medicine, quantity, expiration) in cursor:
	print("{}, {}, {}".format(medicine, quantity, expiration))

query = ("SELECT cartId, cartStatus, macAddr, lastAccess FROM cartTable")
cursor.execute(query)

for(cartId, cartStatus, macAddr, lastAccess) in cursor:
	print("{}, {}, {}, {}".format(cartId, cartStatus, macAddr, lastAccess))

disconnectSQL(cnx, cursor)