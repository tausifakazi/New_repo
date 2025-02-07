'''First_Name = input("First Name : ")
Last_Name = input("Last Name : ")
Age = int(input("age : "))
Percentage = float(input("HSC Marks : "))

output = "Values are correct"

print(output) if First_name == "tausif" and Last_Name == "kazi" and Age == 34 and Percentage >= 80 else print("Records are incorrect")

if First_Name == "Tausif" and Last_Name == "Kazi" and Age >= 25 and Percentage >=65:
    print("Full Name is ", First_Name, Last_Name, "and age is", Age, "and HSC percentage is ", Percentage,'%')
else:
    print("You are not eligible")

====================================================
food = input("food : ")
print("sweet") if food =="cake" or food = "jalebi" else print ("No Sweet")
====================================================
#Clever IF / Ternary Operator

age = int(input("Age : "))
vote = ("Yes", "No") [age >=18]
print(vote)
====================================================
sal = float(input("Salary :"))
tax = sal*(0.1, 0.2) [sal<= 50000]
print(tax)
====================================================
Name = (input("Type name :"))
print(len(Name))
====================================================
str = "I have a $1 million and farheen have $2 Million"
print(str.count("$"))
====================================================
marks = int(input("What is your marks :"))
if (marks >= 90):
    print("Your Grade is A")
elif (marks > 90 and marks >= 80):
    print("Your Grade is B")
elif (marks > 80 or marks >= 70):
    print("Your Grade is C")
elif (marks > 70):
    print("Your Grade is D")
====================================================
num = int(input("enter number :"))
rem = num % 2
if (rem == 0):
    print("EVEN")
else:
    print("ODD")
====================================================
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
if (a >= b or a >= c):
    print("First number is largest ",a)
elif (b >= c):
    print("Second number is largest ",b)
else:
    print("Third number is largest ",c)
====================================================
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")
====================================================
import platform
print(platform.python_version_tuple())
====================================================
import datetime

current_time = float

current_time = datetime.datetime.now()

currect_time = currect_time - 1

print("Currect time ", (current_time.strftime("%Y-%m-%d %H:%M:%S")))
====================================================

Marks = ['Tausif', 'Kazi', '34', 'Mumbai', 'India', '400612']
print(Marks)
Marks.insert(2, 38)
print(Marks)
Marks.remove(38)
print(Marks)
Marks.pop(3)
print(Marks)
print(Marks.sort())
print(Marks.sort(reverse= True))
print(Marks)
print(Marks[0] == "Tausif")
print(type(Marks))
print(Marks[1:4])
print(Marks.append('g'))
print(len(Marks))
Marks[0] = "Farheen"
print(Marks)
====================================================

tup = ('India', 'Maharashtra', '400612')
Marks = ['Tausif', 'Kazi', '34', 'Mumbai', 'India', '400612']
print(type(tup, Marks))
====================================================
Movie = []
Movie.append(str(input("Enter you first movie : ")))
Movie.append(str(input("Enter you second movie : ")))
Movie.append(str(input("Enter you third movie : ")))

print(Movie)
====================================================
#Dictionary & Set

#Dictionary
Info = {
    "Name" : "Tausif",
    "list1" :['HSC', 'BSC', 'Python'],
    "list2" : ('30', '40', '50'),
    "Age" : 34,
    "State" : "Maharashtra",
    "Marks" : 45.60
}
print(Info)
print(Info.keys())

Info1 = {
    "Name" : "Tausif",
    "Age" : 34
}
#Info.__delitem__("Name")
Info.update({"Name" : "Farheen"})
print(Info)
print(Info.keys()) 

#Set
collection = {1, 2, 3, 4, 5}
print(collection)
print(type(collection))

collection1 = set() #Empty set sybtax
print(collection1)
====================================================
Furniture = {
    "table" : ["a piece of furniture", "list of facts & figures"],
    "cat" : "a small animal"
}
print(type(Furniture))
print(Furniture)

subject = {"python", "Java", "C++", "Java", "Javascript", "Java", "python", "Java", "C++", "C"}
print("How many classroom we needed for this batch : ", len(subject))
print(type(subject))

count = 1
while count >= 4:
    ver = 1
marks = {}
subject = input("Enter your subject :")
Pers = int(input("Enter marks : "))
marks.update({subject : Pers})
print(marks)
count+=1

====================================================

num = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

x = 0
value = int(input("Enter value :"))

while x < len(num):
    if(num[value]==x):
        print("value existed")
        break
    else:
        print("finding...")
    x+=1
 ====================================================

#ODD & EVEN using with CONTINUE 
#ODD
i = 1
while i <= 10:
    if(i%2 == 0):
        i += 1
        continue
    print(i)
    i  += 1
#EVEN
i = 1
while i <= 10:
    if(i%2 != 0):
        i += 1
        continue
    print(i)
    i  += 1
====================================================

#for loop == Loops are used for sequential traversal. 
#For Traversing list, string, tuples etc.

num = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

i = 0
x = 5

for list in num:
    if list == x:
        print(list)
        break
    i += 1
====================================================

#range() = Range functions returns a sequence of numbers,
#starting from 0 by default, and increments by 1(by default),
#and stops before a specified number.

for i in range(10): #range(stop)
    print(i)

for i in range(2, 10): #range(start, stop)
    print(i)

for i in range(2, 10, 2): #range(start, stop, step)
    print(i)

====================================================
#Pass statement == pass is a null statement that does nothing. 
#It is used as a placeholder for future code.

for i in range(5): 
    if i == 1:
        pass
    print(i)
====================================================

n = 7
sum = 0
i = 1
while i <= n:
    sum +=i
    i += 1
print("total sum = ", sum)

====================================================

#Tables 

number = int(input("Which table needed : "))
end_rang = int(input("End digits :"))
number1 = int(1)
number2 = int(0)
i = 1

while i <= end_rang:
    number1 = number*i
    print(number, "X", i, "=",  number1)
    i += 1
====================================================
#Function in Python == Block of statements that perform a specific task.
def num(x):
    print(input("Enter the Number : "))
    return x
    print("Entered values is ", x)

num()

i = 1
while i < 10:
    if(i%2 == 0):
        i += 1
    i  += 1
#EVEN
i = 1
while i <= 10:
    if(i%2 != 0):
        i += 1
    print(i)
    i  += 1
====================================

New_file = open("First_TXT_File.TXT", "r+")
New_file.write("My first I/O code for write3")
New_file.write("\nSecond line of records")
New_file.close()

New_file = open("First_TXT_File.TXT")
rl = New_file.read()
print(rl)
New_file.close()


import os
os.remove("First_TXT_File.TXT")
====================================

New_file = open("Practice.TXT", "a+")
New_file.write("Hi everyone\nwe are learning File I/O \nusing Java \nI like programing in Java")
print(New_file.read())
New_file.close()
====================================

with open("Practice.txt", "r") as f:
    read_data = f.read()
    Replace_data = read_data.replace("Java", "Python")
    print(read_data)

with open("practice.txt", "w") as f:
    final = f.write(Replace_data)
    print(final)
====================================
def check_for_word():
    word = "learnings"
    with open("Practice.txt", "r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("Found")
        else:
            print("Not found")

def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("Practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(wor]d in data):
                print(line_no)
                return
                line_no += 1
    return -1

print(check_for_line())

====================================
count = 0
with open("Practice.txt", "r") as f:
    data = f.read()
    num = data.split(',')
    for val in num:
        if(int(val)%2 == 0):
            count =+1
print(val)
====================================

#OOPS
#Constructors and classes

class Student:
    def __init__(self, name, marks, subject):
        self.name = name
        self.marks = marks
        self.subject = subject
        values = print("Student name is ", name, "his marks is", marks, "in subject", subject)

s1 = Student("Tausif", 97, "Maths")
s2 = Student("Farheen", 90, "English")
print(s1, s2)
====================================

class order:
    def __init__(self, item, price):
        self.item = item
        self.price = price 

    def showlist(self):
        print("item ", self.item, "and price is " ,self.price)

    def __gt__(self, od1):
        return self.price < od2.price

od1 = order("Rice", 100)
od2 = order("chips", 20)
print(od1 > od2)

===================================='''

import random
RandNum = random.randint(1, 5)

while True:
    userChoice = int(input("Choose correct number :"))
    if (userChoice == RandNum):
        print("You choose correct number... Congragulation")
        break
print("-----GAME OVER-----")
print(RandNum)

'''====================================

from sklearn.linear_model import LinearRegression
import numpy as np

# Sample data
X = np.array([[1], [2], [3]])  # Features (e.g., square footage)
y = np.array([1, 2, 3])        # Target variable (e.g., house prices)

# Create a Linear Regression model
model = LinearRegression()

# Fit the model to the data
model.fit(X, y)

# Predict new values
X_new = np.array([[4]])  # New feature value
y_pred = model.predict(X_new)

print(f'Predicted value for X_new: {y_pred[0]}')
===================================='''