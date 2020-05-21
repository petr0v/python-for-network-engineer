# -*- coding: utf-8 -*-
'''
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ip = input("Введите IP-адрес: ")

ip = ip.split('.')
oktet1 = int(ip[0])
oktet2 = int(ip[1])
oktet3 = int(ip[2])
oktet4 = int(ip[3])

if  1<=oktet1<=223:
    print('unicast')
elif 224<=oktet1<=239:
    print('multicast')
elif oktet1 == 255 and oktet2 == 255 and oktet3 == 255 and oktet4 == 255:
    print('local broadcast')
elif oktet1 == 0 and oktet2 == 0 and oktet3 == 0 and oktet4 == 0:
    print('unassigned')
else:
    print('unused')
