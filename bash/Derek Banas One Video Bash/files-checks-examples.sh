file1="./test_file1"
file2="./test_file2"

# The -e tests if file is exists
if [ -e "$file1" ]; then
    echo "$file1 exists"
    
    # The -f tests if file is normal
    if [ -f "$file1" ]; then
        echo "$file1 is a normal file"
    fi

    # The -r tests if file is readable
    if [ -r "$file1" ]; then
        echo "$file1 is readable"
    fi

    # The -w tests if file is writable
    if [ -w "$file1" ]; then
        echo "$file1 is writable"
    fi
else
    echo "$file1 doesn't exists"
fi
