# A = X = ROCK    = 1 pt
# B = Y = PAPER   = 2 pts
# C = Z = SCISSOR = 3 pts

X=$(grep X input.txt | wc -l); # play A
Y=$(grep Y input.txt | wc -l); # play B
Z=$(grep Z input.txt | wc -l); # play C

AX=$(grep "A X" input.txt | wc -l); # draw
BY=$(grep "B Y" input.txt | wc -l); # draw
CZ=$(grep "C Z" input.txt | wc -l); # draw

AY=$(grep "A Y" input.txt | wc -l); # win
BZ=$(grep "B Z" input.txt | wc -l); # win
CX=$(grep "C X" input.txt | wc -l); # win

AZ=$(grep "A Z" input.txt | wc -l); # loss
BX=$(grep "B X" input.txt | wc -l); # loss
CY=$(grep "C Y" input.txt | wc -l); # loss

echo $(($X + $Y*2 + $Z*3 + 6*($AY+$BZ+$CX) + 3*($AX+$BY+$CZ)));
