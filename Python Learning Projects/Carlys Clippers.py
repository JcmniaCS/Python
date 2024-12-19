hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#Creating a variable for total price
total_price = 0

#Looping the prices list and adding each price to the variable total_price
for price in prices:
  total_price += price
print(total_price)

#Creating an average_price variable with the total_price divided by the length of the prices list
average_price = total_price / len(prices)
#print a string then convert average_price into a string and display it
print("Average Haircut Price:", str(average_price))

#Cutting prices by $5 using list comprehension and making a new list called new_prices

new_prices = [price -5 for price in prices]
#Print new_prices
print(new_prices)

#Creating a total_revenue variable
total_revenue = 0

#Creating for loop to create variable "i" that goes from 0 to len(hairstyles)
for i in range(len(hairstyles)):
  #The sum to change total_revenue to calculate the total revenue from last week.
  total_revenue += prices[i] * last_week[i]

  #printing total revenue
print("Total Revenue:", total_revenue)

#Creating variable "average_daily_revenue" Dividing total_revenue by 7 to achieve the daily revenue result.
average_daily_revenue = total_revenue / 7
print("Average Daily Revenue:", average_daily_revenue)

#Creating a new list called cuts_under_30 which will show all haircuts under 30 dollars.
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)

  





