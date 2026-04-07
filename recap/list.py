fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

# --- IGNORE ---

fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)

fruits.append('grape')
print(fruits)

fruits.insert(2, 'mango')
print(fruits)

fruits.remove('banana')
print(fruits)

fruits.pop()
print(fruits)

fruits.reverse()
print(fruits)

index = fruits.index('apple')
print("index:", index)