# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

with open('ospf.txt') as f:
    for line in f:
        line = line.split()
        protocol = line[0]
        prefix = line[1]
        ad_metric = line[2]
        next_hop = line[4]
        last_update = line[5]
        outbound_int = line[6]
        protocol = protocol.replace('O','OSPF') 
        ad_metric = ad_metric.strip('[]')  
        next_hop = next_hop.rstrip(',')
        last_update = last_update.rstrip(',') 
        line = """
        Protocol: {0:<18} 
        Prefix: {1:<18} 
        AD/Metric: {2:<18} 
        Next-Hop: {3:<18} 
        Last-update: {4:<18} 
        Outbound Interface: {5:<18} 
        """
        print(line.format(protocol,prefix,ad_metric,next_hop,last_update,outbound_int))


