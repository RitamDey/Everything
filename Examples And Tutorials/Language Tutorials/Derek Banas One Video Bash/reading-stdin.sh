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


# the IFS variable is used to indicate 
# the seperator that will seperate value in stdin
OIFS="$IFS"
IFS=","


read -p "Enter 2 number seperated by commas: " num1 num2


# Using paramter expansion to subsitute whitespaces.
num1=${num1//[[:blank:]]/}
num2=${num2//[[:blank:]]/}


sum=$((num1+num2))
echo "$num1 + $num2 = $sum"


IFS=$OIFS



# Parameter exapsion examples
name="sTux"
echo "${name}'s toy"


samp_string="The dog climbed the tree"
echo "${samp_string//dog/cat}"


echo "I am ${name:=sTux}
