import tkinter as tk
from functions import *

root = tk.Tk()
root.geometry("480x300")
root.title("Smart Crash Cart")

menu = tk.Frame(root, width = 480)

btnUse = tk.Button(menu, text = 'USE', width = 16)
btnUse.pack(side = tk.LEFT)
btnList = tk.Button(menu, text = 'LIST', width = 16)
btnList.pack(side = tk.LEFT)
btnMaintain = tk.Button(menu, text = 'MAINTANANCE', width = 16)
btnMaintain.pack(side = tk.LEFT)

menu.pack()

def main():
	root.mainloop()

if(__name__ == "__main__"):
	ID = 1
	(cnx, cursor) = connectSQL()
	main()