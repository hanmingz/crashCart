import tkinter as tk
import RPi.GPIO as GPIO
from functions import *

# Global variables
count = 0
msg = "msg"

def runGui():

	#functions definitions
	def closeWindow(cnx, cursor):
		disconnectSQL(cnx, cursor)
		root.destroy()

	def btnUseFcn():
		medList.pack_forget()
		frm_keypad.pack_forget()
		use.pack_forget()
		txtUse.delete(1.0, tk.END)
		global msg
		txtUse.insert(tk.END, msg)
		thisMac = getMac()
		cartStatus(cnx, cursor, ID, 1, thisMac)
		use.pack()

	def btnListFcn():
		use.pack_forget()
		lbxList.delete(0, tk.END)
		thisrow = '{:15s}  {:12s}  {:15s}'.format('MEDICINE', 'QUANTITY', 'EXPIRATION')
		lbxList.insert(tk.END, thisrow)
		getAllMedicine(cnx, cursor, ID)
		for(medicine, quantity, expiration) in cursor:
			thisrow = '{:15s}  {:12d}  {:15s}'.format(medicine.ljust(15)[:15], quantity, str(expiration))
			lbxList.insert(tk.END, thisrow)

		frm_keypad.pack_forget()
		medList.pack()

	def btnMaintainFcn():
		frm_keypad.pack()
		medList.pack_forget()
		use.pack_forget()
		thisMac = getMac()
		cartStatus(cnx, cursor, ID, 0, thisMac)

	def incr_count(num, label):
	    global count
	    count = count * 10 + num
	    label.config(text = str(count))

	def delete_last():
	    global count
	    count = count // 10
	    label.config(text = str(count))

	def return_count():
		global count
		barcode = e_bar.get()
		name = findName(cnx, cursor, barcode)
		updateMedicine(cnx, cursor, name, count, "2018-12-12", ID)
		e_bar.delete(0, tk.END)
		txtMedicine.delete(1.0, tk.END)
		count = 0
		label.config(text = str(count))

	def barcodeEnter(event):
		try:
			name = findName(cnx, cursor, e_bar.get())
			txtMedicine.delete(1.0, tk.END)
			txtMedicine.insert(tk.END, name)
		except:
			pass

	def display_ls1(channel):
		global msg
		msg = "Roxithromycin"

	def display_ls2(channel):
		global msg
		msg = "Band Aid"

	def display_ls3(channel):
		global msg
		msg = "Medication 3"

	# GUI
	ID = 1
	global cnx
	global cursor
	(cnx, cursor) = connectSQL()
	initCart(cnx, cursor, ID)

	root = tk.Tk()
	root.protocol("WM_DELETE_WINDOW", lambda: closeWindow(cnx, cursor))
	root.geometry("480x300")
	root.title("Smart Crash Cart")
	root.bind('<Return>', barcodeEnter)

	# Menu bar
	menu = tk.Frame(root, width = 480, height = 60)
	btnUse = tk.Button(menu, text = 'USE', width = 16, command = btnUseFcn)
	btnUse.pack(side = tk.LEFT)
	btnList = tk.Button(menu, text = 'LIST', width = 16, command = btnListFcn)
	btnList.pack(side = tk.LEFT)
	btnMaintain = tk.Button(menu, text = 'MAINTENANCE', width = 16, command = btnMaintainFcn)
	btnMaintain.pack(side = tk.LEFT)

	# Keypad Frame
	frm_keypad = tk.Frame(root, width = 480, height = 240)
	frm_keypad.pack()
	label = tk.Label(frm_keypad, fg="green")
	label.grid(row=0, columnspan=3)

	# create buttons
	btn0 = tk.Button(frm_keypad, text='0', width=10, command=lambda: incr_count(0, label))
	btn0.grid(row=4, column=1)

	btn1 = tk.Button(frm_keypad, text='1', width=10, command=lambda: incr_count(1, label))
	btn1.grid(row=3, column=0)

	btn2 = tk.Button(frm_keypad, text='2', width=10, command=lambda: incr_count(2, label))
	btn2.grid(row=3, column=1)

	btn3 = tk.Button(frm_keypad, text='3', width=10, command=lambda: incr_count(3, label))
	btn3.grid(row=3, column=2)

	btn4 = tk.Button(frm_keypad, text='4', width=10, command=lambda: incr_count(4, label))
	btn4.grid(row=2, column=0)

	btn5 = tk.Button(frm_keypad, text='5', width=10, command=lambda: incr_count(5, label))
	btn5.grid(row=2, column=1)

	btn6 = tk.Button(frm_keypad, text='6', width=10, command=lambda: incr_count(6, label))
	btn6.grid(row=2, column=2)

	btn7 = tk.Button(frm_keypad, text='7', width=10, command=lambda: incr_count(7, label))
	btn7.grid(row=1, column=0)

	btn8 = tk.Button(frm_keypad, text='8', width=10, command=lambda: incr_count(8, label))
	btn8.grid(row=1, column=1)

	btn9 = tk.Button(frm_keypad, text='9', width=10, command=lambda: incr_count(9, label))
	btn9.grid(row=1, column=2)

	btn_enter = tk.Button(frm_keypad, text='Enter', width=10, command=return_count)
	btn_enter.grid(row=4, column=2)

	btn_del = tk.Button(frm_keypad, text='Delete', width=10, command=delete_last)
	btn_del.grid(row=4, column=0)

	# create Entry
	tk.Label(frm_keypad, text="Medicine: ").grid(row=5, column=0)
	e_bar = tk.Entry(frm_keypad)
	e_bar.grid(row=5, column=1, columnspan=2)
	txtMedicine = tk.Text(frm_keypad, width = 20, height = 1)
	txtMedicine.grid(row=6, column = 1, columnspan = 2)
	frm_keypad.pack_forget()

	# List
	medList = tk.Frame(root, width = 480, height = 260)
	lbxList = tk.Listbox(medList, width = 480, height = 260, font = ("Courier", 12))
	lbxList.pack()

	#use
	use = tk.Frame(root, width = 480, height = 260)
	txtUse = tk.Text(use, width = 480, height = 260, font = ("Courier", 16))
	txtUse.pack()

	# GPIO from light sensor
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.add_event_detect(36, GPIO.RISING)
	GPIO.add_event_callback(36, display_ls1)
	GPIO.add_event_detect(38, GPIO.RISING)
	GPIO.add_event_callback(38, display_ls2)
	GPIO.add_event_detect(40, GPIO.RISING)
	GPIO.add_event_callback(40, display_ls3)
	# running
	menu.pack()
	root.mainloop()
