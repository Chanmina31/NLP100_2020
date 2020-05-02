# coding:utf-8
n = int(input('出力したい行数を数字で入力してください=>'))

with open('../popular-names.txt') as f:
    for i, line in enumerate(f):
        if(i>=n):
            break
        print(line.rstrip('\n'))