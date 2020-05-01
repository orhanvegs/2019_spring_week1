# no1 = 25
# no2 = 30
# no3 = 27
# no4 = 7
# sum = no1 + no2
# multiplication = no1 * no2
# division = no1 / no2
# modulo= no2 % no1 # ilk sayinin ikinci sayiya bolumunden KALAN sayiyi verir
# remainder = no2 // no1  # ilk sayinin ikinci sayiya bolumunden SONUC olan sayiyi verir
# remainder2 = no3 // no4
# print(sum)
# print(multiplication)
# print(division)
# print(modulo)
# print(remainder)
# print(remainder2)

# ***** END of Page, you can see modulo and reminder examples

# numbers >> integers, floats

# number1 = input("Enter your first number: ")
# number2 = input("Enter your second number: ")
# converting the old values of variables from string to integers
# number1 = int(input("Enter your first number: "))
# number2 = int(input("Enter your second number: "))

# operations with numbers
# sum = number1 + number2
# multiplication = number1 * number2
# division = number1 / number2
# # modulo
# remainder = number2 % number1
# remainder1 = number1 % number2

# division_floor = number2 // number1  # 30//25
# division_floor1 = number1 // number2  # 25//30

# print(sum)
# print(multiplication)
# print(division)
# print(remainder)
# print(remainder1)
# print(division_floor)
# print(division_floor1)

# using numbers with strings : using str() - converts numbers to strings, int() - converts strings to integers
# print("Sum of number1 and number2 is : " + str(sum))
# print("Sum of " + str(number1)+" and " + str(number2) + " is : " + str(sum))
# print("Multiplication of number1 and number2 is : " + str(multiplication))
# print(division)
# print(remainder)
# print(remainder1)
# print(division_floor)
# print(division_floor1)

# fstring 
# number1 = 12
# number2 = 15
# sum = 12 + 15
# print("**** using fstring ****************** ")
# print(f"Sum of {number1} and {number2} is : {sum}")
# print(f" {number1} minus {number2} is : {number1 - number2}")

# age = "25" # this is the string not integer
# print(age)
# age = int(age) + 12 #      age += 12
# print(age)
# age++ >> age = age + 1
# age-- >> age = age - 1

#modulo (%) -- ilk sayinin ikinci sayiya bolumunden KALANI verir.
# a=7
# b=2
# c=3
# d=4
# e=12
# d=27
# res= a % b
# res2= c % d
# res3= d % e
# res4= e % d
# print(res)  # 7 / 2 = 3 * 2 + 1 --- 7 % 2 = 3 R 1 = 1
# print(res2) # 3 / 4 = 0 * 4 + 3 --- 3 % 4 = 0 R 3 = 3
# print(res3) # 27 / 12 = 2 * 12 + 3 --- 27 % 12 = 2 R 3 = 3
# print(res4) # 12 / 27 = 0 * 27 + 12 --- 12 % 27 = 0 R 12 = 12

# remainder (//) -- ilk sayinin ikinci sayiya bolumunden SONUCU verir.
# a=7
# b=2
# c=3
# d=4
# e=12
# d=27
# tes= a // b
# tes2= c // d
# tes3= d // e
# tes4= e // d
# tes5= d // c
# print(tes)  # 7 / 2 = 3 * 2 + 1 --- 7 // 2 = 3 R 1 = 3
# print(tes2) # 3 / 4 = 0 * 4 + 3 --- 3 // 4 = 0 R 3 = 0
# print(tes3) # 27 / 12 = 2 * 12 + 3 --- 27 // 12 = 2 R 3 = 2
# print(tes4) # 12 / 27 = 0 * 27 + 12 --- 12 // 27 = 0 R 12 = 0
# print(tes5) # 27 / 3 = 9 * 3 + 0 --- 27 // 3 = 9 R 0 = 9

#convert string to integer and convert integer to string
# num1 = "12"
# num2 = "20"
# num3 = 15
# num4 = 22
# kan = int(num1) + int(num2)
# kan2 = num3 + num4
# kan3 = int(num1) + num4
# kan4 = str(int(num2) + num3)
# print(kan)
# print(kan2)
# print(kan3)
# print (kan4)

#  FIRST WAY
# say = int(input("Enter your first number: "))
# say2 = int(input("Enter your Second number: "))
# sum = say + say2
# print(str(say) + " " + "sum" + " " + str(say2) + " equal " + str(sum))

# #  SECOND WAY
# may = input("Enter your first number: ")
# may2 = input("Enter your Second number: ")
# sum2 = int(may) + int(may2)
# print( may + " " + "sum" + " " + may2 + " equal " + str(sum2))
# sum3 = str(int(may)+int(may2))
# print( may + " " + "sum" + " " + may2 + " equal " + sum3)