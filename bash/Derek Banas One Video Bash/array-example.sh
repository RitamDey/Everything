# Creating an array
fav_nums=(3.14 2.718 0.57721 4.6692)


# Getting a value from array
echo "Pi: ${fav_nums[0]}"


# Adding a value
fav_nums[4]=1.618
echo "GR: ${fav_nums[4]}"

# Extending an array
fav_nums+=(1 7)


# looping over array
for i in ${fav_nums[*]}; do
    echo $i
done


# print the indexes
for i in ${fav_nums[@]}; do
    echo $i
done


# print the length
echo "Array Length: ${#fav_nums[@]}"


# Get a element
echo "Index 3 Length: ${#fav_nums[3]}"


# Sort a array
sorted_nums=( $(
                for i in "${fav_nums[@]}"
                do
                    echo "$i"
                done | sort) )


for i in ${sorted_nums[*]}; do
    echo $i
done


# delete an array element or array
unset 'sorted_nums[1]'
unset sorted_nums
