guest = ["orhan", "ozan", "alican", "Egemen"]
invitation = ",\n happy to invite you to my birhtday party at my garden.\n"

# print(invitation)
# print(guest[0] + invitation)
# print(guest[1] + invitation)
# print(guest[2] + invitation.upper())
# print(guest[3].upper() + invitation)

# guest.insert(0, "serdar")
# guest_couldnt_come = []
# guest_couldnt_come.append(guest.pop(0))
# print(guest_couldnt_come)
# print("Some guests can not come.\n\tguests can not come to my birthday party  " + guest_couldnt_come[0].upper())
# print(guest[0].title() + invitation)
# print(guest[1].title() + invitation)
# print(guest[2].title() + invitation)
# print(guest[3].title() + invitation)

### ---------- POP ---------- #### HOW TO USE
# classroom = ["osman","mehmet","ahmet","Suleyman","ali"]
# print(classroom)
# classroom.insert(0, "veli")
# print(classroom)
# absent = []
# absent.append(classroom.pop(0))
# print(absent)
# print(classroom)
# absent.append(classroom.pop(2))
# print(absent)
# print(classroom)

for person in guest:
    print(person + invitation)

number_of_guest = len(guest)
print(f"we will be {number_of_guest} people to night")
print(f"\twe will be {len(guest)} people to night")
