weight = 41.5

#Ground Shipping
if weight <= 2:
   cost_ground_shipping = weight * 1.50 + 20
elif weight <= 6: 
  cost_ground_shipping = weight * 3.00 + 20
elif weight <= 10:
  cost_ground_shipping = weight * 4.00 + 20
else:
  cost_ground_shipping = weight * 4.75 + 20

print("Ground Shipping: $", cost_ground_shipping)

#Premium Ground Shipping
cost_ground_premium = 125.00

print("Premium Shipping: $", cost_ground_premium)

#Drone Shipping
if weight <= 2:
  cost_drone_shipping = weight * 4.50
elif weight <= 6: 
 cost_drone_shipping = weight * 9.00
elif weight <= 10:
  cost_drone_shipping = weight * 12.00
else:
  cost_drone_shipping = weight * 14.25

print("Drone Shipping: $", cost_drone_shipping)