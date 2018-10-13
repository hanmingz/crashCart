import tkinter as tk
from functions import *
from guiFunctions import *

def runGui():
	def closeWindow(cnx, cursor):
		disconnectSQL(cnx, cursor)
		root.destroy()


	def btnUseFcn():
		print("Clicked Use")

	def btnListFcn():
		print("Clicked List")

	def btnMaintainFcn():
		print("Clicled Maintain")

	ID = 1
	(cnx, cursor) = connectSQL()

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
	lbxList = tk.Listbox(medList, width = 480, height = 260)
	lbxList.pack()

	# running
	menu.pack()
	root.mainloop()