##EL OFICINISTA

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
        elif articulo.lower() == "tamiz textil":
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
        if articulo == "Bolsa petaca":
            while True:
                dim_o_ancho_plano = int()
                dim_o_ancho_plano = input("Introduce el ancho plano ")
                if dim_o_ancho_plano.isdigit():
                    dim_o_ancho_plano = int(dim_o_ancho_plano)
                    break
                else:
                    print("Error, vuelve a introducir el dato")
        
        elif articulo == "Tamiz textil":
            while True:
                dim_o_ancho_plano = int()
                dim_o_ancho_plano = input("Introduce el ancho plano ")
                if dim_o_ancho_plano.isdigit():
                    dim_o_ancho_plano = int(dim_o_ancho_plano)
                    break
                else:
                    print("Error, vuelve a introducir el dato")     
        else:        
            while True:
                dim_o_ancho_plano = int()
                dim_o_ancho_plano = input("Introduce el Ø ")
                if dim_o_ancho_plano.isdigit():
                    dim_o_ancho_plano = int(dim_o_ancho_plano)
                    break
                else:
                    print("Error, vuelve a introducir el dato")
        break
                     
    while True:
        longitud = int()
        longitud = input("Introduce la longitud: ")
        if longitud.isdigit():
            longitud = int(longitud)
            break
        else:
            print("Error, vuelve a introducir el dato")
    
    if (articulo == 'Manga') or (articulo == 'Conector') or (articulo == 'Bolsa') or (articulo == 'Bolsa petaca'):
        while True:
            cod_sup = input("Introduce el código superior: ")
            if cod_sup.isdigit() and mat_cod_sup.columns.values.any():
                cod_sup = int(cod_sup)   
                break
            else:
                print("Error, vuelve a introducir el dato")

        while True:
            cod_med = ""
            cod_med = input("Introduce el código intermedio: ")
            if cod_med.isdigit() and mat_cod_sup.columns.values.any():
                cod_med = int(cod_med)   
                break
            else:
                print("Error, vuelve a introducir el dato")

        while True:
            cod_inf = ""
            cod_inf = input("Introduce el código inferior: ")
            if cod_inf.isdigit() and mat_cod_inf.columns.values.any():
                cod_inf = int(cod_inf)   
                break
            else:
                print("Error, vuelve a introducir el dato")

    elif articulo == 'Tamiz textil':
        cod_sup = 0
        cod_med = 0
        cod_inf = 0
        
    return (articulo, calidad, dim_o_ancho_plano, longitud, cod_sup, cod_inf)

datos = datos_iniciales() #return (articulo, calidad, dim_ancho_plano, longitud, cod_sup, cod_inf)

if datos[0] == "Manga":
    def calculo():
        costura = 20
        gramaje = datos[1]
        if gramaje[1] == 'A':
            polimero = 'poliamida'
        else:
            polimero = 'poliester'


        corte_superior = (((mat_cod_sup.loc[mat_cod_sup["calidad"] == datos[1]][datos[4]])))
        corte_inferior = (((mat_cod_sup.loc[mat_cod_sup["calidad"] == datos[1]][datos[5]])))
        corte_superior = int(corte_superior.iloc[0])
        corte_inferior = int(corte_inferior.iloc[0])
        if corte_superior < corte_inferior:
            corte = corte_inferior
        elif corte_superior > corte_inferior:
            corte = corte_superior
        else: 
            corte = corte_superior
        ancho_corte = ((datos[2] * math.pi) + corte + costura)
        ancho_corte = math.ceil(ancho_corte)


        largo_superior = (((mat_cod_inf.loc[mat_cod_inf["calidad"] == datos[1]][datos[4]])))
        largo_inferior = (((mat_cod_inf.loc[mat_cod_inf["calidad"] == datos[1]][datos[5]])))
        largo_superior = int(largo_superior.iloc[0])
        largo_inferior = int(largo_inferior.iloc[0])
        largo_corte = (datos[3] + largo_superior + largo_inferior)


        if datos[2] < 80:
            dim_tapa = round(((ancho_corte - costura)/math.pi) + 15 )
        else:
            dim_tapa = round(((ancho_corte - costura)/math.pi) + 20 )


        return ancho_corte, largo_corte, dim_tapa, polimero   

if datos[0] == "Conector":
    def calculo():
        costura = 20
        corte_superior = (((mat_cod_sup.loc[mat_cod_sup["calidad"] == datos[1]][datos[4]])))
        corte_inferior = (((mat_cod_sup.loc[mat_cod_sup["calidad"] == datos[1]][datos[5]])))
        corte_superior = int(corte_superior.iloc[0])
        corte_inferior = int(corte_inferior.iloc[0])
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


        largo_superior = (((mat_cod_inf.loc[mat_cod_inf["calidad"] == datos[1]][datos[4]])))
        largo_inferior = (((mat_cod_inf.loc[mat_cod_inf["calidad"] == datos[1]][datos[5]])))
        largo_superior = int(largo_superior.iloc[0])
        largo_inferior = int(largo_inferior.iloc[0])

        largo_corte = (datos[3] + largo_superior + largo_inferior)


        return ancho_corte, largo_corte

if datos[0] == "Bolsa petaca":
    def calculo():
        costura = 20
        costura_burlete = 90
        corte_superior = (((mat_cod_sup.loc[mat_cod_sup["calidad"] == datos[1]][datos[4]])))
        corte_inferior = (((mat_cod_sup.loc[mat_cod_sup["calidad"] == datos[1]][datos[5]])))
        corte_superior = int(corte_superior.iloc[0])
        corte_inferior = int(corte_inferior.iloc[0])

        if corte_superior < corte_inferior:
            corte = corte_inferior
        elif corte_superior > corte_inferior:
            corte = corte_superior
        else: 
            corte = corte_superior
        ancho_corte = ((datos[2]*2) + corte + costura)
        ancho_corte = math.ceil(ancho_corte)

        largo_superior = (((mat_cod_inf.loc[mat_cod_inf["calidad"] == datos[1]][datos[4]])))
        largo_inferior = (((mat_cod_inf.loc[mat_cod_inf["calidad"] == datos[1]][datos[5]])))
        largo_superior = int(largo_superior.iloc[0])
        largo_inferior = int(largo_inferior.iloc[0])

        largo_corte = (datos[3] + largo_superior + largo_inferior)
        
        longitud_burlete = (datos[2] *2) + costura_burlete

        return ancho_corte, largo_corte, longitud_burlete

if datos[0] == "Tamiz textil":
    def calculo():
        micraje = datos[1]
        micraje = micraje[3:7]
        if micraje[1] == 'A':
            polimero = 'poliamida'
        else:
            polimero = 'poliester'

        if int(micraje) <= 750:
            longitud_tiras_bocas = (datos[2] * 2) + 70
            longitud_tiras_longitudinales = (datos[3])
            ancho_corte = (datos[2] * 2) + 50
            largo_corte = (datos[3])
            longitud_cuerda = longitud_tiras_bocas

        elif (int(micraje)  > 750) and (int(micraje)  <= 1000):
            longitud_tiras_bocas = (datos[2] * 2) + 70
            longitud_tiras_longitudinales = (datos[3]) - 20
            ancho_corte = (datos[2] * 2) + 40
            largo_corte = (datos[3]) - 20
            longitud_cuerda = longitud_tiras_bocas
        
        elif int(micraje)  > 1000:
            longitud_tiras_bocas = (datos[3] * 2) + 70
            longitud_tiras_longitudinales = (datos[3]) - 20
            ancho_corte = (datos[2] * 2) + 40
            largo_corte = (datos[3]) - 20
            longitud_cuerda = longitud_tiras_bocas
        return ancho_corte, largo_corte, longitud_tiras_bocas, longitud_tiras_longitudinales, longitud_cuerda, micraje, polimero

def calculo_gasto():
    calidad = datos[1]
    longitud_rollo = mat_cod_sup.loc[mat_cod_sup["calidad"] == calidad,"longitud rollo"]
    longitud_rollo = int(longitud_rollo.iloc[0])

    num_cortes_rollo = math.floor(longitud_rollo/resultado[0])
    area_mat_corte = ((longitud_rollo * resultado[1])/(num_cortes_rollo*1000000))

    if datos[5] == 70:
        if datos[2] < 80:
            area_mat_tapa = 0.06
        else: 
            area_mat_tapa = (longitud_rollo * resultado[2])/((math.floor(longitud_rollo/datos[2])*1000000))
    else:
        area_mat_tapa = 0

    area_total = ((area_mat_corte + area_mat_tapa)*1.1)

    return num_cortes_rollo, area_mat_corte, area_mat_tapa, area_total





########      RESULTADOS      ########

resultado = calculo()   #ancho corte, largo corte, longitud burlete/cuerda
gasto = calculo_gasto()

corte = f"{resultado[0]} x {resultado[1]}"
if datos[0] == "Bolsa petaca":
    ancho_plano = datos[2]
else:
    ancho_plano = math.ceil((int(datos[2]*math.pi))/2)

# descripcion_articulo = f"Has definido el articulo como {datos[0]} de Ø{datos[2]} x {datos[3]}mm·\nExtremo superior con {datos[4]} y extremo inferior con {datos[5]}"
# print(descripcion_articulo)


if datos[0] == "Manga":
    print(f'\n\nHas definido el artículo como Manga de Ø = {datos[2]} x {datos[3]}mm')
    print(f'\n\n\nLongitudes de corte:\n')
    print(f"El corte es = {corte}mm.")

    if datos[4] == 3:
        print(f"El corte de la cuerda es = {round(((datos[2]*math.pi)+30),)}mm.")
    if datos[5] == 70:
        print(f"El corte de la tapa es = Ø {resultado[2]}mm.")

    print(f'\n\nConsumo:\n')
    print(f'Consumo de {datos[1]} = {round(gasto[3],3)} m2')
    print(f'Consumo de CE-03 = {round(((((datos[2]*math.pi)+30)*1.1)*0.001),3)} m')
    if resultado[3] == 'poliamida':
        print(f'Consumo de HA-40.2.S0 = 0.03m')
    else:
        print(f'Consumo de HE-40.3.S0 = 0.03m')

    print(f'\n\nMedidas e información:\n')
    print(f"El A.P = {ancho_plano}mm.")

if datos[0] == "Conector":
    print(f"El corte es = {corte}mm.")
    print(f"El A.P = {ancho_plano}mm.")

if datos[0] == "Bolsa petaca":
    print(f"El corte es = {corte}mm.")
    print(f"El A.P = {ancho_plano}mm.")
    print(f"La longitud del burlete = {resultado[2]}mm.")
    print(f'Consumo de {datos[1]} = {gasto[3]} m2')

if datos[0] == "Tamiz textil":
    print(f'\n\nHas definido el artículo como Tamiz textil de A.P = {datos[2]} x {datos[3]}mm')
    print(f'\n\n\nLongitudes de corte:\n')
    print(f'2 tiras a {resultado[2]}mm de RF-P02.068.125')
    print(f'2 tiras a {resultado[3]}mm de RF-P02.030.125')
    print(f'El corte es = {resultado[0]} x {resultado[1]}mm')
    print(f'\n\nConsumo:\n')
    print(f'Consumo de {datos[1]} = {round(gasto[3],3)} m2')
    print(f'Consumo de RF-P02.068.125 = {round((resultado[2]*2*0.0011),3)} m')
    print(f'Consumo de RF-P02.030.125 = {round((resultado[3]*2*0.0011),3)} m')
    print(f'Consumo de CE-03 = {round((resultado[4]*2*0.0011),3)} m')
    print(f'Consumo de ZE-45 = {round(datos[2]*4*0.0011,3)}m')
    print(f'Consumo de ZE-35 = {round(datos[3]*2*0.0011,3)}m')
    if resultado[6] == 'poliamida':
        print(f'Consumo de HA-40.2.S0 = 0.03m')
    else:
        print(f'Consumo de HE-40.3.S0 = 0.03m')