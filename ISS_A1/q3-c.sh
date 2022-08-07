#!/bin/bash

filename='quotes.txt'

#printing the number of words in a file using wc -w command
printf "Number of words = %d \n" $(wc -w < $filename)


