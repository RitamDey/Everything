read -p "What is your name? " name
echo "Hello $name"

read -p "What is your age? " age
if [ $age -ge 16 ]
then
    echo "You can drive"

elif [ $age -eq 15 ]
then
    echo "You can drive next year"
else
    echo "You can't drive"
fi


read -p "Enter a number: " num
if ((num == 10)); then
    echo "Your number equals 10"
fi

if ((num > 10)); then
    echo "It is greater than 10"
else
    echo "It is less then ten"
fi


if (( ((num % 2)) == 0 )); then
    echo "It is even"
else
    echo "It is odd"
fi
