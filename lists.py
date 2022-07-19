motorcycles = ["ducati", "suzuki", "yamaha"]
print(motorcycles)
print(motorcycles[1])
motorcycles.insert(0, "romet")          #wstawianie elementu listy razem z wartością w konkretnej pozycji
print(motorcycles)
del motorcycles[2]                      #usuwanie elementu listy 
print(motorcycles)
popped_motorcycles = motorcycles.pop()  #zapisywanie usuniętego elementu (bez wartości w nawiasach będzie to ostatni element listy) do zmiennej
print(popped_motorcycles)
print(motorcycles)
popped_motorcycles = motorcycles.pop(0) #zapisywanie usuniętego elementu listy do zmiennej
print("My first motorcycle was\t" + popped_motorcycles.title() + ".")
motorcycles.remove("ducati")            #usuwanie po wartości (STRING)
print(motorcycles)
motorcycles.append("ducati")
motorcycles.append("suzuki")
motorcycles.append("yamaha")
print(motorcycles)
