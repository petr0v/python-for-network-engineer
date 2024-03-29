# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску,
как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.195/28 - хост из сети 10.0.5.192/28

Если пользователь ввел адрес 10.0.1.1/24, вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях хост/маска, например:
    10.0.5.195/28, 10.0.1.1/24

Подсказка:
Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит
адреса хоста + 4 ноля.
То есть, например, адрес хоста 10.1.1.195/28 в двоичном формате будет
bin_ip = "00001010000000010000000111000011"

А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего
в адресе может быть 32 бита, а 32 - 28 = 4)
00001010000000010000000111000000

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

network = input("Введите адрес сети в формате 10.1.1.10/24: ")
new_ip = network.split('/')
new_ip_network = new_ip[0].split('.')
bin_mask = "1" * int(new_ip[1]) + "0" * (32-int(new_ip[1]))
null_mask = "0" * (32-int(new_ip[1]))
bin_ip_str = "{:08b}{:08b}{:08b}{:08b}".format(int(new_ip_network[0]),int(new_ip_network[1]),int(new_ip_network[2]),int(new_ip_network[3]))
bin_network = bin_ip_str[:int(new_ip[1])] + null_mask
net_oct1,net_oct2,net_oct3,net_oct4 = int(bin_network[0:8],2),int(bin_network[8:16],2),int(bin_network[16:24],2),int(bin_network[24:],2)

out = """
Network:
{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}
"""

out_mask = """
Mask
/{0}
{1:<10}{2:<10}{3:<10}{4:<10}
{1:8b}  {2:08b}  {3:08b}  {4:08b}
"""
print(out.format(net_oct1,net_oct2,net_oct3,net_oct4))
print(out_mask.format(new_ip[1], int(bin_mask[0:8],2), int(bin_mask[8:16],2), int(bin_mask[16:24],2), int(bin_mask[24:],2)))
