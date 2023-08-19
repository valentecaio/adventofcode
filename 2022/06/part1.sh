a=0; b=0; c=0; d=0; i=0;
echo "a - b - c - d - e - i"
echo "---------------------"
while read -n1 e; do
    ((i++));
    a=$b; b=$c; c=$d; d=$e;
    echo "$a - $b - $c - $d - $e - $i"
    if [ $i -lt 4 ]; then continue; fi;
    if [ $a != $b ] && [ $a != $c ] && [ $a != $d ] && [ $b != $c ] && [ $b != $d ] && [ $c != $d ]; then break; fi;
done < input.txt
echo "i = $i"
