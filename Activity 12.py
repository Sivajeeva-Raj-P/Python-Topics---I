
"""List: Given a list of fruits,add one fruit to the end,remove one fruit,and display the final list and also,display
the first five and last 3 elements without slicing."""

Fruits = ["apple","banana","cherry","orange","grapes","pomegranate","mango","custard","rambutan"]

print("List of fruits:",Fruits)

#add one fruit to the end
Fruits.append("kiwi")
print("After adding one fruit:",Fruits)

#Remove one fruits
Fruits.pop(0)
print("After removing first fruit:",Fruits)

#display first 5 and last 3 elements
print("The first 5 elements:",Fruits[:5])
print("The last 3 elements are:",Fruits[-3:])
