#!/bin/bash
echo -n "ファイルを何分割にしたいか入力してください=>"
read num
split -n $num -d ../popular-names.txt div_files/bash