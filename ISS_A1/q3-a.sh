#!/bin/bash

filename='quotes.txt'

#to find the size of the file in bytes
size=$(find quotes.txt -printf "%s")

#printing the size of the file in bytes
printf "Size of given file = %d bytes\n" $size

