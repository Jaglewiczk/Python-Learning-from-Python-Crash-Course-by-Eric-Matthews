from math import fabs


alien_0 = {}
alien_0["color"] = "czerwony"
alien_0["points"] = 5
print(alien_0)
alien_0["color"] = "żółty"
print(f"Kolor obcego to teraz {alien_0['color']}")
alien_0["x position"] = 0
alien_0["y position"] = 3
alien_0["speed"] = "szybko"
if alien_0["speed"] == "wolno":
    speed_move = 1
elif alien_0["speed"] == "średnio":
    speed_move = 2
elif alien_0["speed"] == "szybko":
    speed_move = 3
alien_0["x position"] = alien_0["x position"] + speed_move
print(alien_0)
del alien_0["color"]
print(alien_0)

favourite_languages = {
    "jan": "C",
    "karol": "python",
    "justyna": "ruby",
    "paweł": "python"
}
favourite_language = favourite_languages["karol"]
print(f"Ulubionym językiem Karola jest {favourite_language}")

third_position = alien_0.get("z position", "Nie jest przypisana pozycja z!")
print(third_position)
alien_0["z position"] = 23
third_position = alien_0.get("z position", "Nie jest przypisana pozycja z!")
print(third_position)

for name, favourite_language in favourite_languages.items():
    print(f"Ulubionym językiem programowania {name} jest {favourite_language}")

for name in favourite_languages.keys():    # może być bez .keys!!! Szukanie po kluczach jest domyślne.
    print(name.title())


