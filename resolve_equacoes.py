#A numbers game
#(code50, solved by 154)
#Description: People either love or hate math. Do you love it? Prove it! You just need to solve a bunch of equations without a mistake.
#Service: 188.166.133.53:11027

import socket, time
host = '188.166.133.53'
port = 11071
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
s.recv(4096)


while True:
	conta = s.recv(4096)
	print conta
	conta = conta.strip().split()
	val1 = int(conta[6])
	val2 = int(conta[4])
	simbol = conta[3]
	if simbol == '+':
		result = val1 - val2
	elif simbol == '*':
		result = val1 / val2
	elif simbol == '-':
		result = val1 + val2
	elif simbol == '/':
		result = val1 * val2
	print result
	s.send(str(result))
	#time.sleep(1)
	print s.recv(4096).strip()
