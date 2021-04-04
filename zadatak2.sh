#a
linije=$(grep -i 'banana\|jabuka\|jagoda\|dinja\|lubenica' namirnice.txt)
echo $linije

#b
linije=$(grep -i -v 'banana\|jabuka\|jagoda\|dinja\|lubenica' namirnice.txt)
echo $linije

#c
linije=$(grep -r '[A-Z][A-Z][A-Z][100000-999999]' ~/projekti/)
echo $linije

#d
find . -mtime +7 -mtime -14 -ls

#e
for i in {1..15};
do echo $i;
done

#f
kraj=15
# for i in {1..$kraj};
# do echo $i;
# done
seq 1 $kraj
