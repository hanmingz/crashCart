import socket
from parse import *
from getmac import get_mac_address
import mysql.connector
import time
import datetime
import tkinter as tk

def getMac():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	ip_addr = s.getsockname()[0]
	s.close()

	ip_field = parse("{}.{}.{}.{}", ip_addr)
	ip_router = "{}.{}.{}.1".format(ip_field[0], ip_field[1], ip_field[2])

	ip_mac = get_mac_address(ip=ip_router)
	return ip_mac

def connectSQL():
	pw = input("Enter password to MySQL: ")
	cnx = mysql.connector.connect(user = 'masterUsername', password = pw,
	host = 'crashcart.cf5ytddocao2.us-east-1.rds.amazonaws.com', database = 'CrashCart', port = 3306)
	cursor = cnx.cursor()
	return (cnx, cursor)

def initCart(cnx, cursor, cId):
	cursor.execute(f"""CREATE TABLE IF NOT EXISTS cart{cId}(medicine VARCHAR(30) PRIMARY KEY, 
	quantity INT, description VARCHAR(30), expiration DATE, FOREIGN KEY(description) 
	REFERENCES pharmacy(name))""")
	cnx.commit()
	

def cartStatus(cnx, cursor, cId, status, mac):
	timestamp = datetime.datetime.now() 
	timestamp.strftime('%Y-%m-%d %H:%M:%S')
	try:
		add_cart = (f"""INSERT INTO cartTable (cartId, cartStatus, macAddr, lastAccess)
		 VALUES(%s, %s, %s, %s)""")
		cursor.execute(add_cart, (cId, status, mac, timestamp))
		cnx.commit()
	except:
		cursor.execute(f"""UPDATE cartTable SET cartStatus = %s, macAddr = %s, lastAccess = %s
			WHERE cartId = %s""", (status, mac, timestamp, cId))
		cnx.commit()


def getAllMedicine(cnx, cursor, cId):
	query = (f"""SELECT medicine, quantity, expiration FROM cart{cId}""")
	cursor.execute(query)
	return cursor

def getMedicine(cnx, cursor, cId, med):
	query = (f"""SELECT medicine, quantity, expiration FROM cart{cId} WHERE medicine= %s""")
	cursor.execute(query, (med, ))
	return cursor

def updateMedicine(cnx, cursor, med, quantity, exp, cId):
	try:
		add_medicine = (f"""INSERT INTO cart{cId} (medicine, quantity, description, expiration) 
			VALUES(%s, %s, %s, %s)""")
		add_med = (med, quantity, med, exp)
		cursor.execute(add_medicine, add_med)
		cnx.commit()

	except:
		cursor.execute(f"""UPDATE cart{cId} SET quantity = %s, expiration = %s
			WHERE medicine = %s""", (quantity, exp, med))
		cnx.commit()

def disconnectSQL(cnx, cursor):
	cursor.close()
	cnx.close()
	print("MySQL connection closed successfully")
