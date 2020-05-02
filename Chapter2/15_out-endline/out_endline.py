# coding:utf-8
n = int(input('出力したい行数を数字で入力してください=>'))

with open('../popular-names.txt') as f:
    read_lines = f.readlines()

for line in read_lines[-n:]:
    print(line.rstrip('\n'))