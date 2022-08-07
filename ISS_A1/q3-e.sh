#!/bin/bash

filename='quotes.txt'

#printing the occurences of a word in a file
grep -o '[[:alnum:]]*' $filename | sort | uniq -c | sed -E 's/[[:space:]]*([0-9]+) (.+)/\2 : \1/'
