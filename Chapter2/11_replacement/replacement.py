# 11_replacementディレクトリで実行
with open('../popular-names.txt') as f:
    tab_name = f.read()

space_name = tab_name.replace("\t", " ")

with open('replacement-names.txt', mode="w", newline="\n") as f:
    f.write(space_name)