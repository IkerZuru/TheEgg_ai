palabra = input("Introduce una palabra y te dire si es un palíndromo:\n")
if palabra.lower() == palabra[::-1].lower():
    print("La palabra proporcionada SI es un palíndromo")
else:
    print("La palabra proporcionada NO es un palíndromo")