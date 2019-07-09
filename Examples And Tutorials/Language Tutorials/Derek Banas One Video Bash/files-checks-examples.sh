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

    # The -x tests if file is executable
    if [ -x "$file1" ]; then
        echo "$file1 is executable"
    fi

    # -d checks if file is directory
    if [ -d "$file1" ]; then
        echo "$file1 is a directory"
    fi

    # -L checks if file is a link
    if [ -L "$file1" ]; then
        echo "$file1 is a symbolic link"
    fi

    # -p checks if file is a named pipe
    if [ -p "$file1" ]; then
        echo "$file1 is a named pipe"
    fi

    # -S checks if file is a network socket
    if [ -S "$file1" ]; then
        echo "$file1 is a network socket"
    fi

    # -G checks if file is owned by same group
    if [ -G "$file1" ]; then
        echo "$file1 is owned by same group"
    fi

    # -O checks if file is owned by user
    if [ -O $file1 ]; then
        echo "$file1 is owned by user"
    fi
fi
