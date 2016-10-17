#!/usr/bin/bash

read num1
read num2

if [ $num1 -gt $num2 ]; then
    echo "X greater then Y"
    
elif [ $num1 -lt $num2 ]; then
    echo "X smaller than Y"
else
    echo "X is equal to Y"
fi
