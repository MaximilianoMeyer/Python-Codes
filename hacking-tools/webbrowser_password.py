#!/usr/bin/python
#coding: utf-8

import tkinter as tk
import webbrowser

def open_website():
	website = entry.get()
	webbrowser.open(website)


def password_check():
	password = entry_password.get()
	if password == 'secret':
		label_result['text'] = "Senha correta"
		entry.config(state='normal')
		button['state'] = 'normal'
	else:
		label_result['text'] = "senha incorreta"


root = tk.Tk()
root.title("Navegador web")

label_password = tk.Label(root, text='senha')
entry_password = tk.Entry(root, show='*')

button_password = tk.Button(root, text='Verificar', command=password_check)

label = tk.Label(root, text='URL')
entry = tk.Entry(root, state='disable')

button = tk.Button(root, text='Abrir', command=open_website, state='disabled')

label_result = tk.Label(root)

label_password.pack()
entry_password.pack()
button_password.pack()
label.pack()
entry.pack()
button.pack()
label_result.pack()

root.mainloop()
