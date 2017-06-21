# The -p switch is for the prompt to be displayed
read -p "Enter 2 Numbers to Sum: " num1 num2


sum=$((num1+num2))
echo "$num1 + $num2 = $sum"


# Enter info without echoing back
read -sp "Enter the secret code " secret


if [ $secret == "password" ]; then
    echo "Enter"
else
    echo "Wrong Password"
fi
