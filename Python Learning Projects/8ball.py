#Enter the weight of the product
weight = input("What is the total weight of product?")
weight = float(weight)

#Ground Shipping Price
cost_ground = ""
if weight <= 2.00 and weight >= 0:
  cost_ground = weight * 1.5 + 20.0
  print ("Total cost with Ground Shipping: " + str(cost_ground))

elif weight >= 2.01 and weight <= 6.00 :
  cost_ground = weight * 3 + 20
  print ("Total cost with Ground Shipping: " + str(cost_ground))

elif weight >= 6.01 and weight <= 10.00 :
  cost_ground = weight * 4 + 20
  print ("Total cost with Ground Shipping: " + str(cost_ground))

elif weight >= 10.01:
  cost_ground = weight * 4.75 + 20
  print ("Total cost with Ground Shipping: " + str(cost_ground))
else:
  print("Invalid weight. Please enter a positive number.")

#Ground Shipping Premium Price
cost_ground_prem = 125
print("Total cost with Ground Shipping Premium: " + str(cost_ground_prem))

#Drone Shipping Price
cost_drone = ""

if weight <= 2.00 and weight >= 0:
  cost_drone = weight * 4.5
  print("Total cost with Drone Shipping: " + str(cost_drone))

elif weight >= 2.01 and weight <= 6.00 :
  cost_drone = weight * 9
  print("Total cost with Drone Shipping: " + str(cost_drone))

elif weight >= 6.01 and weight <= 10.00 :
  cost_drone = weight * 12
  print("Total cost with Drone Shipping: " + str(cost_drone))

elif weight >= 10.01:
  cost_drone = weight * 14.25
  print("Total cost with Drone Shipping: " + str(cost_drone))

else:
  print("Error")



# Determine the cheapest shipping method
cheapest_method = min(cost_ground, cost_ground_prem, cost_drone)
if cheapest_method == cost_ground:
    print("Ground Shipping is the cheapest method.")
elif cheapest_method == cost_ground_prem:
    print("Ground Shipping Premium is the cheapest method.")
else:
    print("Drone Shipping is the cheapest method.")