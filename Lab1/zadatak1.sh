#a
proba="Ovo je proba"

#b
echo $proba

#c
lista_datoteka=*
echo $lista_datoteka

#d
proba3="${proba}. ${proba}. ${proba}."
echo $proba3

#e
a=4
b=3
c=7
d=$(((a+4)*b%c))
echo a=$a, b=$b, c=$c, d=$d

#f
broj_rijeci=$(cat *.txt | wc -w)
echo broj rijeci=$broj_rijeci

#g
ls ~
