#!/bin/bash

#Q1-a
filename='quotes.txt'
#sed -i removes the empty lines in a file
#output is generated in the same file quotes.txt
sed -i '/^$/d' $filename
cat $filename

#Q1-b

filenamenew='new.txt'

#sort the files first then uniq -i removes the duplicate lines
#output is generated in a newfile
sort $filename | uniq -i > $filenamenew

