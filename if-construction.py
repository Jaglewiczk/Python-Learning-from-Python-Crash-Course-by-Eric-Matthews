banned_users = ["Michalina", "Wiktoria", "Justyna", "Darek", "Halina", "Irena"]
authorized_users = ["Karol", "Justyna", "Fryderyk", "Paweł"]
banned_users_2 = banned_users[:]
for banned_user_2 in banned_users_2:
    banned_user_2.lower
authorized_users_2 = authorized_users[:]
for authorized_user_2 in authorized_users:
    authorized_user_2.lower
user = input("Podaj swoje imię: ")
if user.title() in banned_users:
    print(f"{user}, niestety jesteś zablokowany, nie możesz opublikować komentarza")
else:
    print(f"{user}, opublikuj swój komentarz") 

if user.lower() == "Karol":
    print("Królu złoty!")

if user.title() not in authorized_users and user.title() in banned_users:
    print(f"Drogi/a {user}, nie możesz założyć konta")  
elif user.title() not in authorized_users:
    print(f"Drogi/a {user}, załóż proszę konto!")
    new_user = input(f"Wpisz swoje imię: ")
    new_user = new_user.title()
    if new_user in authorized_users or new_user in authorized_users_2:
        print(f"Nazwa użytkownika {new_user} została już zarezerwowana!")
    else:
        authorized_users.append(new_user)
elif user.title() in authorized_users:
    print(f"Witaj {user}!")
else:
    print(f"Witaj {user}, załóż konto!")

print(authorized_users)

print("Mateusz" in authorized_users)
print("Karol" in authorized_users)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")



  


