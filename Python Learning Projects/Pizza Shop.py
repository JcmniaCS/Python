# Your code below:
#List of toppings/pizzas available
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
#print(toppings)

#List of prices for each pizza slice
prices = [2, 6, 1, 3, 2, 7, 2]
#print(prices)

#Counting how many pizza slices cost $2
num_two_dollar_slices = prices.count(2)
#print(num_two_dollar_slices)

#Counting how many different pizza slices there are
num_pizzas = len(toppings)
#print(num_pizzas)

#String to print to show how many different kinds of pizza are sold
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

#Creating a 2D list with both pizzas and prices included following the specified format [price, topping_name]
pizza_and_prices = [
  [2, "Pepperoni"], [6, "Pineapple"], [1, "Cheese"], [3, "Sausage"], [2, "Olives"], [7, "Anchovies"], [2, "Mushrooms"]
]
#print (pizza_and_prices)

#Sorting the 2D list so that the prices are in ascending order.
pizza_and_prices.sort()
#print (pizza_and_prices)

#Storing the first element of pizza_and_prices aka the cheapest pizza.
cheapest_pizza = pizza_and_prices[0]
#print(cheapest_pizza)

#Storing the last element of pizza_and_prices aka the most expensive pizza.
priciest_pizza = pizza_and_prices[6]
#print(priciest_pizza)

#Removing "anchovies" from pizza_and_prices list, the last customer bought the last slice.
pizza_and_prices.pop()
#print(pizza_and_prices)

#Adding a new topping to keep customers excited

pizza_and_prices.insert(4, [2.5, "Peppers"])
#print(pizza_and_prices)

#Some customers come to the shop and ask for 3 different pizza slices but the cheapest slices.
three_cheapest = pizza_and_prices[0:3]
print(three_cheapest)




