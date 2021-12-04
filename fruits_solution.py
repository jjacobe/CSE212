fruits = []

# Let's enqueue some fruits into our list
fruits.append('chocolate')
fruits.append('apple')
fruits.append('banana')
fruits.append('orange')

# Chocolate isn't a fruit, dequeue it by adding code below
first_item = fruits.pop(0)
print(first_item)

# Dequeue again to remove 'apple'
first_item = fruits.pop(0)
print(first_item)

# 'banana' and 'orange' should be left in the queue
print(fruits)
