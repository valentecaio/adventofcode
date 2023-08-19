sed 's/-/,/g' ./input.txt | awk -F, '{
    if ($2 < $3 || $4 < $1)
        print $1,$2,$3,$4
    else
        print $1,$2,$3,$4, "PITOCO"
}' | grep PITOCO | wc -l