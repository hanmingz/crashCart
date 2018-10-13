import tkinter as tk
from functions import *

def packMenu(root):
	menu = tk.Frame(root, width = 480)
	btnUse = tk.Button(menu, text = 'USE', width = 16, command = btnuseFcn(root))
	btnUse.pack(side = tk.LEFT)
	btnList = tk.Button(menu, text = 'LIST', width = 16, command = btnListFcn(root))
	btnList.pack(side = tk.LEFT)
	btnMaintain = tk.Button(menu, text = 'MAINTENANCE', width = 16, command = btnMaintainFcn(root))
	btnMaintain.pack(side = tk.LEFT)
	menu.pack()

def btnuseFcn(root):
	pass

def btnListFcn(root):
	pass

def btnMaintainFcn(root):
	pass

def packKeypad(root, frm_keypad):
	count = 0

	def incr_count(num, label):
	    global count
	    count = count * 10 + num
	    label.config(text = str(count))

	def delete_last():
	    global count
	    count = count // 10
	    label.config(text = str(count))

	def return_count():
	    # TODO: return input
	    global count
	    count = 0
	    label.config(text = str(count))

	# create label
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

