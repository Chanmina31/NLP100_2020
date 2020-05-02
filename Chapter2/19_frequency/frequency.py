# coding:utf-8
import collections

with open('../popular-names.txt') as f:
    names_list = f.readlines()

l = []
for name in names_list:
    l.append(name.split('\t')[0])

counter = collections.Counter(l)
dict_counter = dict(counter)
for k,v in sorted(dict_counter.items(), key=lambda x: -x[1]):
    print(str(k) + ":" + str(v))