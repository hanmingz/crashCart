import tkinter as tk
from functions import *

def menuPack(root):
	menu = tk.Frame(root, width = 480)
	btnUse = tk.Button(menu, text = 'USE', width = 16)
	btnUse.pack(side = tk.LEFT)
	btnList = tk.Button(menu, text = 'LIST', width = 16)
	btnList.pack(side = tk.LEFT)
	btnMaintain = tk.Button(menu, text = 'MAINTANANCE', width = 16)
	btnMaintain.pack(side = tk.LEFT)
	menu.pack()