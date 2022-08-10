for value in range(1,21):
    print(value)
list = []
for value in range(1, 100001):
    list.append(value)
print(min(list))
print(max(list))
print(len(list))
print(sum(list))

list2 = []
for value in range(1,20,2):
    list2.append(value)
print(list2)

list3 = []
for value in range(3,30):
    list3.append(value**3)
print(list3)

list4 = []
for value in range (1, 11):
    list4.append(value**3)
print(list4)

list5 = [value**2 for value in range(1,11)]
print(list5)