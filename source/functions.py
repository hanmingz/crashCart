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
	cursor.execute("CREATE TABLE IF NOT EXISTS cart{}(medicine VARCHAR(30) PRIMARY KEY, quantity INT, description VARCHAR(30), expiration DATE, FOREIGN KEY(description) REFERENCES pharmacy(name))".format(cId))
	cnx.commit()


def cartStatus(cnx, cursor, cId, status, mac):
	timestamp = datetime.datetime.now()
	timestamp.strftime('%Y-%m-%d %H:%M:%S')
	try:
		add_cart = ("INSERT INTO cartTable (cartId, cartStatus, macAddr, lastAccess) VALUES(%s, %s, %s, %s)")
		cursor.execute(add_cart, (cId, status, mac, timestamp))
		cnx.commit()
	except:
		cursor.execute("UPDATE cartTable SET cartStatus = %s, macAddr = %s, lastAccess = %s WHERE cartId = %s", (status, mac, timestamp, cId))
		cnx.commit()


def getAllMedicine(cnx, cursor, cId):
	query = ("SELECT medicine, quantity, expiration FROM cart{}".format(cId))
	cursor.execute(query)
	return cursor

def getMedicine(cnx, cursor, cId, med):
	query = ("SELECT medicine, quantity, expiration FROM cart{} WHERE medicine= %s".format(cId))
	cursor.execute(query, (med, ))
	return cursor

def updateMedicine(cnx, cursor, med, quantity, exp, cId):
	try:
		add_medicine = ("INSERT INTO cart{} (medicine, quantity, description, expiration) VALUES(%s, %s, %s, %s)".format(cId))
		add_med = (med, quantity, med, exp)
		cursor.execute(add_medicine, add_med)
		cnx.commit()

	except:
		cursor.execute("UPDATE cart{} SET quantity = %s, expiration = %s WHERE medicine = %s".format(cId), (quantity, exp, med))
		cnx.commit()

def disconnectSQL(cnx, cursor):
	cursor.close()
	cnx.close()
	print("MySQL connection closed successfully")

def findName(cnx, cursor, bcode):
	query = ("SELECT name FROM pharmacy WHERE barcode LIKE '%{}%'".format(bcode))
	cursor.execute(query)
	ret = ''
	for name in cursor:
		ret = name
	return ret[0]