# coding:utf-8
num = int(input("いくつに分割しますか？=>"))

with open('../popular-names.txt') as f:
    names_list = f.readlines()

lines = len(names_list)
unit = int(lines/num)

for i, offset in enumerate(range(0,lines,unit),1):
    file_name = '{:03d}.txt'.format(i)
    with open('div_files/{}'.format(file_name),mode='w') as f:
        f.writelines(names_list[offset:offset+unit])