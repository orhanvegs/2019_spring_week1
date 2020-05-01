# counter = 0
# while counter < 10:
#     print(counter)
#     counter = counter + 1

# infinte loop = if you wanna exit to push; ctrl+C
# var = 1
# while var == 1:  # This constructs an infinite loop
#     number = input("Bir numara girin: ")
#     print("Sizin girdiginiz numara: ", number)

# sayac = 10
# while sayac >= 1:
#     print(sayac)
#     sayac = sayac - 1

# a = int(input("write first number: "))
# b = int(input("write second number: "))
# c = 0
# while a <= b:
#     c = (a + b) * b
#     print(c)
#     a = a + 1
# else:
#     print("execute app again")

# msg = ""
# while msg.lower() != "quit" :
#     print(msg.upper())
#     msg = input("Enter your word, i will repeat that for you: ")


while True :
    msg = input("Enter your word, i will repeat that for you: ")
    print(msg.upper())
    if msg.lower() == "quit" :
        print("your word is quit. you can go home")
        break