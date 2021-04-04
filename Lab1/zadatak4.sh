#!/bin/bash

if [[ ! -d $1 ]] ;then
    echo "Potrebno je kao argument zadati ime direktorija sa slikama."
    exit
fi

arg=$1
sortirani=$(ls $arg | sort)
set -- $sortirani
trenutni=""
brojac=1
for file in $sortirani
    do
    if [[ $(echo $file | cut -b 1-6) -ne $(echo $trenutni | cut -b 1-6) ]]; then

        if [[ $brojac -gt 1 ]]; then
            echo "--- Ukupno: $((brojac-1)) slika -----"
        fi
        echo
        brojac=1
        trenutni=$(echo $file | cut -b 1-6)
        echo "$(echo $trenutni | cut -b 5-6)-$(echo $trenutni | cut -b 1-4) :"
        echo "----------"
    fi
    echo "${brojac}. ${file}"
    brojac=$((brojac+1))
done
echo "--- Ukupno: $((brojac-1)) slika -----"
