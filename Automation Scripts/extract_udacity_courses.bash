#!/usr/bin/env bash


ZIP_PATH=$1
EXTRACT_PATH=$2


get_name() {
    local file_name=$1
    echo "$file_name"
    return $(basename "file_name" .zip)
}


if [ -e "$EXTRACT_PATH" ] && [ -d "$EXTRACT_PATH" ]
then
    echo "$EXTRACT_PATH exists"
else
    echo "Creating $EXTRACT_PATH"
    mkdir "$EXTRACT_PATH"
fi


for file in "$ZIP_PATH"/*
do
    unzip -d "$EXTRACT_PATH$(basename "$file" .zip)" "$file"
done

