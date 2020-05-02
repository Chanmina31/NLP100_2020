#!/bin/bash
# -nで改行しない
echo -n "出力したい行数を数字で入力してください=>"
# 入力を受付、それを変数に代入
read lines
tail -n $lines ../popular-names.txt