
""" Create a list containing duplicate numbers.Convert it to a set to remove the duplicates,then
convert it back into a list """

list1 = [1,2,3,5,8,35,23,98,65,2,35,1]
print("The list is :",list1)

set1 = set(list1)
print("The set is:",set1)

list2 = list(set1)
print("From set to again list:",list2)