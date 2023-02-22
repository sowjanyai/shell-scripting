#! /bin/bash
# program to read two integer numbers and print the substraction of both numbers

echo "Enter num1: "
read num1
echo "Enter num2: "
read num2
result=`expr $num1 - $num2`

echo "Subtraction is: $result"
