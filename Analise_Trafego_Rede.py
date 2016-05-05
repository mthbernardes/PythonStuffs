#!/usr/bin/env python
# coding=utf-8

import datetime, sys, dataset, logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *



#Verifica passagem de paramentros
#Verifica se foi passado o parametro com a interface
#Caso não tenha sido passado ele apresenta o erro
#Caso tenha passado ele retorna o nome da interface passada
def checa_exec():
    if len(sys.argv) < 2:
            print 'ERROR, please pass the interface as parameter'
            exit()
    else:
            return sys.argv[1]

#Função responsavel por criar o banco
#Cria a tabela access_log onde são salva todas as informações que foram logadas
#Retorna o objeto que contem a tabela
def banco():
    db = dataset.connect('sqlite:///database/full_access.db')
    packets_log = db['packets_log']
    return packets_log

#Função principal para analise dos pacotes
#Identifica se a conexão é TCP ou UDP
#Apos isso realiza o registro no banco de dados das seguintes informações
#Data atual, Source IP, Source Port, Dest IP, Dest Port, Packet Protocol, Packet Size, Packet Content

def packet_callback(packet):
    try:
        if packet[IP].proto == 6:
            modo = 'TCP'

        elif packet[IP].proto == 17:
            modo = 'UDP'

        packets_log = banco()
        agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')

        print agora,'|',str(packet[IP].src),'|',str(packet[modo].sport),'|',str(packet[IP].dst),'|',str(packet[modo].dport),'|',modo,'|',len(packet)
        packets_log.insert(dict(time=agora,src_ip=str(packet[IP].src),src_port=str(packet[modo].sport),dst_ip=str(packet[IP].dst),dst_port=str(packet[modo].dport),conn_type=modo,packet_size=len(packet),packet_content=str(packet[modo].payload)))
    except:
        pass

#Funcao principal que realiza chamada a funcao checa_exec
#Inicia o sniff de rede , chamando a funcao packet_callback
def main():
    interface = checa_exec()
    sniff(iface=interface, prn=packet_callback)

main()
