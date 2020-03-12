# # from string import ascii_lowercase
# # print(ascii_lowercase)  # abcdefghijklmnopqrstuvwxyz
# #
# # # Open file for writing data
# # file_to_open = open("file.txt", "w")
# # file_to_open.write(ascii_lowercase)
# #
# # create_dict = {}
# #
# #----------------from course slides--------
# from string import ascii_lowercase
# from pprint import pprint
#
# def main():
#     filename = input("Enter a filename: ").strip()
#     dict_of_letter = {}
#     f = open(filename)
#     for line in f:
#         for letter in line.lower():
#             if letter in ascii_lowercase:
#                 if letter in dict_of_letter:
#                     dict_of_letter[letter] += 1
#                 else:
#                     dict_of_letter[letter] = 1
#     f.close()
#     pprint(dict_of_letter)
#
# main()
# #----------------from course slides--------
#

#------------in the lesson----------
from string import ascii_lowercase
print(ascii_lowercase)  # abcdefghijklmnopqrstuvwxyz

def main():
    my_file = input('enter file name: ')
    infile = open(my_file, 'r')
    my_str = infile.read()
    letter = {}

    for l in my_str.lower():
        if l in ascii_lowercase:
            if l  in letter:
                letter[l] += 1
            else:
                letter[l] = 1
    print(letter)

main()
#------------in the lesson----------