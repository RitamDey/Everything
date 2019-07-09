rand_str="A random string"


echo "String is $rand_str"
echo "String Length: ${#rand_str}"
echo "Character @ 3rd place: ${rand_str:2}"
echo "String's slice from position 2-7: ${rand_str:2:7}"
echo "Get everything after 'A': ${rand_str#*A }"
