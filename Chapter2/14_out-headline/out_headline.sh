#!/bin/bash
# -nで改行しない
echo -n "出力したい行数を数字で入力してください=>"
read lines
head -n $lines ../popular-names.txt