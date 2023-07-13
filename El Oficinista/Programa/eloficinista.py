import math
import pandas as pd
import numpy as np
import openpyxl as op

mat_cod_sup = pd.read_excel("listcodancho.xlsx")
mat_cod_inf = pd.read_excel("listcodlargo.xlsx")
print(mat_cod_sup)
print(mat_cod_inf)


def datos_iniciales():
    while True:
        articulo = ""
        articulo = input("Introduce el tipo de articulo: ")
        if articulo.lower() == "manga":
            articulo = articulo.lower()
            articulo = articulo.capitalize()
            break
        elif articulo.lower() == "conector":
            articulo = articulo.lower()
            articulo = articulo.capitalize() 
            break
        elif articulo.lower() == "bolsa":
            articulo = articulo.lower()
            articulo = articulo.capitalize() 
            break
        elif articulo.lower() == "bolsa petaca":
            articulo = articulo.lower()
            articulo = articulo.capitalize() 
            break
        else:
            print("Error, vuelve a introducir el dato")

    while True:
        calidad = ""
        calidad = input("Introduce la calidad del artículo: ")
        calidad = calidad.upper()
        existe_en_listado = mat_cod_sup.isin(["calidad", calidad]).any()
        if existe_en_listado["calidad"] == True: 
            break
        else:
            print("Error, vuelve a introducir el dato")
    while True:
        dim = int()
        dim = input("Introduce el Ø ")
        if dim.isdigit():
            dim = int(dim)
            break
        else:
            print("Error, vuelve a introducir el dato")
    while True:
        longitud = int()
        longitud = input("Introduce la longitud: ")
        if longitud.isdigit():
            longitud = int(longitud)
            break
        else:
            print("Error, vuelve a introducir el dato")
    while True:
        cod_sup = ""
        cod_sup = int(input("Introduce el código superior: "))
        if cod_sup in mat_cod_sup.values:
            cod_sup = int(cod_sup)   
            break
        else:
            print("Error, vuelve a introducir el dato")
    while True:
        cod_inf = ""
        cod_inf = int(input("Introduce el código inferior: "))
        if cod_inf in mat_cod_inf.values:
            cod_inf = int(cod_inf)   
            break
        else:
            print("Error, vuelve a introducir el dato")
    return (articulo, calidad, dim, longitud, cod_sup, cod_inf)

datos = datos_iniciales() #return (articulo, calidad, dim, longitud, cod_sup, cod_inf)
descripcion_articulo = f"Has definido el articulo como {datos[0]} de Ø{datos[2]} x {datos[3]}·\nExtremo superior con {datos[4]} y extremo inferior con {datos[5]}"
print(descripcion_articulo)

if datos[0] == "Manga":
    def calculo():
        costura = 20
        corte_superior = int((((mat_cod_sup.loc[mat_cod_sup["calidad"] == datos[1]][datos[4]]))))
        corte_inferior = int((((mat_cod_sup.loc[mat_cod_sup["calidad"] == datos[1]][datos[5]]))))
        print(corte_superior)
        print(corte_inferior)
        if corte_superior < corte_inferior:
            corte = corte_inferior
        elif corte_superior > corte_inferior:
            corte = corte_superior
        else: 
            corte = corte_superior
        ancho_corte = ((datos[2] * math.pi) + corte + costura)
        ancho_corte = math.ceil(ancho_corte)


        largo_superior = int((((mat_cod_inf.loc[mat_cod_inf["calidad"] == datos[1]][datos[4]]))))
        print(largo_superior)
        largo_inferior = int((((mat_cod_inf.loc[mat_cod_inf["calidad"] == datos[1]][datos[5]]))))
        largo_corte = (datos[3] + largo_superior + largo_inferior)


        return ancho_corte, largo_corte
    

if datos[0] == "Conector":
    def calculo():
        costura = 20
        corte_superior = int((((mat_cod_sup.loc[mat_cod_sup["calidad"] == datos[1]][datos[4]]))))
        corte_inferior = int((((mat_cod_sup.loc[mat_cod_sup["calidad"] == datos[1]][datos[5]]))))
        print(corte_superior)
        print(corte_inferior)
        if corte_superior < corte_inferior:
            corte = corte_inferior
        elif corte_superior > corte_inferior:
            corte = corte_superior
        else: 
            corte = corte_superior
        ancho_corte = ((datos[2] * math.pi) + corte + costura)
        ancho_corte = math.ceil(ancho_corte)


        largo_superior = int((((mat_cod_inf.loc[mat_cod_inf["calidad"] == datos[1]][datos[4]]))))
        print(largo_superior)
        largo_inferior = int((((mat_cod_inf.loc[mat_cod_inf["calidad"] == datos[1]][datos[5]]))))
        largo_corte = (datos[3] + largo_superior + largo_inferior)


        return ancho_corte, largo_corte



########      RESULTADOS      ########

resultado = calculo()
corte = f"{resultado[0]} x {resultado[1]}"
print(f"El corte es = {corte}mm.")
ancho_plano = math.ceil((int(datos[2]*math.pi))/2)
print(f"El A.P = {ancho_plano}mm")
