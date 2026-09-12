# i=1  #this is a itrator
# while i<=10:# this is a stopping condition 
#     print(i)  # this is itration process
#     i+=1

# if i want to print in reverse 
# i=10

# while i>=1:
#     print(i)
#     i-=1

# if i want print reverse order number 100 to 1 then 

# i=100
# while i>=1:
#     print(i)
#     i-=1

# multipilication of number table n 
# n= int(input("Enter here Number:  "))
# i=1
# while i<=10:
#     print(n*i)
#     i+=1

# num= [1,4,16,25,36,45,55,65,75,80]
# x= 55
# # founding in list so we can write 
# index=0
# while index<len(num):
#     if (num[index]== x):
#         print("Found in Index",index)
#     else:
#        print("founding..")
#     index+=1

# this is the concept of break loop
# i=0
# while i<=5:
#     print(i)
#     if (i==2): # when condn is true then loop automatically close
#         break
#     i+=1
# print("END of LOOP")

# reverse break concept of loop 
# i=10
# while i>=1:
#     print(i)
#     if(i==6):
#         break
#     i-=1
# print("End of Loop")

# i=0
# while i<=10:
#     print(i)
#     if(i==4):
#         break
#     i+=1
# print("End of loop")

# i=0
# while i<=10:
#     if (i==7):
#         i+=1
#         continue # skip current number in iteration
#     print(i)
#     i+=1


#IF I Print Only Odd Number So i can write
# i=0
# while i<=10:
#     if (i%2==0):
#         i+=1
#         continue # skip current number in iteration 
#     print(i)
#     i+=1

# if we can print only even number so write
# i=0
# while i<=10:
#     if (i%2!=0):
#         i+=1
#         continue # skip current number in iteration 
#     print(i)
#     i+=1



# i=1
# while i<=5:
#     print("Hello")
#     i+=1

# i=1
# while i<=10:
#     print("Python")
#     i+=1

# for i in range(1):
#     print("Hello")

# for i in range(10):
#     print("python")

# for i in range(5):
#     print(i)

# for i in range(1,11):
#     print(i)

# for x in range(5,16):
#     print(x)

# for y in range(10,0,-1):
#     print(y)

# for ev in range(0,20,2):
#     print(ev)

# for odd in range(1,20,2):
#     print(odd)

# for i in range(5):
#     print(i)


# for i in range(2, 11, 2):
#     print(i)

# 22. Write a range() that generates 1, 3, 5, 7, 9.

# for i in range(1,10,2):
#     print(i)

# . Write a range() that generates 10, 8, 6, 4, 2.

# for y in range(10,0,-2):
#     print(y)

# Given products = ["Laptop", "Mobile", "Tablet", "Monitor"], write a loop to print every product.

# products = ["Laptop", "Mobile", "Tablet", "Monitor"]

# for i in products:
#     print(i)

# Given cities = ["Delhi", "Mumbai", "Lucknow", "Pune"], write a loop to print every city.

# cities = ["Delhi", "Mumbai", "Lucknow", "Pune"]

# for c in cities:
#     print(c)

# . Given numbers = [10, 20, 30, 40, 50], write a loop to print every number.
# numbers = [10, 20, 30, 40, 50]

# for num in numbers:
#     print(num)

# . Given salespersons = ["Rahul", "Amit", "Priya", "Neha"], write a loop to print each salesperson.

# salespersons = ["Rahul", "Amit", "Priya", "Neha"]

# for s in salespersons:
#     print(s)

# . Given products = ["Laptop", "Mobile", "Tablet", "Keyboard", "Mouse"], write a loop to print each product on a separate line.

# products = ["Laptop", "Mobile", "Tablet", "Keyboard", "Mouse"]

# for p in products:
#     print(p)

# Write a loop to print each value from this sales list:
# sales = [1000, 2500, 3500, 4500, 5000]

# sales = [1000, 2500, 3500, 4500, 5000]
# for s in sales:
#     print(s)

# . Write a loop to print each number from this list multiplied by 2:
# numbers = [5, 10, 15, 20]

# for num in numbers:
#     print(2*num)

# 33. Write a loop to print each sales value increased by 1000:
# sales = [5000, 10000, 15000, 20000]

# for s in sales:
#     print(s+1000)

# Write a loop to print the square of every number:
# numbers = [1, 2, 3, 4, 5]

# for num in numbers:
#     print(2**num)

# Write a loop to calculate the total of all values:
# sales = [1000, 2000, 3000, 4000]
# total=0

# for s in sales:
#     total=s+total
# print(total)

# Write a for loop to print each character of "Python" on a separate line.

# text="Python"

# for t in text:
#     print(t)

# . Write a loop to print each character of your name.

# name= "Akash Kumar"

# for n in name:
#     print(n)

# Write a loop to print every character of "Analytics".

# course= "Analytics"
# for c in course:
#     print(c)

# . Write a loop to print each character of "POWER BI" one by one.

# Course= "POWER BI"

# for c in Course:
#     print(c)

# Calculate the total sales using a for loop:
# sales = [5000, 10000, 15000, 20000]
# total=0

# for s in sales:
#     total= total+s
# print(total)

# . Calculate the total quantity using a for loop:
# quantity = [5, 10, 15, 20]
# total=0
# for q in quantity:
#     total= total+q

# print(total)

# Calculate the total of the following numbers using a loop:
# numbers = [10, 20, 30, 40, 50]
# total=0


# for num in numbers:
#     total = total + num
# print(total)

# Calculate the total sales and print the result:
# sales = [1200, 2500, 1800, 3200, 4500]
# total=0

# for s in sales:
#     total = total + s
# print(total)

# Calculate the total sales from the following list using a loop:
# sales = [10000, 25000, 15000, 30000, 20000]
# total=0

# for s in sales:
#     total = total + s
# print(total)

# Print only the sales values greater than 30000:
# sales = [10000, 25000, 50000, 75000, 15000, 45000]

# for s in sales:
#     if(s>30000):
#         print(s)

# Print only the numbers greater than 50:
# numbers = [20, 60, 40, 80, 100, 30]

# for num in numbers:
#     if num > 50:
#         print(num)

# Print only the sales values less than 20000:
# sales = [10000, 25000, 15000, 50000, 18000, 30000]

# for s in sales:
#     if s > 20000:

# Print only the numbers that are greater than 10:
# numbers = [5, 12, 8, 20, 15, 3]

# for num in numbers:
#     if num > 10:
#         print(num)

# Given the sales list below, use a for loop and condition to print only those sales values that are greater than 30000, then calculate their total:
# sales = [10000, 35000, 50000, 15000, 45000, 25000, 60000]
# total=0

# for s in sales:
#     total= total + s
#     if total>30000:
#         print(total) 


# name= input("Enter your Name Here: ")           
# age= int(input("Enter your age: "))
# Course_name= input("Type here Your Course name: ")
# City= input("Enter your city: ")

# print("I am",name,"and",age,"years old","and I want become an",Course_name,"lives in",City)

# light= input("Enter your light here: ")

# if(light=="Red"):
#     print("Stop")
# elif light== "Yellow":
#     print("Ready to go")
# elif light == "Green":
#     print("Go")
# else: 
#     light=="Blue"
#     print("broken")

# marks= int(input("Enter your marks: "))

# if marks > 85:
#     print("A")
# elif marks > 65:
#     print("B")
# elif marks > 45 :
#     print("C")
# elif marks > 33:
#     print("D")
# else:
#     print("Fail")

# Calculate tax deduction if your salary is less 50000 then 10% tax and your salary is greater than 50000 then tax 20%

# salary= float(input("Enter your salary: "))
# tax= salary * (0.1,0.2) [salary>=50000]
# print(tax)

# calculate the simple interest

# p= float(input("P: "))
# r= float(input("R: "))
# t= float(input("T: "))
# si= (p*r*t)/100
# print(si)

# name = input("Enter your name here: ")
# print(name)

# Arthmetics operators
a = 5
b = 6

# print(a+b)
# print(a-b)
# print(a*b)
# # print(a/b) when we have divide any number it's convert into float value 
# print(a%b) # this is modulo it's use for calculate reminder
# print(a**b) # use for sqaure

# name = input("Enter your name: ")
# coruse = input("Enter your course: ")
# age = float(input("Enter your age: "))
# marks = int(input("Enter your makrs: "))
# print("My name is",name,"and my course is",coruse,"my age is",age,"I have obtain marks:",marks)



# num1 = int(input("Enter here number: "))
# num2 = int(input("Enter here number: "))

# print("total= ",num1*num2)

# # concatenation means adding two strings ex
# str1 = "Akash"
# str2 = "Chaudhary"
# final_str = str1 + " " + str2

# print(final_str)

# print(len(final_str))

# name = input("Enter your name: ")
# Len = len(name)
# print("Len:",len(name))

# name = "$I am Akash $Kumar$"
# print(name.count("$"))

# num = int(input("Enter Any number Here:"))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
# print("Number is: ",num)


# num = int(input("Enter number here:"))

# if num % 7 == 0:
#     print("Divisible by 7")
# else:
#     print("Not divisible")
# print("Number is:",num)

# marks = [75, 65, 79, 80, 85, 92, 96]

# print(marks[2])
# print(len(marks))

# print(marks[1:5])
# print(marks[-5:-2])

# it's called List Function 

# append function use to add some number of the end of list 

# marks.append(66) # this is a example of append and it's also called mutated in list/ change in list
# print(marks)


# marks = [75, 65, 79, 80, 85, 92, 96]

# list.sort(marks) # this method called an arrange list in assending order
# print(marks)

# list.sort()
# print(marks)
# print(marks.append(82))
# print(marks.sort())
# print(marks)

# if i want to print dessending order then 

# marks.sort(reverse=True)
# print(marks)

# list=  ["Banana","Apple","orange","pineapple"]

# list.append("Kiwi") # it's function also work on strings 
# print(list)

# list.sort() # this a assending order 
# print(list)

# list.sort(reverse=True) # this is a desending order 
# print(list)

# list.reverse() this function reverse all value in list in opposite direction
# print(list)

# Insert function

# list.insert(0,"litchi")
# print(list)

# list.insert(2,"Guvava")
# print(list)

# list= [1,2,3,4,5,6]d list.insert(1,8) # index wise value fill krta hai 
# print(list)

# list.insert(3,10)
# print(list)

# list.sort()
# print(list) # this is a assending order list

# list.sort(reverse=True) # this is desending order 
# print(list)

# list.reverse()
# print(list)

# list= [1,2,3,4,5,6]

# list.remove(2) # remove function only used for inside the value of list to delete.
# print(list)

# # pop function delete index wise 
# list.pop(1)
# print(list)


# # write a programme ask to user fav 3 movies and convert into list
#1st method to write :-

# movies= []
# mov= input("Enter your 1st movie:")
# movies.append(mov)
# mov= input("Enter your 2st movie:")
# movies.append(mov)
# mov= input("Enter your 3st movie:")
# movies.append(mov)
# print(movies)

#2nd method to write this programme:-

# movies=[]

# movies.append(input("Enter your 1st fav Movie:"))
# movies.append(input("Enter your 2st fav Movie:"))
# movies.append(input("Enter your 3st fav Movie:"))
# print(movies)

# palindrome list creating method
# if value inside the list forword direction reading shame and reversed reading same then list is palindrome list 
# list= [1,2,3,3,2,1]
# list.copy()
# print(list)
# list.reverse()
# print(list)

# list= ["racecar"]
# list.copy()
# print(list)
# list.reverse()
# print(list)

list1= ["racecar"]
list_1= list1.copy()
list_1.reverse()
if list_1==list1:
    print("Palindrom")
else:
    print("not palindrom")

i=1
while i<=10:
    print(i)
    i+= 1


