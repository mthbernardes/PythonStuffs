#Codigo para resolver desafio, onde devia pegar paragrafo,linha e posição de uma letra em um texto, para encontrar a flag
phrase = []

def generate(text,p,l,i):
    try:
        parags = text.split('\n\n')
        linhas = parags[p-1].split('\n')
        linha = linhas
        letter = linha[l-1].replace(' ', '')[i-1]
        phrase.append(letter)
    except:
        pass
text = open('crypto50.txt').read()


lista = [3,3,2],[6,1,6],[7,2,3],[4,6,1],[2,1,3],[11,3,9],[10,1,6],[7,3,2],[5,1,1],[7,3,4],[9,3,33],[9,5,1],[10,1,2],[1,9,3]
for info in lista:
    generate(text,info[0],info[1],info[2])
    #exit()
print ''.join(phrase)
