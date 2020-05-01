# a = 3
# b = 5
# if a==2:
#     print(f"yes the value of a is: {a}")
# else:
#     print(f"the value of a is not equal to 2, it is :{a}")
# if b==5:
#     print(f"yes you are correct. the value is a {b}")
# else:
#     print(f"no you make a mistake. the value must be {b}")    

# age = 31
# if age<50:
#     print("right")
# else:
#     print("wrong")
# if age!=50:        #!= means "is not equal"
#     print("right")
# else:
#     print("wrong")


# drinks = ["beer", "votka", "visky", "ayran", "water", "cola"]
# for drink in drinks:
#     if drink == 'beer':
#         print("i love "+ drink.upper())
#     elif drink == 'cola':
#         print(drink.upper()+" is an unhealty")
#     elif drink == 'visky':
#         print(drink.upper() + " is a very expensive")
#     elif drink == 'water':
#         print(drink.upper() + " is a healty")
#     else:
#         print(drink.title()+" is a turkish drink")

# mind = int(input("write one number between 0 to 100: "))
# print("Hold that number on your mind")
# number = 50
# if mind < number:
#     print("your number is between 0 to 50")
#     print("i guess your number: " + str(mind))
# elif mind > number and mind<=100:
#     print("your number is between 50 to 100")
#     print("i guess your number: "+ str(mind))
# else:
#     print("are you stupid baby. please next time write between 0 to 100")

# age = int(input("write your age: "))
# if age < 21 and age > 0:
#     print("Alcohol is not allowed for you")
# elif (age >=21) and (age < 110):  
#     print("you can buy alcohol bottle")
# else: 
#     print("you go fuck yourself! . Are you fucking kidding me!. Again write your age: ")
#     age = int(input("write your age: "))
#     if age < 21 and age > 0:
#         print("Alcohol is not allowed for you!")
#     elif (age >=21) and (age < 110):  
#         print("you can buy alcohol bottle")
#     else:
#         print("cancel your operation")

# cars = [ "toyota", "lexus",  "bmw", "audi", "mercedes" ]
# car = input("Enter your car: ")
# if car.lower() not in cars: #buyuk kucuk harf uyumu olsun diye koydum. (.lower)
#     print("Sorry we dont have " + car.upper())
# else: 
#     print(f"Yes we have {car.title()} in our show room")

# available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'cheese']

# requested_toppings = ['mushrooms', 'tomato', 'cheese']

# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print(f"Adding {requested_topping} topping to your pizza")
#     else:
#         print(f"Sorry we dont have {requested_topping} topping")

# available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'cheese']
# request1 = input("which first topping do you add for your pizza: ")
# request2 = input("which second topping do you add for your pizza: ")
# request3 = input("which third topping do you add for your pizza: ")
# requested_toppings = [request1.lower(), request2.lower(), request3.lower()]

# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print(f"Adding {requested_topping.upper()} topping to your pizza")
#     else:
#         print(f"Sorry we dont have {requested_topping.upper()} topping")