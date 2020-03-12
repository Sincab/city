# # list1 = [x for x in range(0, 5)]
# # # print(list1)
# # # list2 = [0.5 * x for x in list1]
# # # print(list2)
# # # list3 = [x for x in list2 if x < 1.5]
# # # print(list3)
# # #
# # # print('=-------------------------- ')
# # #
# # # in_string = input('Enter a date: ')
# # #
# # # list1 = list(in_string)
# # #
# # # list2 = in_string.split('/')
# # #
# # # list3 = [int(x) for x in list2]
# # #
# # # entered_string = '/'.join(list2)
# # #
# # # print(list1)
# # # print(list2)
# # # print(list3)
# # # print(entered_string)
# # #
# # # #proper copying
# # # list2 = [x for x in list1]
# # # list2 = list1[:]
# # # list2 = list(list1)
# # # list2 = list(list1)
# # # import copy
# # # list2 = copy.copy(list1)
# # # list2 = copy.deepcopy(list1) # will copy the object as well
# # #
# #
# # def printGrade(score):
# #     # Print grade for the score
# #     if score >= 90.0:
# #         print('A')
# #     elif score >= 80.0:
# #         print('B')
# #     elif score >= 70.0:
# #         print('C')
# #     elif score >= 60.0:
# #         print('D')
# #     else:
# #         print('F')
# #
# # def main():
# #     score = eval(input("Enter a score: "))
# #     print("The grade is ", end = "")
# #     printGrade(score)
# #
# # main() # Call the main function
# # def getGrade(score):
# #     # Return the grade for the score
# #     if score >= 90.0:
# #         return 'A'
# #     elif score >= 80.0:
# #         return 'B'
# #     elif score >= 70.0:
# #         return 'C'
# #     elif score >= 60.0:
# #         return 'D'
# #     else:
# #         return 'F'
# #
# # def main():
# #     score = eval(input("Enter a score: "))
# #     print("The grade is", getGrade(score))
# #
# # main() # Call the main function

# def main():
# 2	    x = 1
# 3	    print("Before the call, x is", x)
# 4	    increment(x)
# 5	    print("After the call, x is", x)
# 6
# 7	def increment(n):
# 8	    n += 1
# 9	    print("n inside the function is", n)
# 10
# 11	main() # Call the main function
