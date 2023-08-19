sed 's/-/,/g' ./input.txt | awk -F, '{
    if (($1 >= $3 && $2 <= $4) || ($1 <= $3 && $2 >= $4))
        print $1,$2,$3,$4, "PITOCO"
    else
        print $1,$2,$3,$4
}' | grep PITOCO | wc -l