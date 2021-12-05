# Grocery problem
grocery =  (["fruit", "vegetables", "milk", "eggs", "meat"])

# Let's add cake on the grocery list 
grocery.add("cake") 
print(grocery)

# We have two lists but we want a union of both lists to remove duplicates
groceryA = (["fruit", "vegetables", "milk", "eggs", "meat"])
groceryB = (["milk", "bread", "soda"])

# Let's write the union operation
allGroceries = union(groceryA, groceryB)
print(allGroceries) 