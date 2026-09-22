# def calculate_total(a, b): 
    
#     return a+b

# print(calculate_total(2, 4))
# # 2, and 4 are arguments 


# print(calculate_total(12, 16))

# calculate_total(2,4)

# sales = 2000
# def calculatePerformance(sales):
#     if(sales >= 5000):
#         print("Excellent")
#         print("Keep it up")
#     elif(sales >= 1000):
#         print("Average")
#         return
#         print("You have to make more sales")
#     else:
#         print("BAd sales")

# def calculaterange():

#     for i in range(1,10):
#         if(i == 5):
#             continue
#         print(i)

# calculaterange()


# def greet(name = "Amit"):
#     print("hello" , name)

# greet("Shivam")

# keyword argument
# def employee_info(name, department, salary):
#     print("Name: ", name, " Department: ", department, " Salary: ", salary)

# employee_info(name = "Amaan", department="IT", salary=70000)
# employee_info(name = "Anurag", department="HR", salary=45000)
# employee_info(name = "kaif", department="Sales", salary=55000)


# def Calculate(a, b):
#     total = a + b
#     difference = a - b 
#     return total,difference

# # total, difference = Calculate(15,5)
# # print(total)
# # print(difference)

# Total = Calculate(15, 5)
# print(Total)

# def greet():
#     return
# print("hello")

# def greeting():
#     return
# print("Hello Student")

# Create a function that accepts a name and prints "Hello <name>".

# def name():
#     return
# print("Hello Akash")

# . Create a function that accepts two numbers and prints their sum.

# def sum(a,b):
#     return a+b
# print(sum(2,4))

# def difference(a,b):
#     return a-b
# print(difference(47,17))

# Create a function that accepts two numbers and returns their multiplication.

# def cal_multiplication(a,b):
#     return (a*b)
# print(cal_multiplication(16,9))

# Create a function that accepts a number and returns its square.

# def cal_square(a):
#     return a ** 2
# result= cal_square(19)
# print(result)

# Create a function that accepts price and quantity and returns total amount.

# def cal_amount(price,quantity):
#     return (price * quantity)
# print(cal_amount(200,5))

# Create a function that accepts marks and returns "Pass" or "Fail".

# def result_analysis(a):
#     if a >= 90:
#          return("Pass")
#     else: 
#          return("Fail")
# print(result_analysis(50))

# Create a function that accepts age and returns "Adult" or "Minor".

# def vote_eligiblity(age):
#     if age >=18:
#         return("Eligible")
#     else:
#         return("Not Eligible")
# print(vote_eligiblity(17))

# Create a function that accepts salary and returns Excellent/Good/Average/Poor using thresholds 80000, 60000, and 40000.

# def salary_analysis(salary):
#     if salary>=80000:
#         return("Excellent")
#     elif salary >= 60000:
#         return("Good")
#     elif salary >= 40000:
#         return("Average")
#     else:
#         return("Poor")
# print(salary_analysis(80000))

# . Create a function that accepts purchase amount and returns Premium/Gold/Silver/Regular using thresholds 100000, 50000, and 20000.

# def customer_category(purchase):
#     if purchase >= 100000:
#         return("Premium")
#     elif purchase >= 50000:
#         return("Gold")
#     elif purchase >= 20000:
#         return("Silver")
#     else:
#         return("Regular")
# print(customer_category(120000))

# Create a function to calculate 10% discount

# def discount(price, discount):
#     return ( price * discount/100)
# print(discount(25000,20))

# . Create a function that accepts amount and discount percentage and returns final amount

# def discounted_price(price,discount):
#     discount = (price * discount / 100)
#     return(price - discount)
# print(discounted_price(15000,20))
    
# Create a function that accepts a number and returns "Even" or "Odd".

# def check_odd_even(num):
#     if (num % 2== 0):
#         return("Even")
#     else:
#         return("Odd")
# print(check_odd_even(16))

# Create a function that accepts a city and checks whether it is Delhi or Mumbai.

# def city_check(city):
#     if city == "Mumbai" or city == "Delhi":
#         return("Found")
#     else:
#         return("Not found")
# print(city_check("banguluru"))

#  Create a function that accepts purchase and orders and returns VIP when purchase >= 50000 AND orders >= 5; otherwise return Regular.

# def customer_category(purchase,quantity):
#     if purchase >= 50000:
#         if quantity >= 5:
#             return("VIP")
#     else:
#         return("Regular")
# print(customer_category(40000,5))

# second method to write this function 

# def customer_category(purchase, order):
#     if purchase >= 50000 and order >= 5:
#         return("VIP")
#     else:
#         return("Regular")
# print(customer_category(50000,5))

# Create a function that calculates the total of a list of numbers

# def total_sum_num(numbers):
#     return sum (numbers)
# numbers= [23,45,20,41,55,66,85,96]
# print(total_sum_num(numbers))

# Create a function that calculates the average of a list.

# def avg_num(numbers):
#     return sum(numbers) / len(numbers)
# numbers = [20,40,50,60,70,85,63,46,98,56,54]
# total= avg_num(numbers)
# print(total)

# reate a function that returns the highest value from a list.

# def find_highest(number):
#     return max(number)
# number = (98,45,65,28,56,36,77,86,466,789496)
# max= find_highest(number)
# print(max)

# Create a function that returns the lowest value from a list.

# def find_lowest(num):
#     return min(num)
# num = [10,50,98,75,66,25,45,92,56]
# minimum = find_lowest(num)
# print(minimum)

# Create a function that counts numbers greater than 50000

# def count_high_salary(salary):
#     count = 0

#     for i in salary:
#         if i > 50000:
#             count += 1

#     return count

# salary = [30000,40000,50000,60000,80000,78000]
# print(count_high_salary(salary))

# Given sales = [10000, 25000, 50000, 75000, 120000], create a function that classifies each sale as High or Low.

# def classify_sale(sales):
#     if sales > 100000:
#         return("High")
#     else:
#         return("Low")

# sales = [10000, 25000, 50000, 75000, 120000]

# print(classify_sale(120000))

# Use a loop and your function to classify every sale in the sales list.

# def check_sale(sales):
#     if sales >= 100000:
#         return("High")
#     elif sales > 70000:
#         return("Good")
#     elif sales > 40000:
#         return(" Improvement")
#     else:
#         return ("Poor")
        
# sales = [10000, 25000, 50000, 75000, 120000]
# for sale in sales:
#     print(sale,check_sale(sale))

# Create a function to calculate total sales from a list.

# def total_sales(sales):
#     total = 0
#     for sale in sales:
#         total += sale
#     return total
# sales = [10000, 25000, 50000, 75000, 120000]
# print(total_sales(sales))

# Create a function to calculate average sales from a list.

# def avg_sales(sales):
#     avg = sum(sales)/len(sales)
#     return avg
    
# sales = [10000, 25000, 50000, 75000, 120000]
# print(avg_sales(sales))


# Create a function to calculate 10% discount on every sale.

# def discounted_sales(sales):
#     return [sale- (sale*10/100) for sale in sales]

# sales = [10000, 25000, 50000, 75000, 120000]
# discount_price = discounted_sales(sales)
# print(discount_price)




