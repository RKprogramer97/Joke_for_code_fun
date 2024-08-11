#dict

manu = {
    'Burgar':48,
    'Pizza': 84,
    'pasta': 67, 
    'solid': 75, 
    'coffee': 80,
}

#Great
print("welcome to PYTHON Resturent,  Here's manu")

#Show manu of buyer
print('Burgar: Rs40\nPizza: Rs84\npasta: Rs67\nsolid: Rs75\ncoffee: Rs80')

order_total = 0
#80 + 50 = 130


item_1 = input("Enter the item You want to buy: ")
if item_1 in manu:
    order_total += manu[item_1]
    print(f"Your item{item_1} has been added in your order")
else:
    print(f"ordered ite {item_1} is not Availabel yet")