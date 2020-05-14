# -*- coding: utf-8 -*-
'''
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ip_network = (input("Введите ip-cеть: "))
ip = ip_network[:ip_network.find('/')]
ip = ip.split('.')
                                      
network_temp = '''
Network:
{0:<8} {1:<8} {2:<8} {3:<8} 
{0:08b} {1:08b} {2:08b} {3:08b}
''' 
network_temp = network_temp.format(int(ip[0]),int(ip[1]),int(ip[2]),int(ip[3]))
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
