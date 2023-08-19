#!/bin/bash

# bash day2-1.sh

FORWARD=$(grep forward input.txt | awk '{s+=$2} END {print s}')
DOWN=$(grep down input.txt | awk '{s+=$2} END {print s}')
UP=$(grep up input.txt | awk '{s+=$2} END {print s}')
echo "forward: ${FORWARD}"
echo "up: ${UP}"
echo "down: ${DOWN}"
DEPTH=$(($DOWN-$UP))
echo "depth: ${DEPTH}"
echo "multiplication: $(($DEPTH * $FORWARD))"
