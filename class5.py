def calculate_total(a, b): 
    
    return a+b

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


def Calculate(a, b):
    total = a + b
    difference = a - b 
    return total,difference

# total, difference = Calculate(15,5)
# print(total)
# print(difference)

Total = Calculate(15, 5)
print(Total)