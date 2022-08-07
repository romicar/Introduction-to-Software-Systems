"""
Created on Sat May 20 12:0:43 2022
@author: romica
"""
datalist = []          
rollnumberlist = []    
newdatalist = []       
namelist = []          
mathlist = []          
cselist = []           
sciencelist = []        
markslist = []         

number = int(input('Enter the number of students: '))

if number > 0:
    for i in range(1,number + 1,1):
        studentlist = []
        name = input('Enter name: ')
        rollnumber = int(input('Enter roll number: '))
        math = int(input("Enter math marks: "))
        cse = int(input("Enter CSE marks: "))
        science = int(input("Enter Science marks: "))
        marks = math + science + cse
        studentlist.extend([name,rollnumber,math,cse,science,marks])
        rollnumberlist.append(rollnumber) 
        datalist.append(studentlist)
    rollnumberlist.sort()
    for i in rollnumberlist:
       m = 0
       while m < len(datalist):
           if datalist[m][1] == i:
               newdatalist.append(datalist[m])
           m = m + 1
    
    for i in newdatalist:
        
        namelist.append(i[0])
        mathlist.append(i[2])
        cselist.append(i[3])
        sciencelist.append(i[4])
        markslist.append(i[5])
        
    datalist.sort(key = lambda x:x[5]) 
    nameranklist = []
    rollnumberranklist = []
    for i in datalist:
        nameranklist.append(i[0])
        rollnumberranklist.append(i[1])
    
    print('\nroll no   name\n')
    i = 0
    while i < len(newdatalist):
        print(f'  {rollnumberlist[i]} \t {namelist[i]}')
        i = i + 1
# if the total marks of two students are same then priority is given according to roll number ordering
    userchoice = str(input('Choose method of input(RollNumber Or Name): '))
    if userchoice == 'Name':
        username = input('Enter name: ')
        index = namelist.index(username)
        index2 = nameranklist.index(username)
        rank = number - index2 
        mean = (mathlist[index] + cselist[index] + sciencelist[index]) / 3
        medianlist = [mathlist[index] , cselist[index] , sciencelist[index]]
        medianlist.sort()
        median = medianlist[1]
        
        print(f'Name = {username} ')
        print(f'Roll number = {rollnumberlist[index]} (CSE : {cselist[index]} Science : {sciencelist[index]} Maths : {mathlist[index]})')
        print(f'marks = {markslist[index]}')
        print(f'median = {median}')
        print(f'mean = {mean}')
        print(f'rank = {rank}')
    elif userchoice == 'RollNumber':
        userrollnumber = int(input('Enter roll number: '))
        index = rollnumberlist.index(userrollnumber)
        index2 = rollnumberranklist.index(userrollnumber)
        rank = number - index2 
        mean = (mathlist[index] + cselist[index] + sciencelist[index]) / 3
        medianlist = [mathlist[index] , cselist[index] , sciencelist[index]]
        medianlist.sort()
        median = medianlist[1]
    
        print(f'Name = {namelist[index]} ')
        print(f'Roll number = {rollnumberlist[index]}')
        print(f'Total marks = {markslist[index]} (CSE : {cselist[index]} Science : {sciencelist[index]} Maths : {mathlist[index]})')
        print(f'Median = {median}')
        print(f'Mean = {mean}')
        print(f'Rank = {rank}')
else:
    print('The number of students should be above 0/n')
        
        
    
