# A string is a palindrome if it is identical forward and backward. For example “anna”, “civic”,
# “level” and “hannah” are all examples of palindromic words. Write a program that reads a
# string from the user and uses a loop to determine whether
# or not it is a palindrome. Display the result, including a meaningful output message.

#line = input('Enter a string: ')

x = 'sinan'

print(x)

x1 = x.splitlines()

str="Python" # initial string
stringlength=len(str) # calculate length of the list
slicedString=str[stringlength::-1] # slicing
print (slicedString) # print the reversed string


line = input('Enter a string: ')



for i in range(0, len(line) // 2):
    if line[i] != line[len(line) - 1 - i]:
        is_palindrome = False
        break

if is_palindrome:
    print(line, "is a palindrome")
else:
    print(line, "is not a palindrome")

