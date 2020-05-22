# -*- coding: utf-8 -*-
'''
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
ip = input("Введите IP-адрес: ") 
error_ip = False

while not error_ip:
    if ip.count('.') !=3:
        print('Неправильный IP-адрес')
    elif ip.split('.')[0].isdigit() is False or ip.split('.')[1].isdigit()is False or ip.split('.')[2].isdigit() is False or ip.split('.')[3].isdigit() is False:
        print('Неправильный IP-адрес')
    elif int(ip.split('.')[0]) not in list(range(0,256)) or int(ip.split('.')[1]) not in list(range(0,256)) or int(ip.split('.')[2]) not in list(range(0,256)) or int(ip.split('.')[3]) not in list(range(0,256)):
            print('Неправильный IP-адрес')
    else:
        ip = ip.split('.')
        oktet1 = int(ip[0])
        oktet2 = int(ip[1])
        oktet3 = int(ip[2])
        oktet4 = int(ip[3])
        if 1<=oktet1<=223:
            print('unicast')
        elif 224<=oktet1<=239:
            print('multicast')
        elif oktet1 == 255 and oktet2 == 255 and oktet3 == 255 and oktet4 == 255:
            print('local broadcast')
        elif oktet1 == 0 and oktet2 == 0 and oktet3 == 0 and oktet4 == 0:
            print('unassigned')
        else:
            print('unused')
        error_ip = True
        continue 
    ip = input('Введите Ip-адрес ещё раз: ')
    
    
    
    
    
     
    
    
