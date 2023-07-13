# import pandas as pd
# import numpy
# a = pd.read_excel("prueba.xlsx")
# print(a)
# cod = 2
# print(a.loc[a["calidad"] == "PE-0500.000000"][2])
# b = ((a.loc[a["calidad"] == "PE-0500.000000"][cod]) + 4)
# print(b)
# b = int(b)
# print(f"550 x {b}")
# # print(a[[["calidad"] == "PE-0500.000000", 1]])



import pandas as pd
import numpy
a = pd.read_excel("prueba1.xlsx")
mat_cod_inf = pd.read_excel("prueba2.xlsx")
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
print(a.iloc[-1] == cod_sup)
print(cod_sup in a.values)
# print(a.isin(["calidad", material]).any())
# existe_en_listado = a.isin(["calidad", material]).any()
# print(existe_en_listado["calidad"])
# ancho(material, cod_sup)

