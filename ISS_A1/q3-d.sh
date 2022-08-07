#!/bin/bash

filename='quotes.txt'

#to count the number of words per line
x=1
while read lines;
do
        count=$(wc -w <<< "$lines")
        echo "Line No:$x - Count of Words:$count"
        x=$((x+1)) #increment the line number
done < $filename
