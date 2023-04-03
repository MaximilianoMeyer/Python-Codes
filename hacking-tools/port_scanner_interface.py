#!/usr/bin/python
#coding: utf-8

import socket
from tkinter import *

def scan_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        con = s.connect((host, port))
        return True
    except:
        return False
    finally:
        s.close()

def scan_host(host):
    open_ports = []
    for port in range(1, 100):
        if scan_port(host, port):
            open_ports.append(port)
    return open_ports

def display_result(host, open_ports):
    result = "Host: " + host + "\n"
    result += "Open ports:\n"
    for port in open_ports:
        result += str(port) + "\n"
    result_text.delete(1.0, END)
    result_text.insert(INSERT, result)

def start_scan():
    host = host_entry.get()
    open_ports = scan_host(host)
    display_result(host, open_ports)

root = Tk()
root.title("Port Scanner")

host_label = Label(root, text="Host/IP:")
host_label.grid(row=0, column=0, sticky="W")

host_entry = Entry(root)
host_entry.grid(row=0, column=1)

scan_button = Button(root, text="Scan", command=start_scan)
scan_button.grid(row=1, column=0, columnspan=2, pady=10, padx=10, ipadx=50)

result_label = Label(root, text="Result:")
result_label.grid(row=2, column=0, sticky="W", pady=10)

result_text = Text(root, height=15, width=50)
result_text.grid(row=3, column=0, columnspan=2)

root.mainloop()
