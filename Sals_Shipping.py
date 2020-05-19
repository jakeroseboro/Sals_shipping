#Defining functions to calculate the cheapest shipping option for this Mock Company
#Ground shipping cost
def ground_ship_cost(weight):
  if (weight >= 10):
    cost = ((weight * 4.75) + 20.00)
    return cost
  elif (weight >= 6):
    cost = ((weight * 4.00) + 20.00)
    return cost
  elif (weight >= 2):
    cost = ((weight * 3.00) + 20.00)
    return cost
  else: 
    cost = ((weight * 1.50) + 20.00)
    return cost

#Tesing the code
print(ground_ship_cost(8.40))

#Premium shipping cost
premium_shipping = 125.00

#Drone shipping cost
def drone_ship_cost(weight):
    if (weight >= 10):
      cost = (weight *14.25)
      return cost
    elif (weight >= 6):
      cost =(weight * 12.00) 
      return cost
    elif (weight >= 2):
      cost = (weight * 9.00)
      return cost
    else: 
      cost = (weight * 4.50) 
      return cost

#Testing the code
print(drone_ship_cost(1.5))

#Cheapest option
def cheapest_opt(weight):
  if (ground_ship_cost(weight) < drone_ship_cost(weight)) and (ground_ship_cost(weight) < premium_shipping):
    cost = ground_ship_cost(weight)
    print ("You should use ground shipping, it will cost you $" + str(cost) + ".")
  elif (drone_ship_cost(weight) < premium_shipping):
    cost = drone_ship_cost(weight)
    print ("You should use drone shipping, it will cost you $" + str(cost) + ".")
  else: 
    print ("You should use premium shipping, it will cost you $" + str(premium_shipping) + ".")

#Testing the code
cheapest_opt(41.5)#Ground shipping cost
def ground_ship_cost(weight):
  if (weight >= 10):
    cost = ((weight * 4.75) + 20.00)
    return cost
  elif (weight >= 6):
    cost = ((weight * 4.00) + 20.00)
    return cost
  elif (weight >= 2):
    cost = ((weight * 3.00) + 20.00)
    return cost
  else: 
    cost = ((weight * 1.50) + 20.00)
    return cost

#Tesing the code
print(ground_ship_cost(8.40))

#Premium shipping cost
premium_shipping = 125.00

#Drone shipping cost
def drone_ship_cost(weight):
    if (weight >= 10):
      cost = (weight *14.25)
      return cost
    elif (weight >= 6):
      cost =(weight * 12.00) 
      return cost
    elif (weight >= 2):
      cost = (weight * 9.00)
      return cost
    else: 
      cost = (weight * 4.50) 
      return cost

#Testing the code
print(drone_ship_cost(1.5))

#Cheapest option
def cheapest_opt(weight):
  if (ground_ship_cost(weight) < drone_ship_cost(weight)) and (ground_ship_cost(weight) < premium_shipping):
    cost = ground_ship_cost(weight)
    print ("You should use ground shipping, it will cost you $" + str(cost) + ".")
  elif (drone_ship_cost(weight) < premium_shipping):
    cost = drone_ship_cost(weight)
    print ("You should use drone shipping, it will cost you $" + str(cost) + ".")
  else: 
    print ("You should use premium shipping, it will cost you $" + str(premium_shipping) + ".")

#Testing the code
cheapest_opt(41.5)