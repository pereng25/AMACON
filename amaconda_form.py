import telnetlib
import socket
import time
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

# root window
root = tk.Tk()
root.title("AMACONDA")
root.geometry("600x300")
root.resizable(False, False)

HOST = "141.75.28.108"
PORT = "7700"

# frame
frame = ttk.Frame(root)

# field options
options = {'padx': 5, 'pady': 5}

# Connections status label
constat_label = ttk.Label(frame, text="Welcome to AMACONDA")
constat_label.grid(column=0, row=0, sticky='W', **options)

def connection_button_clicked():
    """ Handle convert button click event """
    try:
        telcon = telnetlib.Telnet(HOST, PORT, timeout = 5)
        message = ("> ASTZ KV <").encode('ascii')
        telcon.write(message)
        time.sleep(0.05)
        output=telcon.read_eager()
        result_label.config(text = "Connected to AMA4000 with status" + output.decode("ASCII"))
    except socket.timeout: 
        result_label.config(text="Couldn't connect to AMA4000")

connect_button = ttk.Button(frame, text='Connect to AMA4000')
connect_button.grid(column=2, row=0, sticky='W', **options)
connect_button.configure(command=connection_button_clicked)

def concentration_button_clicked():
    """ Handle convert button click event """
    try:
        telcon = telnetlib.Telnet(HOST, PORT, timeout = 5)
        message = ("> AKON K0 <").encode('ascii')
        telcon.write(message)
        time.sleep(0.05)
        output=telcon.read_eager()
        result_label.config(text = "Concentrations" + output.decode("ASCII"))
    except socket.timeout: 
        result_label.config(text="Communiation error!")

conc_button = ttk.Button(frame, text='Read concentrations')
conc_button.grid(column=4, row=0, sticky='W', **options)
conc_button.configure(command=concentration_button_clicked)

# result label
result_label = ttk.Label(frame)
result_label.grid(row=1, columnspan=3, **options)

# add padding to the frame and show it
frame.grid(padx=10, pady=10)


# start the app
root.mainloop()