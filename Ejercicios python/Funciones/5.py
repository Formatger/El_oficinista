import math as mat

dim = float(input("Introduce el diámetro (en m): "))
l = float(input("Introduce la longitud (en m): "))

def area_circulo():
    area = ((dim/2)**2)*mat.pi
    return area

def volumen_cilindro():
    volumen = area_circulo()*l
    return volumen

volumen = volumen_cilindro()
print(volumen)


