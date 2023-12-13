#!/bin/bash

prefix="split" # File name prefix for split files
count=1
maxsize=$((50 * 1024 * 1024)) # 50 MB in bytes
currentsize=0

# Read the header line
head -1 large_file.csv > header.csv

# Skip the header in the large file and start processing
tail -n +2 large_file.csv | while IFS= read -r line
do
    # If the current file size is less than 50MB, write to the file
    if [ $currentsize -le $maxsize ]; then
        echo "$line" >> "${prefix}_${count}.csv"
        currentsize=$(($(stat -f%z "${prefix}_${count}.csv") + ${#line}))
    else
        # Start a new file
        ((count++))
        echo "$line" > "${prefix}_${count}.csv"
        currentsize=$(stat -f%z "${prefix}_${count}.csv")
    fi
done

# Add the header to each split file
for file in ${prefix}_*.csv
do
    cat header.csv "$file" > temp && mv temp "$file"
done

rm header.csv
#aws s3 cp /path/to/split_files s3://your-bucket-name --recursive
