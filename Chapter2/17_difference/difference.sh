#!/bin/bash
cut -f 1 -d ' ' ../11_replacement/replacement-names.txt | sort | uniq  > check_name_list.txt