def printList(lst, end = '\n'):
    for element in lst:
        print(element, end=end)


# Invoke the function
my_list = [3, 1, 2, 6, 4, 2]
printList(my_list, end = " ** ")

print('----------reversing---------')

def reversing(lst):
    result = []
    for element in lst:
        result.insert(0, element)
        return result
list1 = [1, 2, 3, 4, 5, 6]
list2 = reverse(list1)
print(list2)

reversing()