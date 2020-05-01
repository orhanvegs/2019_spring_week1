# cars = ["toyota","lexus",  "bmw", "merc" ]

# print(cars)
# # accessing the list 
# print("first element of cars list: " + cars[0])
# print("second element of cars list: " + cars[1])
# print("third element of cars list: " + cars[2])
# print("fourth element of cars list: " + cars[3])
# print("last element of cars list: " + cars[-1])
# print("second element from last of cars list: " + cars[-2])
# # IndexError expected "list index out of range"
# # print("fourth element of cars list: " + cars[4])

# # adding elements to the list >> append()
# cars.append("range rover")
# print(cars)
# cars.append("mazda")
# print(cars)
# print("fifth element of cars list: " + cars[4])
# print("sixth element of cars list: " + cars[5])

# # modifying, replacing the element on certain index
# # cars[3] = "bentley"
# cars.extend("bentley")
# print(cars)
# # cars[0] = "ram"
# cars.extend("ram")
# print(cars)

# # deleting the elements by index
# del cars[0]
# print(cars)

# del cars[-9:]
# print(cars)

# # adding an element to a specific position
# cars.insert(0, "audi")
# print(cars)
# cars.insert(3, "tesla")
# print(cars)

# # remove() deleting the element from the list using the value
# cars.remove("range rover")
# print(cars)

# # pop() removes last element and returns the value
# sold_cars = [] # empty list
# sold_cars.append(cars.pop())  # adding the removed car to the end of the new list
# sold_cars.insert(0, cars.pop()) # adding the removed car to the beginning of the new list

# # adding the removed car(first car in the list) to the beginning of the new list
# sold_cars.insert(0, cars.pop(0))

# print(sold_cars) 
# print(cars)

# # organize your lists
# # sort() 
# # cars.sort() # list is sorted in ascending order
# # cars.sort(reverse=True)  # list is ordered in descending order

# sorted_cars = sorted(cars)
# print(cars)
# print(sorted_cars)
# sorted_cars_desc = sorted(cars, reverse=True)
# print(sorted_cars_desc)
# print(cars)

# cars.reverse() # does not apply ordering asc or desc, it just reverses the list
# print(cars)

# copying the list ----------------

# cars.append("moskvish")
# print(cars)
# print(new_cars)

# new_cars_copy = cars[:] # copying the list and creating independent new_cars_copy list
# cars.append("lada")
# print(cars)
# print(new_cars)
# print(new_cars_copy)


# orhan --- orhan ---- orhan -- work on project
animals = ["frog", "bat", "horse", "cat"]
# print(animals)
# print("first element of animals list: " + animals[0].upper())
# print("second element of animals list: " + animals[1])
# print("third element of animals list: " + animals[2])
# print("fourth element of animals list: " + animals[3])
# print("last element of animals list: " + animals[-1])
# print("second element from last of animals list: " + animals[-2])
# #print("fourth element of animals list: " + animals[4]) #indexError? list index out of range (error message)

# animals.append("lion")
# print(animals)
# animals.append("dog")
# print(animals)

# animals[3]= "bird"
# animals.extend("bird")
# print(animals)

# animals[0]="tiger"
# animals.extend("tiger")
# print(animals)

# del animals[0]
# print(animals)
# del animals[-1]
# print(animals)

# animals.insert(1, "fish")
# print(animals)
# animals.insert(3, "monkey")
# print(animals)

# animals.remove("bat")
# print(animals)
# print(str(animals).upper())

# died_animals = []
# # died_animals.append(animals.pop())
# # print(died_animals)
# died_animals.insert(0, animals.pop())
# print(died_animals)

# animals.sort()
# print(animals)
# animals.sort(reverse=True)
# print(animals)

# a= sorted(animals)
# b= sorted(animals, reverse=True)
# print(animals)
# print(a)
# print(b)

# print(animals)
# animals.reverse()
# print(animals)

print(animals)
animals.append("lion")
new_animals = animals
print(animals)
print(new_animals)
new_animals_copy= animals[:]
print(new_animals_copy)
animals.append("snake")
print(animals)
print(new_animals)
print(new_animals_copy)