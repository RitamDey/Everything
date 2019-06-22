#!/bin/bash

if [ $# -lt 4 ]; then
    echo "Usage $0 <input video> <output video> <start time> <duration>"
    exit 1
fi

# Copy all cmdline arguments
start_time="$3"
duration="$4"
input_file="$1"
output_file="$2"


# Check to see if the extensions of the input and output files match or not.
# If not, then give a proper error
# TODO: Handle conversion of formats using ffmpeg
if [ ${input_file##*.} != ${output_file##*.} ]; then
    echo "Formats don't match. Can't convert now. Sorry"
    exit 1
fi

# Check and convert starting time to hh:mm:ss format. Needed by ffmpeg
if [ `python3 -c "print(len('$start_time'.split(':')))"` -ne 3 ]; then
    while [ `python3 -c "print(len('$start_time'.split(':')))"` -lt 3 ]; do
        start_time="00:$start_time"
    done
fi

# Check and convert duration time to hh:mm:ss format.
if [ `python3 -c "print(len('$duration'.split(':')))"` -ne 3 ]; then
    while [ `python3 -c "print(len('$duration'.split(':')))"` -lt 3 ]; do
        duration="00:$duration"
    done
fi

ffmpeg -i "$input_file" -ss "$start_time" -t "$duration" -c:a copy -c:v copy "$output_file"
