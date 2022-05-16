"""Parcial No. 1 - Fundamentos de programación

Realizar el análisis (identificación de variables), diseño (diagrama de flujo) y 
construcción (programa en Python y pantallazos de su funcionamiento) que resuelva 
la siguiente situación:"""

print("-----------------------------------")
print("------------Bienvenidos------------")
print("------Almacén Socorro Center-------")
print("-----------------------------------")

# input
x = int(input("Valor del primer producto: $"))
y = int(input("Valor del segundo producto: $"))
z = int(input("Valor del tercer producto: $"))

# processing
if x > y and x > z:
    suma = y + z
    msj = "El precio de sus productos con la oferta es: $" + str(suma)
else:
    suma1 = x + y
    msj = "El precio de sus productos con la oferta es: $" + str(suma1)
if x < y and y > z:
    suma2 = x + z
    msj = "El precio de sus productos con la oferta es: $" + str(suma2)

# output
print(msj)

print("Gracias por su compra")
print("Feliz Día de la Madre ^^")