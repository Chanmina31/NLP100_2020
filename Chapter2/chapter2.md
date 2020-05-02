Unixコマンド

学習教材
・新しいLinuxの教科書

Linuxの取得知識
#!/bin/bash
⇨シバンという実行形式を指定できる
ex) sh,bash

10.行数のカウント
・wcコマンド
行数/単語数/バイト数/ファイル数
$ wc popular-name.txt
 2779 11120 57804 popular-name.txt

11.タブをスペースに置換
・sedコマンド
　Stream Editorの略
　置換によく使われるらしい
　ファイルからデータを読み出す（変更を施したファイルは未保存）

・trコマンド
　置換に使う
　tr <置換前の文字> <置換後の文字>
・expandコマンド
　各列のデータを並べて表示したいときに使う

19.各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
<dictionary> dictionary.items() ⇨ key,valueのペアを抽出してループ処理