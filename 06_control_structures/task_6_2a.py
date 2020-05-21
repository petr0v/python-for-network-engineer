# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ip = input("Введите IP-адрес: ")
dot = ip.count('.')

if dot !=3:
    print('Неправильный IP-адрес')
else:
    ip = ip.split('.')
    if ip[0].isdigit() is not True and ip[1].isdigit()is not True and ip[2].isdigit() is not True and ip[3].isdigit() is not True:
        print('Неправильный IP-адрес')
    else:
        oktet1 = int(ip[0])
        oktet2 = int(ip[1])
        oktet3 = int(ip[2])
        oktet4 = int(ip[3])
        array_list = list(range(0,256))
        if oktet1 not in array_list or oktet2 not in array_list or oktet3 not in array_list or  oktet4 not in array_list:
            print('Неправильный IP-адрес')
        else:
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
                


