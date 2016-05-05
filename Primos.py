import socket, time


def primes_sieve2():
    limit = 1000
    primeList = []
    a = [True] * limit
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            primeList.append(i)
            for n in xrange(i*i, limit, i):
                a[n] = False
    return primeList

def conecta(lista_primos):
    host = '188.166.133.53'
    port = 11059
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    print s.recv(1024).strip()
    A = True
    while A is True:
            numero = s.recv(1024)
            try:
                level = numero.strip().split(":",1)[0]
                primo = int(numero.strip().split()[8].split(':')[0])
                for proximo in lista_primos:
                    if primo > proximo:
                        continue
                    elif primo == proximo:
                        continue
                    elif primo < proximo:
                        print level+' Primo:',primo,'Proximo:',proximo
                        s.send(str(proximo))
                        rcv = s.recv(19)
                        print rcv
                        break
            except:
                print numero
                A = False
primos = primes_sieve2()
conecta(primos)
