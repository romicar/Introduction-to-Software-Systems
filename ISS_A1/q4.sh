#!/bin/bash
#Sorting the array using Bubble sort

# Given Array:
arr=(21 22 34 1 7 90 101 2 4 8 45)

# Performing Bubble sort 
for ((i = 0; i<11; i++))
do
    
    for((j = 0; j<11-i-1; j++))
    do
    
        if [ ${arr[j]} -gt ${arr[$((j+1))]} ]
        then
            temp=${arr[j]} #temp variable to swap the elements
            arr[$j]=${arr[$((j+1))]}  
            arr[$((j+1))]=$temp
        fi
    done
done

#printing the sorted array
echo ${arr[*]}
