#!/bin/bash

if [ ! -d $1 ] ;then
    echo "Potrebno je kao argument zadati ime direktorija sa log datotekama."
    exit
fi

arg=$1

files=$(ls $arg | grep -E 'localhost_access_log\.[0-9]{4}-02-[0-9]{2}.*\.txt')
for file in $files;do
    date=$(echo $file | grep -oE '[0-9]{4}-02-[0-9]{2}')
    echo "datum: $(date -d "$date" +%d-%m-%Y)"
    echo "------------------------------------------"
    cut $arg/$file -d '"' -f 2 | sort | uniq -c | sort -nr
done
