diff -s check_replacement-names.txt replacement-names.txt

# 日本語出力するとこんな感じ
if [ $? -eq 0 ]; then
    echo "中身は同じ"
elif [ $? -eq 1 ]; then
    echo "中身は異なる"
fi