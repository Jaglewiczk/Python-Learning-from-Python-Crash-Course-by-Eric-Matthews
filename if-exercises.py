alien_color = "zielony"
if alien_color == "zielony":
    print("Brawo, dostałeś 5 punktów za zestrzelenie!")
elif alien_color == "żółty":
    print("Brawo, dostałeś 10 punktów za zestrzelenie!")
else:
    print("Brawo, dostałeś 15 punktów!")
    
age = input("Wpisz swój wiek: ")
age = int(age)

if age < 2:
    print("Jesteś niemowlakiem!")
elif age >= 2 and age < 4:
    print("Jesteś dzieckiem, które uczy się chodzić!")
elif age >=4 and age < 13:
    print("Jesteś dzieckiem!")
elif age >= 13 and age < 20:
    print("Jesteś nastolatkiem!")
elif age >= 20 and age < 65:
    print("Jesteś dorosły!")
elif age >= 65:
    print("Jesteś seniorem!")
    
fruits = ["banana", "apple", "blueberry"]
if "banana" in fruits:
    print("You really like bananas!")
if "kiwi" in fruits:
    print("You really like kiwis!")
if "strawberry" in fruits:
    print("Your really like strawberries!")
if "apple" in fruits:
    print("You really like apples!")
if "blueberry" in fruits:
    print("You really like blueberries!")
for fruit in fruits:
    print(f"I'm adding {fruit} to your fruit salad!")
print("Your fruit salad is ready!")
for fruit in fruits:
    if fruit == "apple":
        print(f"Sorry, we don't have {fruit}, please choose another ingredient!")
    else:
        print(f"Adding {fruit} to your fruit salad!")
print("Your salad is ready!")

fruits = []

if fruits:
    for fruit in fruits:
        print(f"Dodaję {fruit} do sałatki!")
    print("Twoja sałatka jest gotowa")
else:
    print(f"Czy jesteś pewien, że chcesz zamówić sałatkę bez składników? :D")

