# Get the current directory name
dir=$(basename `pwd`)

# Check if the output directory exists, if not create it
if [ ! -d "$dir" ]; then
    mkdir "$dir"
fi


for f in $.c; do
    # The name of the executable if <filename>.out
    $name="$dir/#{f%.*}.out"

    echo "Compiling $f"
    gcc -o "$name" $f
done
