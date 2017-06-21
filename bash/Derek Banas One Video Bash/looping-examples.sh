num=1


while [ $num -le 10 ]; do
    echo $num
    num=$((num+1))
done


num=1
while [ $num -le 20 ]; do
    if (( ((num%2)) == 0 )); then
        num=$((num+1))
        continue
    fi

    if ((num>=15)); then
        break
    fi

    echo $num
    num=$((num+1))
done


num=1
until [ $num -gt 10 ]; do
    echo $num
    num=$((num+1))
done



#creating the file for next example
if [ -e "file.txt" ]; then
    rm file.txt
fi
echo ".298  1996  762" >> file.txt

# iterating over contains of a file
while read avg rbis hrs; do
    printf "Avg: ${avg}\nRBIs: ${rbis}\nHRs: ${hrs}\n"
done < file.txt



for (( i=0; i <= 10; i=i+1 )); do
    echo $i
done


for i in {A..Z}; do
    echo $i
done


# Be responsible delete the file
rm file.txt
