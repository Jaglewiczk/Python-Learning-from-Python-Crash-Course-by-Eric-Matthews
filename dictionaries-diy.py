karols_data = {"first_name": "Karol", "last_name": "Nowak", "city": "Warszawa", "age": 34}
print(f"Dane osoby:\n{karols_data['first_name']}\n{karols_data['last_name']}\n{karols_data['city']}\n{karols_data['age']}")
fav_numbers = {"Karol": 11, "Justyna": 1, "Teresa": 33, "Zbyszek": 21, "Andrzej": 33}
print(f"Ulubiona liczba Karola to {fav_numbers['Karol']}")
print(f"Ulubiona liczba Justyny to {fav_numbers['Justyna']}")
print(f"Ulubiona liczba Teresy to {fav_numbers['Teresa']}")
print(f"Ulubiona liczba Zbyszka to {fav_numbers['Zbyszek']}")
print(f"Ulubiona liczba Andrzeja to {fav_numbers['Andrzej']}")

glosariusz = {"iteracja": "iteracja to przechodzenie przez pętlę na pewnych warunkach", "słownik": "para wartość-klucz"}
print(f"Iteracja: {glosariusz['iteracja'].capitalize()}")
print(f"Słownik: {glosariusz['słownik'].capitalize()}")

for key, value in karols_data.items():
    print(f"Klucz: {key}")
    print(f"Wartość: {value}")
