#! /bin/bash

# greatest among 4 number

read -p "Enter the value of A: " a
read -p "Enter the value of B: " b
read -p "Enter the value of C: " c
read -p "Enter the value of D: " d
if [ $a -gt $b -a $a -gt $c -a $a -gt $d ];
then
	echo "Print $a is greatest number"
elif [ $b -gt $c -a $b -gt $d ];
then
	echo "Print $b is greatest number"
elif [ $c -gt $d ];
then
	echo "Print $c is greatest number"
else
	echo "print $d is greatest number"
fi
