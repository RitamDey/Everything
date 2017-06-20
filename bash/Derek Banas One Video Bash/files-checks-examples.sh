file1="./test_file1"
file2="./test_file2"


if [ -e "$file1" ]; then
    echo "$file1 exists"

    if [ -f "$file1" ]; then
        echo "$file1 is a normal file"
    fi
fi


