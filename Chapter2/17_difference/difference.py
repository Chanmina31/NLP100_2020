with open('../popular-names.txt') as f:
    name_list = f.readlines()

l = []
for name in name_list:
    l.append(name.split('\t')[0])

name_type = list(set(l))
name_type.sort()

with open('name_list.txt', mode='w', newline='\n') as f:
    f.write('\n'.join(name_type))
    f.write('\n')