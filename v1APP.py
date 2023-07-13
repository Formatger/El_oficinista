import math
import tkinter as tk
from tkinter import scrolledtext as st
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb
#PREGUNTAS SOBRE LA MANGA#
print("De que material es el artículo? Punzonado (P), Tejido (T)o Monofilamento (M)?");
Material = input();
print("Código de 3 cifras del material?")
CodMat = input();
print("Diámetro?");
Dim = int(input());
print ("Longitud?");
Long = int(input());
print("Código superior");
CS = int(input());
print("Código inferior");
CI = int(input());

#CONSTANTES#####################################################
TermoSoldado = 20;

#VARIABLES###########################################################
Placa = int(); #DEFINDE LA PLACA COMO A NÚMERO ENTERO#
LongDobladillo = int(); #DEFINDE DOBLADILLO COMO A NÚMERO ENTERO#
AreaTapa = int();
a = int(); #Aumento del ancho segun código#
b1 = int(); #Aumento del largo segun código superior#
b2 = int(); #Aumento del largo segun código inferior#
c = int(); #Área tapa#
if Material == "P":
    LongRollo = int(2150);
if Material == "T":
    LongRollo = int(1700);
if Material == "M":
    LongRollo = int(1200);
    
#AUMENTO ANCHO Y LARGO SEGÚN CS#
if CS == 7: #SNAP-RING#
    print("Placa?");
    Placa = int(input());
    a = TermoSoldado;
    b1 = 60;
    
if CS == 3: #DOBLADILLO CON CUERDA#
    a = TermoSoldado+25;
    print("Longitud del dobladillo? (50 o 30mm?)");
    LongDobladillo = int(input());

    if LongDobladillo == 50:
        b1 = 55;
    else:
        b1 = 35;
    
if CI == 70 or 71 or 74:
    b2 = 15;

#VARIABLES DE CÁLCULO#
AnchoCorte = int();
LargoCorte = int();
DimTapa = int();
NumCortes = math.floor(LongRollo/round((math.pi * Dim)+ a));
NumCortesTapas = int();
AnchoPlano = math.floor(math.pi*Dim/2);
       
#CASO SNAP-RING#
if CS == 7 and CI == 70 or 71 :
    if Material == "P":
        AnchoCorte = round((math.pi * Dim)+ a);
        LargoCorte = round((Long + b1+b2),0);   
    DimFleje =(Placa-4);
    if Material == "T":
        print("Ancho x Largo = ",AnchoCorte,"x",LargoCorte,"mm");
        print(LongRollo);

    if Material == "M":
        print("Monofilamento");

#CASO DOBLADILLO Y CUERDA#
if CS == 3 and CI == 70 or 71 :

    ##PARA PUNZONADOS##
    if Material == "P":
        AnchoCorte = round((math.pi * Dim)+ a);
        LargoCorte = round((Long + b1+b2),0);        
        LongCuerda = round((math.pi * Dim)+ 30);    
        
    ##PARA TEJIDOS##
    if Material == "T":
        print("Ancho x Largo = ",AnchoCorte,"x",LargoCorte,"mm");
        print(LongRollo);
        
    ##PARA MONOFILAMENTOS##
    if Material == "M":
        print("Monofilamento");


########################CÁLCULO RESULTADOS##############################

        
###### DIÁMETRO TAPA + CONSUMO TAPA #####        
if Dim > 80:
    DimTapa = round(((AnchoCorte-16)/math.pi)+20);
else:
    DimTapa = round((Dim+((AnchoCorte-16)/math.pi)+15));
NumCortesTapas = math.floor(LongRollo/DimTapa);
AreaTapa = (LongRollo*DimTapa/1000000)/NumCortesTapas;
if AreaTapa < 0.03:
    AreaTapa = 0.03;
##########################################
  
#CONSUMO MATERIA PRIMA MATERIAL#
ConsumoM2 = round((((((LongRollo/NumCortes)*LargoCorte)/1000000)+AreaTapa)*1.1),3);
#CONSUMO DE CUERDAS#
ConsumoCuerda = round(LongCuerda/1000*1.1,3);

##########################DATOS PARA OFICINA TÉCNICA##############################
print("\n","\n","\n");
print("DATOS PARA OFICINA TÉCNICA:\n","\n");
print("Escandallo y consumo:\n")
print("Consumo de",CodMat,"=",ConsumoM2,"m\xb2");
if CS == 7:
    print("Diámetro del fleje =",DimFleje,"mm");
    print("CE-03 = 0.6m");
    print("RF-013 = 1.2m");
    print("Hilo = 0.03m");
    print("RF-P02.061.201 = 0.3m\n");
if CS == 3:
    print("Consumo de cuerda =",ConsumoCuerda,"m");
    
print();
print();
print("Datos para las fases:\n");
print("Ancho x Largo = ",AnchoCorte,"x",LargoCorte,"mm");
print("Diámetro de la tapa=",DimTapa,"mm");
print("Longitud de cuerda =",LongCuerda,"mm");
print("A.P =",AnchoPlano,"mm");
    
