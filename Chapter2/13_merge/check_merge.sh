#!/bin/bash
diff -s merge.txt check_merge.txt
if [ $? -eq 0 ]; then
    echo "中身は同じ"
elif [ $? -eq 1 ]; then
    echo "中身は異なる"
fi
