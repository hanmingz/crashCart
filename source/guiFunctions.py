import tkinter as tk
from functions import *

def packMenu(root):
	menu = tk.Frame(root, width = 480)
	btnUse = tk.Button(menu, text = 'USE', width = 16, command = btnuseFcn(root))
	btnUse.pack(side = tk.LEFT)
	btnList = tk.Button(menu, text = 'LIST', width = 16, command = btnListFcn(root))
	btnList.pack(side = tk.LEFT)
	btnMaintain = tk.Button(menu, text = 'MAINTANANCE', width = 16, command = btnMaintainFcn(root))
	btnMaintain.pack(side = tk.LEFT)
	menu.pack()

def btnuseFcn(root):
	pass

def btnListFcn(root):
	pass

def btnMaintainFcn(root):
	pass