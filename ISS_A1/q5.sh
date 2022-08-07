#!/bin/bash

#q5-a
read string
len=${#string} #measure the length of string

#loop for reversing the string 
for (( i=$len-1; i>=0; i-- )); #tranvese the loop backwards
do
    ans=$ans${string:$i:1}
done

echo "$ans"

#q5-b
#to increase the ascii value of each character
var=$(echo "$ans" | tr "0-9a-zA-Z" "1-9a-zA-Z_")

#printing the final answer
echo $var

#q5-c

#loop for reversing the first half of the string
for (( i=$len/2-1; i>=0; i-- ));
do
        ans1=$ans1${string:$i:1}
done

#loop to print the second half of the string intact
for (( i=$len/2; i<=$len-1; i++ ));
do
        ans2=$ans2${string:$i:1}
done

#printing both the answers together 
echo $ans1$ans2
