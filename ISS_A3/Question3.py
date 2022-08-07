"""
Created on Sat May 15 01:43:37 2022
@author: romica
"""
stringlist = []
for i in range(0,10,1):
    string = input("Enter a word: ")
    stringlist.append(string)
    
stringlist.sort()

choice = str(input("Choose between ascending or descending: "))

             
if choice == 'ascending':
    for j in range(0, 10,1):
        print(stringlist[j])
         
elif choice == 'descending':
    stringlist.reverse() 
    for j in range(0, 10,1):
        print(stringlist[j])
         
else:
 print('Error:Choice can be either ascending or descending\n')
 
string2 = input("Enter another string: ")
stringlist.append(string2)

stringlist.sort()

if choice == 'ascending':
    for j in range(0, 11 ,1):
        print(stringlist[j])
elif choice == 'descending':
    for j in range(0, 11 ,1):
        print(stringlist[j])
else:
 print('Error:Choice can be either ascending or descending\n')

 
