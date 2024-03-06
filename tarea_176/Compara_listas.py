lista1 = ["a", 5, "iker", 44, 123, ]
lista2 = [4, 6, 5, "a", 1598, 44, "iker", "ababa"]
coinciden = []
for i in lista1:
    if i in lista2:
        coinciden.append(i)
print(f"Lista de valores que están en ambas listas: {coinciden}")
        