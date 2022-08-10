rivers = ["Wisła", "Odra", "San", "Wieprz", "Bug", "Noteć"]
print(rivers)

rivers.insert(1, "Drwęca")
print(rivers)

rivers.append("Warta")
print(rivers)

rivers.remove("Wieprz")
print(rivers)

deleted_river = rivers.pop(3)
print(deleted_river)
print(rivers)

del rivers[4]
print(rivers)

print(sorted(rivers))
print(sorted(rivers, reverse=True))

rivers.sort()
print(rivers)

rivers.sort(reverse=True)
print(rivers)

print("W liście znajduje się " + str(len(rivers)) + " rzek.")