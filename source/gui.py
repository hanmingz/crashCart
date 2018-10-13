import tkinter as tk
from functions import *
from guiFunctions import *

def runGui():
	def closeWindow(cnx, cursor):
		disconnectSQL(cnx, cursor)
		root.destroy()


	def btnUseFcn():
		medList.pack_forget()

	def btnListFcn():
		lbxList.delete(0, tk.END)
		thisrow = '{:15s}  {:12s}  {:15s}'.format('MEDICINE', 'QUANTITY', 'EXPIRATION')
		lbxList.insert(tk.END, thisrow)
		getAllMedicine(cnx, cursor, ID)
		for(medicine, quantity, expiration) in cursor:
			thisrow = '{:15s}  {:12d}  {:15s}'.format(medicine.ljust(15)[:15], quantity, str(expiration))
			lbxList.insert(tk.END, thisrow)

		medList.pack()

	def btnMaintainFcn():
		medList.pack_forget()

	ID = 1
	global cnx
	global cursor
	(cnx, cursor) = connectSQL()
	initCart(cnx, cursor, ID)

	root = tk.Tk()
	root.protocol("WM_DELETE_WINDOW", lambda: closeWindow(cnx, cursor))
	root.geometry("480x300")
	root.title("Smart Crash Cart")

	# Menu bar
	menu = tk.Frame(root, width = 480, height = 60)
	btnUse = tk.Button(menu, text = 'USE', width = 16, command = btnUseFcn)
	btnUse.pack(side = tk.LEFT)
	btnList = tk.Button(menu, text = 'LIST', width = 16, command = btnListFcn)
	btnList.pack(side = tk.LEFT)
	btnMaintain = tk.Button(menu, text = 'MAINTANANCE', width = 16, command = btnMaintainFcn)
	btnMaintain.pack(side = tk.LEFT)

	# List
	medList = tk.Frame(root, width = 480, height = 260)
	lbxList = tk.Listbox(medList, width = 480, height = 260, font = ("Courier", 12))
	lbxList.pack()

	# running
	menu.pack()
	root.mainloop()