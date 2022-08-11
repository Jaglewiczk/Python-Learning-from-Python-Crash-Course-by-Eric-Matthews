pizzas = ["Margherita", "Pepperoni", "Capriciosa", "Hawaii", "Tonno", "Salami", "Diavola"]
for pizza in pizzas:
    print(f"I love {pizza.title()} pizza!")
print("I really love pizza!")

animals = ["dog", "cat", "horse"]
for animal in animals:
    print(f"{animal.title()} is a real friend to human!")
print("All these animals are lovely!")

for pizza in pizzas[:3]:
    print(f"Najlepsze pizze to: {pizza}")

for pizza in pizzas[2:5]:
    print(f"Średnie pizze to: {pizza}")
    
for pizza in pizzas[-3:]:
    print(f"Duże pizze to {pizza}")
    
friends_pizzas = pizzas[:]
pizzas.append("Servant")
friends_pizzas.append("Con Pollo")

print(f"Moje ulubione pizze to: {pizzas}")
print(f"Ulubione pizze Fryderyka to: {friends_pizzas}")

for friend_pizza in friends_pizzas:
    print(f"Fryderyk uwielbia: {friend_pizza}")

for pizza in pizzas:
    print(f"Moje ulubione to {pizza}")