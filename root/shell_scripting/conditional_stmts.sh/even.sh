#! /bin/bash
# Using if-else to check whether a number is even


read 'enter num'
if [ $((n%2))==0 ]
then
	echo "num is even"
else
	echo "num is odd"
fi
