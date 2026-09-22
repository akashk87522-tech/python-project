order_id = ["R001","R002","R003","R004","R005","R006","R007","R008","R009","R010","R011","R012","R013","R014","R015"]
customer = ["Rahul","Priya","Amit","Neha","Arjun","Sneha","Rohan","Anjali","Vikas","Pooja","Karan","Simran","Aditya","Nisha","Varun"]
food_item = ["Biryani","Pizza","Burger","Biryani","Pasta","Pizza","Burger","Pasta","Biryani","Pizza","Burger","Pasta","Biryani","Burger","Pizza"]
category = ["Main Course","Main Course","Fast Food","Main Course","Main Course","Main Course","Fast Food","Main Course","Main Course","Main Course","Fast Food","Main Course","Main Course","Fast Food","Main Course"]
quantity = [2,1,3,4,2,2,1,3,5,2,4,2,3,2,3]
selling_price = [300,550,220,300,350,550,220,350,300,550,220,350,300,220,550]
cost_price = [180,350,130,180,210,350,130,210,180,350,130,210,180,130,350]
payment_method = ["UPI","Card","UPI","Cash","Card","UPI","Card","UPI","Cash","Card","UPI","Card","UPI","Cash","Card"]
order_status = ["Completed","Completed","Cancelled","Completed","Completed","Completed","Completed","Cancelled","Completed","Completed","Completed","Completed","Cancelled","Completed","Completed"]


# . Create all dataset lists exactly as supplied.

# print(order_id)
# print(customer)
# print(food_item)
# print(category)
# print(quantity)
# print(selling_price)
# print(cost_price)
# print(payment_method)
# print(order_status)

# . Print all order IDs.

# print(order_id)

# Print all food items.

# print(food_item)

# Print all customers in uppercase.

# for name in customer:
#     print(name.upper())

# . Print all customers in lowercase.

# for name in customer:
#     print(name.lower())

# 6. Find the total number of orders.

# print(len(order_id))

# Find the total quantity ordered.

# print(sum(quantity))

# Calculate revenue for every order using quantity × selling price.

# for i in range(len(order_id)):
#     revenue = quantity[i] * selling_price[i]
#     print(order_id[i],revenue)

# Calculate cost for every order using quantity × cost price.

# for i in range(len(order_id)):
#     cost = quantity[i] * cost_price[i]
#     print(order_id[i],cost)

# Calculate profit for every order.

# for i in range(len(order_id)):
#     profit = selling_price[i] - cost_price[i]
#     print(order_id[i],profit)

# . Calculate profit margin percentage for every order.

# for i in range(len(order_id)):
#     revenue = quantity[i] * selling_price[i]
#     profit = quantity[i] * (selling_price[i] - cost_price[i])
#     profit_margin = profit / revenue * 100
#     print(order_id[i], round(profit_margin, 2), "%")

# for i in range(len(order_id)):
#     profit_margin = ((selling_price[i]-cost_price[i])/selling_price[i] * 100)
#     print(order_id[i],profit_margin)


# Print only Completed orders.

# for i in range(len(order_id)):
#    if order_status [i]== "Completed":
#     print(order_id[i],food_item[i])

# Count Completed orders.
# count = 0

# for i in range(len(order_id)):
#     if order_status[i]== "Completed":
#         count += 1 
# print(count)
    
# Count Cancelled orders.
# count = 0

# for i in range(len(order_id)):
#     if order_status[i]== "Cancelled":
#         count+= 1
# print(count)

# Calculate total revenue from Completed orders only.
# total_revenue= 0

# for i in range(len(order_id)):
#     if order_status[i]== "Completed":
#         revenue = quantity[i] * selling_price[i]
#         total_revenue+= revenue
# print(total_revenue)

# Calculate total profit from Completed orders only.
# total_profit = 0

# for i in range(len(order_id)):
#     if order_status[i]== "Completed":
#         profit = selling_price[i] - cost_price[i]
#         total_profit += profit
# print(total_profit)


# Find the highest-profit order
# highest_profit = 0
# highest_order = ""

# for i in range(len(order_id)):
#     profit = quantity[i] * (selling_price[i] - cost_price[i])

# profit > highest_profit
# highest_profit = profit
# highest_order = order_id[i]

# print(highest_order,highest_profit)

# Find the lowest-profit order.

# lowest_profit = float("inf")
# lowest_order = ""

# for i in range(len(order_id)):
#     profit = quantity[i] * (selling_price[i] - cost_price[i])

#     if profit < lowest_profit:
#        lowest_profit = profit
#        lowest_order = order_id[i]

# print(lowest_order,lowest_profit)

# . Find all orders with profit margin >= 40%.

# for i in range(len(order_id)):
#     profit = quantity[i] * (selling_price[i] - cost_price[i])
#     revenue = quantity[i] * selling_price[i]
#     profit_margin = profit / revenue * 100

#     if profit_margin >= 40:

#      print(order_id[i],round(profit_margin,2),"%")

# Find all orders with profit margin below 10%.

# for i in range(len(order_id)):
#     profit = quantity[i] * (selling_price[i] - cost_price[i])
#     revenue = quantity[i] * selling_price [i]
#     profit_margin = profit / revenue * 100

#     if profit_margin < 40:
#         print(order_id[i],round(profit_margin,2),"%")

# Create a list of all Biryani orders.

# biryani_list = []

# for i in range(len(order_id)):
#     if food_item[i]=="Biryani":
#         biryani_list.append(order_id[i])
# print(biryani_list)

# 22. Calculate total quantity of Biryani ordered.
# biryani_order = []

# for i in range(len(order_id)):
#     if food_item[i] == "Biryani":
#         biryani_order.append(order_id[i])
# print(len(biryani_order))

# Calculate total revenue from Pizza.
# total_revenue = 0
# for i in range(len(order_id)):
#     if food_item[i] == "Pizza":
#         pizza_revenue = quantity[i] * selling_price[i]
#         total_revenue += pizza_revenue
# print(total_revenue)


# Calculate total revenue from Burger.
# total_revenue = 0

# for i in range(len(order_id)):
#     if food_item[i] == "Burger":
#         burger_revenue = quantity[i] * selling_price[i]
#         total_revenue += burger_revenue
# print(total_revenue)

# 25. Calculate total revenue from Pasta.
# total_revenue = 0

# for i in range(len(order_id)):
#     if food_item[i] == "Pasta":
#         pasta_revenue = quantity[i] * selling_price[i]
#         total_revenue += pasta_revenue
# print(total_revenue)

# 26. Find customers who paid using Card.

# for i in range(len(order_id)):
#     if payment_method[i] == "Card":
#         print(order_id[i],"Card")

# 27. Find customers who paid using UPI.

# for i in range(len(order_id)):
#     if payment_method[i] == "UPI":
#         print(order_id[i], "upi payment")

# 28. Find customers whose order amount is above the average order revenue.
# revenue = []

# #find first total revenue
# for i in range(len(order_id)):
#     total_revenue = quantity[i] * selling_price[i]
#     revenue.append(total_revenue)
# # calculate the average revenue second
# avg_revenue = sum(revenue) / len(revenue)

# #compare thecustomer revenue with the average revenue 
# for i in range(len(order_id)):
#     if revenue[i] > avg_revenue:
#         print(customer[i],revenue[i],"Average revenue : ", round(avg_revenue,2))

# 29. Create a function calculate_revenue(quantity, price).

# def calculate_revenue(price,quantity):
#     revenue = price * quantity
#     return revenue
# calculate_revenue

# print(calculate_revenue(300,5))


# 30. Create a function calculate_cost(quantity, cost_price).

# def calculate_cost(quantity,cost_price):
#     total_cost = quantity * cost_price
#     return total_cost
# calculate_cost
# print(calculate_cost(5,66))

# Create a function calculate_profit(revenue, cost).

# def calculate_profit(revenue,cost):
#     profit = revenue - cost
#     return profit
# calculate_profit
# print(calculate_profit(1000,642))

# 32. Create a function calculate_margin(profit, revenue).

# def calculate_margin(profit,revenue):
#     margin = profit / revenue * 100
#     return margin 
# calculate_margin
# print(calculate_margin(1200,2000),"%")

# 33. Create a function profit_category(margin).

# def profit_category(margin):
#     if margin >= 40:
#         return "High Profit"
#     elif margin >= 20:
#         return "Medium Profit"
#     else:
#         margin < 20
#         return "Low Profit"
# profit_category
# print(profit_category(10))

# 34. Use the function to classify every order.

# def classify_orders(orders):
#     if orders > 10:
#         return "High order"
#     else:
#         orders > 5
#         return "Not Bad But can Improvement"
# classify_orders
# print(classify_orders(11))

# 35. Create separate High/Medium/Low profit lists.
# high_profit = []
# medium_profit = []
# low_profit = []

# for i in range(len(order_id)):
#     profit = selling_price[i] - cost_price [i]
#     revenue = quantity[i] * selling_price[i]
#     margin = profit / revenue * 100

#     if margin >= 40:
#         high_profit.append(order_id[i])
#     elif margin >= 20:
#         medium_profit.append(order_id[i])
#     else:
#         low_profit.append(order_id[i])
# print("high profit",high_profit)
# print("medium profit",medium_profit)
# print("Low Profit",low_profit)
        
# 36. Find the food item with the highest total quantity.
# burger = 0
# pasta = 0 
# biryani = 0
# pizza = 0

# for i in range(len(food_item)):
#     if food_item[i] == "Biryani":
#         biryani += quantity[i]
#     elif food_item[i] == "Pizza":
#         pizza += quantity[i]
#     elif food_item[i]== "Pasta":
#         pasta += quantity[i]
#     else:
#         food_item[i] == burger
#         burger += quantity[i]
# print("Biryani",biryani)
# print("Pizza",pizza)
# print("pasta",pasta)
# print("Burger", burger)

# print("Highest: ", max(pizza,burger,pasta,biryani,))

# 37. Find the food item with the highest total revenue.

# burger_revenue = 0
# pizza_revenue = 0
# pasta_revenue = 0
# biryani_revenue = 0

# for i in range(len(food_item)):
#     revenue = quantity[i] * selling_price[i]

#     if food_item[i]== "Biryani":
#         biryani_revenue += revenue
#     elif food_item[i] == "Pasta":
#         pasta_revenue += revenue
#     elif food_item[i] == "Pizza":
#         pizza_revenue += revenue
#     else:
#         food_item[i] == "Burger"
#         burger_revenue += revenue

# print("Biryani: ", biryani_revenue)
# print("Pasta", pasta_revenue)
# print("Burger",burger_revenue)
# print("Pizza", pizza_revenue)


# 38. Find the customer who generated the highest successful revenue.
# highest_revenue = 0
# highest_customer = ""


# for i in range(len(order_id)):
#     if order_status[i] == "Completed":
#         revenue = quantity[i] * selling_price[i]

#         if revenue > highest_revenue:
#             highest_revenue = revenue
#             highest_customer = customer[i]
# print("Customer: ",highest_customer)
# print("revenue", highest_revenue)


# 40. Read the same order data from a text file and convert numeric values safely.

with open("order.txt","r") as file:

    for line in file:
        data =line.strip().split(",")



        try:
            quantity = int(data[3])
            selling_price = float(data[4])
            cost_price = int(data[5])


    
    