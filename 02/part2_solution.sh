# A = ROCK    = 1 pt
# B = PAPER   = 2 pts
# C = SCISSOR = 3 pts
# X = LOSE
# Y = DRAW
# Z = WIN

X=$(grep X input.txt | wc -l); # lose
Y=$(grep Y input.txt | wc -l); # draw
Z=$(grep Z input.txt | wc -l); # win

AX=$(grep "A X" input.txt | wc -l); # play C 
BZ=$(grep "B Z" input.txt | wc -l); # play C
CY=$(grep "C Y" input.txt | wc -l); # play C

AZ=$(grep "A Z" input.txt | wc -l); # play B
BY=$(grep "B Y" input.txt | wc -l); # play B 
CX=$(grep "C X" input.txt | wc -l); # play B

AY=$(grep "A Y" input.txt | wc -l); # play A
BX=$(grep "B X" input.txt | wc -l); # play A
CZ=$(grep "C Z" input.txt | wc -l); # play A

echo $(($Y*3 + $Z*6 + ($AY+$BX+$CZ) + 2*($AZ+$BY+$CX) + 3*($AX+$BZ+$CY)));
