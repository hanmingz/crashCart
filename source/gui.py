import tkinter as tk
from functions import *
from guiFunctions import *

def main():
	ID = 1
	(cnx, cursor) = connectSQL()

	root = tk.Tk()
	root.geometry("480x300")
	root.title("Smart Crash Cart")

	packMenu(root)

	root.mainloop()

if(__name__ == "__main__"):
	main()