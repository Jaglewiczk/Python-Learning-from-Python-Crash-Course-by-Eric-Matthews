banned_users = ["Michalina", "Wiktoria", "Justyna", "Darek", "Halina", "Irena"]
authorized_users = ["Karol", "Justyna", "Fryderyk", "Paweł"]
user = input("Podaj swoje imię: ")
user = user.lower
if user in banned_users:
    print(f"{user}, niestety jesteś zablokowany, nie możesz opublikować komentarza")
else:
    print(f"{user}, opublikuj swój komentarz") 

if user == "Karol":
    print("Królu złoty!")

if user not in authorized_users and user in banned_users:
    print(f"Drogi/a {user}, nie możesz założyć konta")  
elif user not in authorized_users:
    print(f"Drogi/a {user}, załóż proszę konto!")
elif user in authorized_users:
    print(f"Witaj {user}!")
else:
    print(f"Witaj {user}, załóż konto!")

    


