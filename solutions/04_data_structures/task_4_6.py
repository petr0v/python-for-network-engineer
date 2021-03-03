# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

new_ospf_route = """
{:22} {prefix}
{:22} {ad_metric} 
{:22} {next_hop}
{:22} {last_update}
{:22} {out_int}
"""

ospf_route = new_ospf_route.format('Prefix','AD/metric','Next-hop','Last update','Outbound Interface',prefix = ospf_route.split()[0], ad_metric = ospf_route.split()[1].strip('[]') , last_update = ospf_route.split()[-2].rstrip(','), next_hop = ospf_route.split()[3].rstrip(','), out_int = ospf_route.split()[-1])
print(ospf_route)
    

