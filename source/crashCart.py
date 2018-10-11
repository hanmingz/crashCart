from functions import *

ID = 10
(cnx, cursor) = connectSQL()


initCart(cnx, cursor, ID)
thisMac = getMAC()
cartStatus(cnx, cursor, ID, 3, thisMac)

updateMedicine(cnx, cursor, "Ibuprofen", 100, "2019-5-30", ID)
updateMedicine(cnx, cursor, "H2O2", 100, "2020-5-30", ID)
updateMedicine(cnx, cursor, "O2", 1, "2022-12-31", ID)

cursor = getAllMedicine(cnx, cursor, ID)
for(medicine, quantity, expiration) in cursor:
	print("{}, {}, {}".format(medicine, quantity, expiration))

updateMedicine(cnx, cursor, "Ibuprofen", 50, "2018-12-31", ID)

cursor = getMedicine(cnx, cursor, ID, "Ibuprofen")
for(medicine, quantity, expiration) in cursor:
	print("{}, {}, {}".format(medicine, quantity, expiration))

query = ("SELECT cartId, cartStatus, macAddr, lastAccess FROM cartTable")
cursor.execute(query)

for(cartId, cartStatus, macAddr, lastAccess) in cursor:
	print("{}, {}, {}, {}".format(cartId, cartStatus, macAddr, lastAccess))

disconnectSQL(cnx, cursor)