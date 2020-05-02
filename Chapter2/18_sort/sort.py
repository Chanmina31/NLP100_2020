# coding:utf-8
with open('../popular-names.txt') as f:
    name_list = f.readlines()

sorted_list = sorted(name_list, key=lambda name: int(name.split('\t')[2]), reverse=True)

with open('sorted-names.txt', mode='w') as f:
    f.write(''.join(sorted_list))
