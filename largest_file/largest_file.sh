#!/bin/bash

echo "Enter the exact path of folder whose contents you want to analyze, 0 to exit"
read path

if [ "$path" == "0" ]; then
	exit 1
else
	find "$path" -type f -printf '%s %p\n' | sort -nr | head -n 1 |
	{
	        read -r sz nm
	        printf "Maximum file size: %d B\nFile Name : %s\n" "$sz" "$nm"
        }
fi
