a = int(input("Escribe un número:\n"))
max = a
print(type(a))
b = int(input("Escribe otro número:\n"))
if b > max:
    max = b
c = int(input("Escribe un tercer número:\n"))
if c > max:
    max = c
print(f"El máximo de los 3 números dados es {max}")
