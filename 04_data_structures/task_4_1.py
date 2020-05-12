# -*- coding: utf-8 -*-
'''
Задание 4.1

Обработать строку nat таким образом,
чтобы в имени интерфейса вместо FastEthernet было GigabitEthernet.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

<<<<<<< HEAD
nat = 'ip nat inside source list ACL interface FastEthernet0/1 overload'
=======
nat = 'ip nat inside source list ACL interface FastEthernet0/1 overload
>>>>>>> 0c76a200918a900b2d85a574a0d0aca2a0d76b63
nat = nat.replace('FastEthernet', 'GigabitEthernet')
print(nat)

