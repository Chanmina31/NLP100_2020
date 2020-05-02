#!/bin/bash
diff -s check_col1.txt col1.txt
if [ $? -eq 0 ]; then
    echo "col1の中身は同じ"
elif [ $? -eq 1 ]; then
    echo "col1の中身は異なる"
fi

diff -s check_col2.txt col2.txt
if [ $? -eq 0 ]; then
    echo "col2の中身は同じ"
elif [ $? -eq 1 ]; then
    echo "col2の中身は異なる"
fi