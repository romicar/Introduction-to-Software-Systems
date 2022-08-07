#!/bin/bash

filename='quotes.txt'

#printing the number of lines in a file using wc -l command
printf "Number of lines = %d \n" $(wc -l < $filename)

