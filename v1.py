import math;
import pandas as pd;
import openpyxl;

#####LECTURA LISTADOS EXCEL######
listmat = pd.read_excel("listmat.xlsx");
listcods = pd.read_excel("listcods.xlsx");
listcodi = pd.read_excel("listcodi.xlsx");

#PREGUNTAS SOBRE LA MANGA - INTRODUCCIÓN DE DATOS#
Artículo = input("Que tipo de artículo necesitas? (Manga = M, Conector = C, Saco = S, Bolsa = B, Bolsa Petaca = BP, Tamiz Téxtil = TT)\n");
Material = input("De que material es el artículo? (Punzonado = P, Tejido = T, Monofilamento = M)\n");
CodMat = int(input("Código de 3 cifras del material?\n"));
Dim = int(input("Diámetro?\n"));
Long = int(input("Longitud?\n"));
CS = int(input("Código superior\n"));
CI = int(input("Código inferior\n"));

#CONSTANTES#####################################################
TermoSoldado = 20;
####VARIABLES PARA AUMENTO ANCHO Y LARGO SEGUN CODIGO#####
    
a = int(); #Aumento del ancho segun código#
b1 = int(); #Aumento del largo segun código superior#
b2 = int(); #Aumento del largo segun código inferior#
NumCortesTapas = int(); #Cuantos cortes salen del diámetro tapa#
AnchoPlano = int(); #Ancho plano útil#
LongTotal = int(); #Longitud total del largo teniendo en cuenta refuerzos etc..#
AreaTapa = int(); #Area de la tapa#
AnchoCorte = int(); #Ancho corte manga#
LargoCorte = int(); #Largo corte manga#
DimTapa = int(); #Diiámetro tapa con costuras#
LongRefuerzo = int() #Longitud del refuerzo#
NumCortes = int(); #Num cortes por ancho de rollo de la manga#
Placa = int();
DimFleje =int();
longRollo = int(listmat[listmat["Código material"]==CodMat]["LongRollo"]);
######################AUMENTOS ANCHOS Y LARGOS SEGÚN CÓDIGO SUP. E INF.#########################
#AUMENTO ANCHO Y LARGO SEGÚN CS#
if CS == 1: #DOBLADILLO#
    a = TermoSoldado;
    b1 = 0;
    
if CS == 2: #DOBLADILLO#
    a = TermPlaca = input();oSoldado;
    print("Longitud del dobladillo? (50 o 30mm?)");
    LongDobladillo = input();

    if LongDobladillo == 50:
        b1 = 55;
    else:
        b1 = 35; 
    
if CS == 3: #DOBLADILLO CON CUERDA#
    a = TermoSoldado+25;
    print("Longitud del dobladillo? (50 o 30mm?)");
    LongDobladillo = int(input()); #Definimos dobladillo como a entero#

    if LongDobladillo == 50:
        b1 = 55;
    else:
        b1 = 35;
if CS == 6:   #SNAP.RING POSTIZO#
    print("Placa?");
    Placa = int(input());
    print("Material Cabezal postizo? (Normal = N, Anti-éstático = B, Siliconado = S, Anti-estático + siliconado = BS");
    TipoCab = input();
    if TipoCab == "B":
        MatCab = "PE-0450.B00000";
    if TipoCab == "N":
        MatCab = "PE-0450.000000";
    if TipoCab == "S":
        MatCab = "PE-0450.0S0000";
    if TipoCab == "BS":
        MatCab = "PE-0450.BS0000";
    a = TermoSoldado;
    b1 = -35        
if CS == 7: #SNAP-RING#
    print("Placa?");
    Placa = int(input());
    a = TermoSoldado;
    b1 = 65;

    
#AUMENTO ANCHO Y LARGO SEGÚN CI#    
if CI == 70 or 71 or 74:
    b2 = 15;
if CI == 71:
    b2 = 15;
    print("Longitud del refuerzo?")
    LongRefuerzo = int(input());#Definimos refuerzo como a entero#


########################CÁLCULO RESULTADOS##############################

#########CÁLCULO CORTES PUNZONADOS#######
AnchoCorte = round((math.pi * Dim)+ a);
LargoCorte = round((Long + b1+b2),0);
AnchoCorteRef = AnchoCorte;
LongCuerda = round((math.pi * Dim)+ 30);
LongTotal = LargoCorte+LongRefuerzo;
AnchoPlano = math.floor(math.pi*Dim/2);
NumCortes = math.floor(longRollo/round((math.pi * Dim)+ a));
DimFleje =(Placa-4);
AnchoCorteCab = int(Placa*math.pi+20)
LargoCorteCab = 140;
NumCortesCab = math.floor(longRollo/round(AnchoCorteCab));
########CONSUMO CABEZAL POSTIZO HACER FORMULA###########
ConsumoCabPostizo = round((((longRollo*LargoCorteCab)/NumCortesCab)/1000000)*1.1,3);
###### DIÁMETRO TAPA + CONSUMO TAPA #####        
if Dim > 80:
    DimTapa = round(((AnchoCorte-16)/math.pi)+20);
else:
    DimTapa = round((Dim+((AnchoCorte-16)/math.pi)+15));
NumCortesTapas = math.floor(longRollo/DimTapa);
AreaTapa = (longRollo*DimTapa/1000000)/NumCortesTapas;
if AreaTapa < 0.03:
    AreaTapa = 0.03;
##########################################
  
#CONSUMO MATERIA PRIMA MATERIAL#
ConsumoM2 = round((((((longRollo/NumCortes)*(LongTotal))/1000000)+AreaTapa)*1.1),3);
#CONSUMO DE CUERDAS#
ConsumoCuerda = round(LongCuerda/1000*1.1,3);





##########################DATOS PARA OFICINA TÉCNICA##############################
print("\n","\n","\n");
print("DATOS PARA OFICINA TÉCNICA:\n","\n");
print("Escandallo y consumo:\n")
print("Consumo de",listmat[listmat["Código material"]==CodMat]["Tipo"],"=",ConsumoM2,"m\xb2");
if CS == 6:
    print("Cabezal postizo en",MatCab,"=",ConsumoCabPostizo,"m\xb2")
if CS == 7:
    print("Diámetro del fleje =",DimFleje,"mm");
    print("CE-03 = 1.2m");
    print("RF-013 = 0.6m");  
    print("RF-P02.061.201 = 0.6m\n");
if CS == 6:
    print("Diámetro del fleje =",DimFleje,"mm");
    print("CE-03 = 01.2m");
    print("RF-013 = 0.6m");  
    print("RF-P02.061.201 = 0.6m");    
print("Hilo = 0.03m");
if CS == 3:
    print("Consumo de cuerda =",ConsumoCuerda,"m");



    
print();  
print();
print("Datos para las fases:\n");
print("Ancho x Largo = ",AnchoCorte,"x",LargoCorte,"mm");
if CS == 6:
    print("Ancho x Largo del cabezal= ",AnchoCorteCab,"x",LargoCorteCab,"mm");
if CI == 71:
    print("Ancho x largo del refuerzo =",AnchoCorteRef,"x",LongRefuerzo,);
print("Diámetro de la tapa=",DimTapa,"mm");
if CS == 3:
    print("Longitud de cuerda =",LongCuerda,"mm");
print("A.P =",AnchoPlano,"mm");
    
