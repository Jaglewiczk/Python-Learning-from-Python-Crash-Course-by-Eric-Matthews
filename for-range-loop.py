for value in range(1,30):
    print(value)
numbers = list(range(1,10))
print(numbers)

even_numbers = list(range(2,11,2))  #3-ci argument definiuje, o ile zwiększony będzie każdy kolejny wyraz listy
print(even_numbers)

squares = []
for value in range (1,11):
    square = value**2
    squares.append(square)
    squares.append(value**2)    #inny zapis tego samego (bez tworzenia dodatkowej zmiennej square)
print(squares)

print(min(squares))
print(max(squares)) #najmniejszy, największy wyraz z listy oraz ich suma)
print(sum(squares))

squares2 = [value**2 for value in range(3, 15)]    #bardziej zaawansowane(lista składana)
print(squares2)
print(sum(squares2))