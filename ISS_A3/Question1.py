"""
Created on Sat May 17 12:05:13 2022
@author: romica
"""
start = int(input("Enter an even number between length of stars: "))
print("\n")
if ( start % 2 == 0):
 for i in range(start,0,-2):
   star = i*'*'
   star = star.center(start)
   print(star)
 for i in range(2,start + 2,2):
   star = i*'*'
   star = star.center(start)
   print(star)
else:
    print('Error:Length has to be an even number')
        
        

    
   