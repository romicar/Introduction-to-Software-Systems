"""
Created on Fri May 31 19:01:54 2022
@author: romica
"""

# connecting with mysql
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Romica@1112"
)
# Creating Cursor Instance
mycursor = mydb.cursor()

# Create A Database
mycursor.execute("CREATE DATABASE IF NOT EXISTS Record")
mycursor.execute("USE Record")

# Delete the table Ticker if exits in record
sql = "DROP TABLE IF EXISTS Ticker"
mycursor.execute(sql)

# Delete the table Metrics if exits in record
sql = "DROP TABLE IF EXISTS Metrics"
mycursor.execute(sql)

def findconfidence(line, readcontrol1, readcontrol2, readcontrol3,
                   readcontrol4, readcontrol5, readcontrol6,
                   readcontrol7, readcontrol8, readcontrol9):
    if line[2] == 'Finance - General':
        low_con = readcontrol1[1][1].split("%")
        med_con1 = readcontrol2[1][1].split("%")
        med_con2 = readcontrol2[1][3].split("%")
        med_con2 = med_con2[0].split("<=")
        high_con = readcontrol3[1][0].split("%")
        high_con = high_con[0].split(">")
        if float(line[5]) < float(readcontrol1[1][1][0]):
            confidence = 'Low'
        elif (float(line[5]) >= float(readcontrol2[1][1][0])
              and float(line[5]) <= float(readcontrol2[1][3][2])):
            confidence = 'Medium'
        elif float(line[5]) > float(readcontrol3[1][0][1]):
            confidence = 'High'
    if line[2] == 'Auto Ancillaries':
        low_con = readcontrol4[1][1].split("%")
        med_con1 = readcontrol5[1][1].split("%")
        med_con2 = readcontrol5[1][3].split("%")
        med_con2 = med_con2[0].split("<=")
        high_con = readcontrol6[1][0].split("%")
        high_con = high_con[0].split(">")
        if float(line[5]) < float(low_con[0]):
            confidence = 'Low'
        elif (float(line[5]) >= float(med_con1[0])
              and float(line[5]) <= float(med_con2[1])):
            confidence = 'Medium'
        elif float(line[5]) > float(high_con[1]):
            confidence = 'High'
    if line[2] == 'Ceramics & Granite':
        low_con = readcontrol7[1][1].split("%")
        med_con1 = readcontrol8[1][1].split("%")
        med_con2 = readcontrol8[1][3].split("%")
        med_con2 = med_con2[0].split("<=")
        high_con = readcontrol9[1][0].split("%")
        high_con = high_con[0].split(">")
        if float(line[5]) < float(low_con[0]):
            confidence = 'Low'
        elif (float(line[5]) >= float(med_con1[0])
              and float(line[5]) <= float(med_con2[1])):
            confidence = 'Medium'
        elif float(line[5]) > float(high_con[1]):
            confidence = 'High'
    return confidence


# Creating Ticker
mycursor.execute(("CREATE TABLE IF NOT EXISTS Ticker (date VARCHAR(255)"
                  ",companyname VARCHAR(255), industry VARCHAR(255), "
                  "previousdayprice VARCHAR(255), currentprice VARCHAR(255),"
                  " changeinprice VARCHAR(255), confidence VARCHAR(255))"))

# Creating Metrics
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS"
    " Metrics (kpis VARCHAR(255), metric VARCHAR(255))")

# Opening files containing data from date 20-05-2022
# to 24-05-2022 and control file
file20 = open(r"Record/2021101053-Date-20-05-2022.csv", "r")
file21 = open(r"Record/2021101053-Date-21-05-2022.csv", "r")
file22 = open(r"Record/2021101053-Date-22-05-2022.csv", "r")
file23 = open(r"Record/2021101053-Date-23-05-2022.csv", "r")
file24 = open(r"Record/2021101053-Date-24-05-2022.csv", "r")
control = open(r"Control/control-table.csv", "r")

# Reading data from the files opened above starting from line 1
readfile20 = file20.readlines()[1:]
readfile21 = file21.readlines()[1:]
readfile22 = file22.readlines()[1:]
readfile23 = file23.readlines()[1:]
readfile24 = file24.readlines()[1:]

# creating price list of date 20-05-2022
pricelist20 = []
# creating price list of date 21-05-2022
pricelist21 = []
# creating price list of date 22-05-2022
pricelist22 = []
# creating price list of date 23-05-2022
pricelist23 = []
# creating price list of date 24-05-2022
pricelist24 = []

list20 = []
list21 = []
list22 = []
list23 = []
list24 = []

# reading data from control file

# reading header row
control.readline()
# data of first line
readcontrol1 = control.readline()
# data of second line
readcontrol2 = control.readline()
# data of third line
readcontrol3 = control.readline()
# data of fourth line
readcontrol4 = control.readline()
# data of fifth line
readcontrol5 = control.readline()
# data of sixth line
readcontrol6 = control.readline()
# data of seventh line
readcontrol7 = control.readline()
# data of eight line
readcontrol8 = control.readline()
# data of ninth line
readcontrol9 = control.readline()


# spliting the data of the above lines seperated by comma
readcontrol1 = readcontrol1.split(',')
readcontrol1[1] = readcontrol1[1].split()
readcontrol2 = readcontrol2.split(',')
readcontrol2[1] = readcontrol2[1].split()
readcontrol3 = readcontrol3.split(',')
readcontrol3[1] = readcontrol3[1].split()
readcontrol4 = readcontrol4.split(',')
readcontrol4[1] = readcontrol4[1].split()
readcontrol5 = readcontrol5.split(',')
readcontrol5[1] = readcontrol5[1].split()
readcontrol6 = readcontrol6.split(',')
readcontrol6[1] = readcontrol6[1].split()
readcontrol7 = readcontrol7.split(',')
readcontrol7[1] = readcontrol7[1].split()
readcontrol8 = readcontrol8.split(',')
readcontrol8[1] = readcontrol8[1].split()
readcontrol9 = readcontrol9.split(',')
readcontrol9[1] = readcontrol9[1].split()


for line in readfile20:
    line = line.replace("\n", "")
    line = line.split(',')
    line.insert(0, "20-5-2022")
    pricelist20.append(line[3])
    line = tuple(line)
    list20.append(line)


i = 0
for line in readfile21:
    line = line.replace("\n", "")
    line = line.split(',')
    line.insert(0, "21-5-2022")
    line.insert(3, pricelist20[i])
    line[3] = float(line[3])
    line[4] = float(line[4])
    pricelist21.append(line[4])
    change = ((line[4] - line[3])/line[3])*100
    line.append(change)
    confidence = findconfidence(line, readcontrol1, readcontrol2,
                                readcontrol3, readcontrol4, readcontrol5,
                                readcontrol6, readcontrol7, readcontrol8,
                                readcontrol9)
    line.insert(6, confidence)
    line = tuple(line)
    list21.append(line)
    i = i + 1

# exceptioncase with unwanted spaces
i = 0
for line in readfile22:
    line = line.replace("\n", "")
    line = line.split(',')
    line.remove('')
    line.remove('')
    line.insert(0, "22-5-2022")
    line.insert(3, pricelist21[i])
    line[3] = float(line[3])
    line[4] = float(line[4])
    pricelist22.append(line[4])
    change = ((line[4] - line[3])/line[3])*100
    line.append(change)
    confidence = findconfidence(line, readcontrol1, readcontrol2,
                                readcontrol3, readcontrol4,
                                readcontrol5, readcontrol6, readcontrol7,
                                readcontrol8, readcontrol9)
    line.insert(6, confidence)
    line = tuple(line)
    list22.append(line)
    i = i + 1

i = 0
for line in readfile23:
    line = line.replace("\n", "")
    line = line.split(',')
    line.insert(0, "23-5-2022")
    line.insert(3, pricelist22[i])
    line[3] = float(line[3])
    line[4] = float(line[4])
    pricelist23.append(line[4])
    change = ((line[4] - line[3])/line[3])*100
    line.append(change)
    confidence = findconfidence(
        line, readcontrol1, readcontrol2, readcontrol3,
        readcontrol4, readcontrol5, readcontrol6,
        readcontrol7, readcontrol8, readcontrol9)
    line.insert(6, confidence)
    line = tuple(line)
    list23.append(line)
    i = i + 1

i = 0
for line in readfile24:
    line = line.replace("\n", "")
    line = line.split(',')
    line.insert(0, "24-5-2022")
    line.insert(3, pricelist23[i])
    line[3] = float(line[3])
    line[4] = float(line[4])
    pricelist24.append(line[4])
    change = ((line[4] - line[3])/line[3])*100
    line.append(change)
    confidence = findconfidence(
        line, readcontrol1, readcontrol2, readcontrol3,
        readcontrol4, readcontrol5, readcontrol6,
        readcontrol7, readcontrol8, readcontrol9)
    line.insert(6, confidence)
    line = tuple(line)
    list24.append(line)
    i = i + 1

# inserting the rows with 20-5-2022 into Ticker
sql = ("INSERT INTO Ticker"
       " (date , companyname, industry,"
       " currentprice) VALUES (%s, %s, %s, %s)")
val = list20

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")

# inserting the rows with 21-5-2022 into Ticker
sql = "INSERT INTO Ticker  VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = list21

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")

# inserting the rows with 22-5-2022 into Ticker
sql = "INSERT INTO Ticker  VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = list22

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")

# inserting the rows with 23-5-2022 into Ticker
sql = "INSERT INTO Ticker  VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = list23

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")

# inserting the rows with 24-5-2022 into Ticker
sql = "INSERT INTO Ticker  VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = list24

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")


# Select companyname and currentprice from rows of ticker with date 20-5-2022
mycursor.execute(
    "select companyname, currentprice from Ticker where date like '20-5-2022'")
myresult20 = mycursor.fetchall()
# Select currentprice from rows of Ticker with date 24-5-2022
mycursor.execute(
    "select  currentprice from Ticker where date like '24-5-2022'")
myresult24 = mycursor.fetchall()

gainpercent = [[]]
for x in myresult20:
    gainpercent.append([x[0], x[1]])

count = 1
for x in myresult24:
    gainpercent[count].append(x[0])
    count = count + 1

# deleting the empty sublist at index 0
gainpercent.pop(0)


# temp - stores the max gain%
temp = 0
# tempmin - stores the min gain% or max loss%
tempmin = 10000000000000
# tempcompany - the name of company with max gain%
tempcompany = ""
# tempmincompany - the name of the comapny with max loss%
tempmincompany = ""

for x in gainpercent:
    x.append(((float(x[2]) - float(x[1]))/float(x[1]))*100)
    temp = max(x[3], temp)
    if(temp == x[3]):
        tempcompany = x[0]
    tempmin = min(tempmin, x[3])
    if(tempmin == x[3]):
        tempmincompany = x[0]

# counting the total no. of highs for Finance - General
mycursor.execute(
    "select count(*) from Ticker where industry"
    " = 'Finance - General' and confidence = 'High'")
high_banking = mycursor.fetchall()

# counting the total no. of highs for Auto Ancillaries
mycursor.execute(
    "select count(*) from Ticker where industry"
    " = 'Auto Ancillaries' and confidence = 'High'")
high_auto = mycursor.fetchall()

# counting the total no. of highs for Ceramics & Granite
mycursor.execute(
    "select count(*) from Ticker where industry"
    " = 'Ceramics & Granite' and confidence = 'High'")
high_granite = mycursor.fetchall()

# determining the max no of highs among the three industry
bestindustryvalue = max(
    high_granite[0][0], high_auto[0][0], high_banking[0][0])

# storing bestindustry as the one corresponding to max highs
if(bestindustryvalue == high_banking[0][0]):
    bestindustry = "Finance - General"
elif(bestindustryvalue == high_granite[0][0]):
    bestindustry = "Ceramics & Granite"
elif(bestindustryvalue == high_auto[0][0]):
    bestindustry = "Auto Ancillaries"


# counting the total no. of lows for Finance - General
mycursor.execute(
    "select count(*) from Ticker where industry"
    " = 'Finance - General' and confidence = 'Low'")
low_banking = mycursor.fetchall()

# counting the total no. of lows for Auto Ancillaries
mycursor.execute(
    "select count(*) from Ticker where industry "
    "= 'Auto Ancillaries' and confidence = 'Low'")
low_auto = mycursor.fetchall()

# counting the total no. of lows for Ceramics & Granite
mycursor.execute(
    "select count(*) from Ticker where industry"
    " = 'Ceramics & Granite' and confidence = 'Low'")
low_granite = mycursor.fetchall()


# determining the max no of lows among the three industry
worstindustryvalue = max(low_granite[0][0], low_auto[0][0], low_banking[0][0])

# storing worstindustry as the one corresponding to max lows
if(worstindustryvalue == low_banking[0][0]):
    worstindustry = "Finance - General"
elif(worstindustryvalue == low_granite[0][0]):
    worstindustry = "Ceramics & Granite"
elif(worstindustryvalue == low_auto[0][0]):
    worstindustry = "Auto Ancillaries"


# inserting into metrics corresponing kpis and values
sql = "INSERT INTO Metrics VALUES (%s, %s)"
val = [('Best listed industry', bestindustry),
       ('Best company', tempcompany), ('Gain %', temp),
       ('Worst listed company', worstindustry),
       ('Worst company', tempmincompany), ('Loss %', tempmin)]

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")