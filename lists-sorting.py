guest_list = ["Aleksandra", "Justyna", "Fryderyk"]
print("Zapraszam Cię na obiad " + guest_list[0])
print("Zapraszam Cię na obiad " + guest_list[1])
print("Zapraszam Cię na obiad " + guest_list[2])
print(guest_list[0] + " nie może przyjść.")
guest_list[0] = "Monika"
print("Znaleźliśmy większy stół! Wobec tego zwiększymy liczbę Gości.")
guest_list.insert(0, "Julia")
guest_list.insert(2, "Sławek")
guest_list.append("Andrzej")
print("Zapraszam Cię na obiad " + guest_list[0])
print("Zapraszam Cię na obiad " + guest_list[1])
print("Zapraszam Cię na obiad " + guest_list[2])
print("Zapraszam Cię na obiad " + guest_list[3])
print("Zapraszam Cię na obiad " + guest_list[4])
print("Zapraszam Cię na obiad " + guest_list[5])

print(guest_list)

uninvited_guest1 = guest_list.pop(0)
print("Niestety, nie udało sięprzygotować stołu. Muszę odwołać Twoje zaproszenie, przepraszam " + uninvited_guest1)
uninvited_guest2 = guest_list.pop(1)
print("Niestety, nie udało sięprzygotować stołu. Muszę odwołać Twoje zaproszenie, przepraszam " + uninvited_guest2)
uninvited_guest3 = guest_list.pop(0)
print("Niestety, nie udało sięprzygotować stołu. Muszę odwołać Twoje zaproszenie, przepraszam " + uninvited_guest3)
uninvited_guest4 = guest_list.pop(1)
print("Niestety, nie udało sięprzygotować stołu. Muszę odwołać Twoje zaproszenie, przepraszam " + uninvited_guest4)

print(guest_list[0] + ", zapraszam na obiad!")
print(guest_list[1] + ", zapraszam na obiad!")

print(guest_list)

del guest_list[0]
del guest_list[0]
print(guest_list)
