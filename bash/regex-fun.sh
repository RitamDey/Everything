read -p "Enter a date: " date


pat="^[0-9]{2}(:?\-|\.)[0-9]{2}(:?\-|\.)[0-9]{4}"


if [[ $date =~ $pat ]]; then
    echo "$date is valid"
else
    echo "$date is invalid"
fi
