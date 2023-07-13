import pandas as pd
import numpy
a = pd.read_excel("prueba.xlsx")
material = input("Introduce el material: ")
material = material.upper()
cod_sup = int(input("Introduce el código superior: "))
def ancho(material, cod_sup):
    material = material.upper()
    print(material)
    c = int((((a.loc[a["calidad"] == material][cod_sup]))))
    print(f"550 x {c}")

print(a)
print(cod_sup)
print(cod_sup in a.values)