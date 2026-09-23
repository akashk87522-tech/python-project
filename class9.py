import numpy as np 

# number = np.array([25,35,45,50,60])
# print(number)

# sales = [10000, 15000, 12000, 18000, 20000]

# sales_array = np.array(sales)
# print(sales_array)

# total_sales = np.sum(sales_array)
# print(total_sales)

# average = np.average(sales_array)
# print(average)

# lowest_sales = np.min(sales_array)
# print(lowest_sales)
# print(np.min(sales)) 

# Highest_sales = np.max(sales_array)
# print(Highest_sales)

# std = np.std(sales_array)
# print(std)

# # indexing

# print(sales_array[1])
# print(sales_array[0])
# print(sales_array[-2])

# # slicing
# print(sales_array[1:4])
# print(sales_array[:2])
# print(sales[::3])

# for sales in sales_array(1,21):
#     print(sales)

# sales = np.array([
#     12000, 18000, 15000, 22000,
#     30000, 17000, 25000, 14000,
#     35000, 28000])

# 1.	Calculate total sales.

# Total_sum = np.sum(sales)
# print(Total_sum)

# 2.	Calculate average sales.

# print(np.average(sales))

# 3.	Find the highest sale.
# print(np.max(sales))

# 4.	Find the lowest sale.
# print(np.min(sales))

# 5.	Show sales greater than ₹20,000.

# print(sales > 20000)

# 6.	Show sales less than ₹15,000.

# print(sales < 15000)

# 7.	Add ₹2,000 to every sale.
# print(sales + 20000)

# 8.	Double every sale.

# print(sales * 2)

# 9.	Display the first 5 sales.
# print(sales[0:6])

# 10.	Display the last 3 sales.
# print(sales[-3:])


# numbers = np.array([10,20,30,40,50])
# print(numbers)

# 14.	Print the first element of the array.
# print(numbers[0])


# 15.	Print the last element of the array.
# print(numbers[-1])

# 16.	Print the third element of the array.
# print(numbers[-3])

# 17.	Print the first three elements using slicing.
# print(numbers[:3])

# 18.	Print the last three elements using slicing.

# print(numbers[-3:])

# 19.	Create an array containing sales values: 12000, 18000, 15000, 22000, and 30000.

# sales_values = np.array([12000,18000,15000,22000,30000])
# 20.	Calculate the total of the sales array.
# print(np.sum(sales_values))

# 21.	Calculate the average of the sales array.
# average = np.average(sales_values)
# print("Avgerage:",average)

# 22.	Find the maximum sales value.
# Highest_value = np.max(sales_values)
# print("Highest Value:",Highest_value)

# 23.	Find the minimum sales value.
# Lowest_value = np.min(sales_values)
# print("Minimu Value:",Lowest_value)

# 24.	Calculate the standard deviation of the sales array.
# mean = np.std(sales_values)
# print("Mean:",mean)

# 25.	Add 2000 to every value in the sales array.

# Update_value = sales_values + 2000
# print("New Values:",Update_value)

# 26.	Subtract 1000 from every value in the sales array.
# deduction = sales_values - 1000
# print("New VAlues:",deduction)

# 27.	Multiply every sales value by 2.
# Update_values = sales_values * 2
# print("new values:",Update_values)

# 28.	Divide every sales value by 2.

# divide = sales_values / 2
# print("divieded Values:",divide)

# 29.	Create an array of five zeros.
# Arrray = np.zeros(5)
# print(Arrray)

# 30.	Create an array of five ones.
# One_arrays = np.ones(5)
# print(One_arrays)

# 31.	Create an array containing numbers from 1 to 10 using np.arange().
# numbers = np.arange(1,11)
# print(numbers)
# 32.	Create an array containing even numbers from 2 to 20.
# num = np.arange(2,21,2)
# print(num)

# 33.	Create an array containing numbers from 10 to 100 with a step of 10.
# num_array = np.arange(10,101,10)
# print(num_array)

# 34.	Using the sales array, display all sales greater than 15000.
# print(sales_values > 15000)

# 35.	Using the sales array, display all sales less than 20000.
# print(sales_values < 20000)

# 36.	Display all sales greater than or equal to 20000.
# print(sales_values >= 20000)

# 37.	Display all sales less than or equal to 15000.
# print(sales_values  <= 15000)

# 38.	Display all sales values between 15000 and 25000.
# result = sales_values[(sales_values >= 15000) & (sales_values <= 2000)]
# print(result)

# 39.	Count how many sales values are greater than 20000.

# count = np.sum(sales_values > 20000)
# print(count)

# 40.	Count how many sales values are less than 15000.
# count = np.sum(sales_values < 10000)
# print(count)

# 41.	Create an array of employee salaries: 35000, 42000, 55000, 60000, and 75000.
# emp_salary = np.array([35000, 42000, 55000, 60000, 75000])

# 42.	Find the average employee salary.
# Average = np.average(emp_salary)
# print("Avg Salary:",Average)

# 43.	Find the highest employee salary.
# highest_salary = np.max(emp_salary)
# print(highest_salary)

# 44.	Find the lowest employee salary.
# lowest_salary = np.min(emp_salary)
# print(lowest_salary)

# 45.	Show salaries greater than 50000.
# print(emp_salary > 50000)

# 46.	Add a 10% salary increment to every salary value.
# increment = emp_salary * 0.01 
# total = emp_salary + increment
# print(total)

# 47.	Create an array of product prices: 500, 750, 1200, 1500, and 2000.
# product_price = np.array([500,750,1200,1500,2000])

# 48.	Calculate the total product value.
# total = np.sum(product_price)
# print(total)

# # 49.	Calculate the average product price.
# Avg_product_price = np.average(product_price)
# print(Avg_product_price)

# 50.	Display product prices greater than 1000.
# print(product_price > 1000)

# 51.	Display product prices below 1000.
# print(product_price < 1000)

# 52.	Increase every product price by 5%.
# Increase_price = product_price * 0.05
# New_product_price = product_price + Increase_price
# print(Increase_price)
# print(New_product_price)

# 53.	Create an array of monthly sales: 10000, 15000, 12000, 18000, 22000, 25000, 30000.
# Monthly_sales = np.array([10000, 15000, 12000, 18000, 22000, 25000, 30000])

# 54.	Find the total monthly sales.
# Total = np.sum(Monthly_sales)
# print(Total)

# 55.	Find the average monthly sales.
# Avg_monthly_sales = np.average(Monthly_sales)
# print("Avg Mon Sales:",Avg_monthly_sales)

# 56.	Find the highest monthly sales value.
# Highest_monthly_sales =  np.max(Monthly_sales)
# print("Highest Monthly sales:",Highest_monthly_sales)

# 57.	Find the lowest monthly sales value.
# lowest_sales = np.min(Monthly_sales)
# print("Monthly lowest sales:",lowest_sales)

# 58.	Display sales values that are greater than the average sales.

# Avg_Monthly_sales = np.average(Monthly_sales)
# print(Avg_Monthly_sales)

# 59.	Display sales values that are below the average sales.
# Avg_Sales = np.average(Monthly_sales)
# print(Avg_Sales < Monthly_sales)

# # 60.	Create a complete NumPy sales analysis that prints total, average, maximum, minimum, and all sales above 20000.

# sales = np.array([
#     12000, 18000, 15000, 22000,
#     30000, 17000, 25000, 14000,
#     35000, 28000
# ])

# print("Total Sales:",np.sum(sales))
# print("Average Sales:",np.average(sales))
# print("highest Sales:",np.max(sales))
# print("Lowest sales:",np.min(sales))
# print("Difference:",sales > 20000)
