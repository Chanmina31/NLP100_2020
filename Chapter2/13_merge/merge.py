# coding: utf-8
with open('../12_split/col1.txt') as col1:
    col1_list = col1.readlines()
with open('../12_split/col2.txt') as col2:
    col2_list = col2.readlines()

merge_list = []

for col1, col2 in zip(col1_list, col2_list):
    merge_text = col1.rstrip('\n') + '\t' + col2.rstrip('\n')
    merge_list.append(merge_text)

with open('merge.txt', mode='w', newline='\n') as f:
    f.writelines('\n'.join(merge_list))
    f.write('\n')
