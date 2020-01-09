#! /bin/python3
import sys
from fractions import gcd

BLUE, RED, WHITE, YELLOW, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[32m', '\033[0m'


sys.stdout.write(RED + """  
  

			████████╗   ██████╗ ███████╗ █████╗ 
			╚══██╔══╝   ██╔══██╗██╔════╝██╔══██╗
			   ██║█████╗██████╔╝███████╗███████║
			   ██║╚════╝██╔══██╗╚════██║██╔══██║
			   ██║      ██║  ██║███████║██║  ██║
			   ╚═╝      ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝                             		                                                                                                                                 
"""  + END + BLUE +
'' + '	     ENCRYPTION-DECRYPTION TOOL'.format(RED, END).center(69) +
'\n' + '             Developed by: {}NIRAJ'.format(YELLOW, RED, YELLOW, BLUE).center(76)+ '\n\n' + END)

print("\n------------------Enter Prime Numbers------------------\n")
round1 = True
while round1 == True:
	p1 = int(input("Enter p1: "))
	if p1 == 2:
		round1 = False
	else:
		for i in range(2,p1):
			if (p1 % i) == 0:
				sys.stdout.write(RED + "Invalid Prime Number\n" + END)
				break
			else:
				round1 = False


round2 = True
while round2 == True:
	p2 = int(input("Enter p2: "))
	if p2 == 2:
		round2 = False
	else:
		for i in range(2,p2):
			if (p2 % i) == 0:
				sys.stdout.write(RED + "Invalid Prime Number\n" + END)
				break
			else:
				round2 = False


round3 = True
while round3 == True:
	q1 = int(input("Enter q1: "))
	if q1 == 2:
		round3 = False
	else:
		for i in range(2,q1):
			if (q1 % i) == 0:
				sys.stdout.write(RED + "Invalid Prime Number\n" + END)
				break
		else:
			round3 = False


round4 = True
while round4 == True:
	q2 = int(input("Enter q2: "))
	if q2 == 2:
		round4 = False
	else:
		for i in range(2,q2):
			if (q2 % i) == 0:
				sys.stdout.write(RED + "Invalid Prime Number\n" + END)
				break
		else:
			round4 = False


round5 = True
while round5 == True:
	r1 = int(input("Enter r1: "))
	if r1 == 2:
		round5 = False
	else:
		for i in range(2,r1):
			if (r1 % i) == 0:
				sys.stdout.write(RED + "Invalid Prime Number\n" + END)
				break
		else:
			round5 = False


round6 = True
while round6 == True:
	r2 = int(input("Enter r2: "))
	if r2 == 2:
		round6 = False
	else:
		for i in range(2,r2):
			if (r2 % i) == 0:
				sys.stdout.write(RED + "Invalid Prime Number\n" + END)
				break
		else:
			round6 = False

# Calculate large number n
n1 = p1 * p2
n2 = q1 * q2
n3 = r1 * r2

# Calculate j fromo Eulers Totient Function
j1 = (p1-1) * (p2-1)
j2 = (q1-1) * (q2-1)
j3 = (r1-1) * (r2-1)

# Calculate public key
e1_list = []
for e1_i in range (1,j1):
	if gcd(e1_i,j1) == 1:
		e1_list.append(e1_i)
		
e2_list = []
for e2_i in range (1,j2):
	if gcd(e2_i,j2) == 1:
		e2_list.append(e2_i)

e3_list = []
for e3_i in range (1,j3):
	if gcd(e3_i,j3) == 1:
		e3_list.append(e3_i)

e1 = e1_list[-1]
# print('e1: ',e1)
e2 = e2_list[-1]
# print('e2: ',e2)
e3 = e3_list[-1]
# print('e3: ',e3)

# Calculate Private Key
d1_list = []
for d1_i in range(1,j1):
	if (e1 * d1_i) % j1 == 1:
		d1_list.append(d1_i)

d2_list = []
for d2_i in range(1,j2):
	if (e2 * d2_i) % j2 == 1:
		d2_list.append(d2_i)

d3_list = []
for d3_i in range(1,j3):
	if (e3 * d3_i) % j3 == 1:
		d3_list.append(d3_i)

d1 = d1_list[-1]
#print('d1: ',d1)
d2 = d2_list[-1]
#print('d2: ',d2)
d3 = d3_list[-1]
#print('d3: ',d3)

def calculation():
	while True:
		choice = input("\nEnter 'E' for encryption and 'D' for decryption and 'X' for exit: ")	

		if choice.lower() == 'e':
			m = int(input("\nEnter plain text: "))

			while True:
				c = ((((((m**e1) % n1)**e2) % n2)**e3) % n3)
				sys.stdout.write(YELLOW + "----------------------\n")
				print("Cipher text: ",c)
				sys.stdout.write(YELLOW + "----------------------\n" + END)
				order = input("Continue Encryption? (y/n): ")
				if order == 'y':
					m = int(input("\nEnter plain text: "))
				else:
					break 

		elif choice.lower() == 'd':
			c = int(input("\nEnter cipher text: "))


			while True:
				m = ((((((c**d3) % n3)**d2) % n2)**d1) % n1)
				sys.stdout.write(YELLOW + "----------------------\n")
				print("Plain text: ",m)
				sys.stdout.write(YELLOW + "----------------------\n" + END)
				order = input("Continue Decryption? (y/n): ")
				if order == 'y':
					c = int(input("\nEnter cipher text: "))
				else:
					break
		elif choice.lower() == 'x':
			sys.stdout.write(RED + "Exiting!!! \n" + END)			
			sys.exit()

		else:
			calculation()

calculation()

	
