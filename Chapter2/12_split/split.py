with open('../popular-names.txt') as f:
    name_list = f.readlines()

col1 = []
col2 = []
for name in name_list:
    split_column = name.split('\t')
    col1.append(split_column[0])
    col2.append(split_column[1])

with open("col1.txt", mode='w',newline='\n') as f_col1:
    f_col1.write('\n'.join(col1))
    f_col1.write('\n')
with open("col2.txt", mode='w',newline='\n') as f_col2:
    f_col2.write('\n'.join(col2))
    f_col2.write('\n')