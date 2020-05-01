# find the sum of the numbers using loops
# numbers = [1, 4, 5093, 32444, 2200, 122]
# sum = 0
# for number in numbers:
#     sum = sum + number
#     print(sum)
# print(f"Total of the numbers : {sum}")

# # print the given string with double characters
# word = input("Enter the word :")
# # letter = word
# double_letter_word = ""

# for letter in word:
#     # double_letter = letter*2
#     double_letter_word = double_letter_word + letter*2
#     print(letter*2)

# print(double_letter_word)

number = '45783'
double_number = ""
triple_number = ""
double_number_all = ""
triple_number_all = ""
for one in number:
    double_number = one * 2
    triple_number = one * 3
    double_number_all = double_number_all + one * 2
    triple_number_all = triple_number_all + one * 3
    print(one)
    print(double_number)
    print(triple_number)
print (double_number_all)
print(triple_number_all)