echo "1st Argument: $1"


sum=0


# $# gets the total number arguments
while [[ $# -gt 0 ]]; do
    num=$1
    sum=$(( sum+num ))
    
    # the shift command shifts each argument one place to the left
    shift
done

echo $sum
