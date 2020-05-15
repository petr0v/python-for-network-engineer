# -*- coding: utf-8 -*-

'''
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from sys import argv

ip_network = argv[1:]
ip_network = ''.join(ip_network)
ip = ip_network[:ip_network.find('/')]
ip = ip.split('.')

network_temp = '''
Network:
{0:<8} {1:<8} {2:<8} {3:<8} 
{0:08b} {1:08b} {2:08b} {3:08b}
''' 
network_temp = network_temp.format(int(ip[0]),int(ip[1]),int(ip[2]),0 * int(ip[3]))
print(network_temp)


mask = ip_network[ip_network.find('/')::]
mask1 = mask.lstrip('/')
maskint = int(mask1)
maskbit = '1' * maskint
maskbit = "{:<032}".format(maskbit)

mask_temp = '''
Mask:
{4:<}
{0:<8} {1:<8} {2:<8} {3:<8} 
{0:08b} {1:08b} {2:08b} {3:08b}
'''
mask_temp = mask_temp.format(int(maskbit[0:8],2),int(maskbit[8:16],2),int(maskbit[16:24],2),int(maskbit[24:32],2),mask)
print(mask_temp)

