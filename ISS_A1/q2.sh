#!/bin/bash

filename='quotes.txt'
outputfile='speech.txt'

#remove the empty lines first using sed -i command
sed -i '/^$/d' $filename

#synatx for [author] once said, “[quote]”
#output is generated in a new file named speech.txt
awk -F"~" '{ print $2 " once said,\""$1"\"" }' $filename > $outputfile



