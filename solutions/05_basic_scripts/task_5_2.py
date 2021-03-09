# -*- coding: utf-8 -*-
"""
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

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

network = input("Введите адрес сети в формате 10.1.1.10/24: ")
new_ip = network.split('/')
new_ip_network = new_ip[0].split('.')
prefix = network.split('.')
bin_mask = "1" * int(new_ip[1]) + "0" * (32-int(new_ip[1]))

out = """
Network:
{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}
"""

out_mask = """
Mask
{0}
{1:<10}{2:<10}{3:<10}{4:<10}
{1:8b}  {2:08b}  {3:08b}  {4:08b}
"""
print(out.format(int(new_ip_network[0]),int(new_ip_network[1]),int(new_ip_network[2]),int(new_ip_network[3])))
print(out_mask.format(prefix[-1].strip('1'), int(bin_mask[0:8],2), int(bin_mask[8:16],2), int(bin_mask[16:24],2), int(bin_mask[24:],2)))
