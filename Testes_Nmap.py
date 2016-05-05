import nmap,json
from pprint import pprint
host='192.168.1.0/24'
nm = nmap.PortScanner()
result = nm.scan(hosts=host,arguments='-sV -T5')
#pprint(result)

print 'Scan Statistics'
print '-' * 50
print 'Hosts Alive: ' + result['nmap']['scanstats']['uphosts']
print 'Hosts Downs: ' + result['nmap']['scanstats']['downhosts']
print 'Hosts Total: ' + result['nmap']['scanstats']['totalhosts']
print '-' * 50
scan_info = result['scan']
print '-' * 50
for ip in scan_info:
	print 'Host Informations'
	print 'IP: ' + scan_info[ip]['addresses']['ipv4']
	print 'Status: ' + scan_info[ip]['status']['state'].upper()
	print 'MAC: ' + scan_info[ip]['addresses']['mac']
	print 'Vendor: ' + scan_info[ip]['vendor'][scan_info[ip]['addresses']['mac']]
	if 'tcp' in scan_info[ip]:
		print ' '*22 + 'Ports' + ' ' * 23
		ports = scan_info[ip]['tcp']
		for port in ports:
			state = ports[port]['state']
			name = ports[port]['name']
			print str(port)+'\t'+str(state)+'\t'+str(name)
	else:
		print 'No Open Ports'
	print '-' * 50
