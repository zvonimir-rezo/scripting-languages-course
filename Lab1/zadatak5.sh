#!/bin/bash

if [[ ! -f $1 ]] ;then
    echo "Potrebno je kao argument zadati ime filea sa korisnicima."
    exit
fi

IFS=':'
while read -r row; do
    br=0
    for i in $row;do      

        if [ $br -eq 0 ];then
            #zad=$(echo ${i##*/} | cut -c 1-2)
            zad=$(echo $i | cut -c 1-2)
        fi

        if [ $br -eq 4 ];then
            tmp=$(echo $i | sed 's/-.//')
            initials=$(echo "${tmp//[a-z]/}" | sed 's/ //g')
            if [ $zad != ${initials,,} ];then
                echo $row
            fi
        fi
        br=$((br + 1))
    done
done < $1