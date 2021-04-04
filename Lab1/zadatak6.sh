#!/bin/bash

if [ ! -d $1 ] || [ ! -d $2 ] ;then
    echo "Kao argumente treba unijeti dva postojeca direktorija."
    exit
fi

arg1=$1
arg2=$2

for file in $(ls $arg1)
    do
    file2=$(find "$arg2" -name "$file")
    found=$(find "$arg2" -name "$file" | wc -l)
    if [[ $found -eq 0 || $arg1/$file -nt $file2 ]]; then
        echo "$arg1/$file --> $arg2"
    fi
done

for file in $(ls $arg2)
    do
    file2=$(find "$arg1" -name "$file")
    found=$(find "$arg1" -name "$file" | wc -l)
    if [[ $found -eq 0 || $arg2/$file -nt $file2 ]]; then
        echo "$arg2/$file --> $arg1"
    fi
done
