import math;
import pandas as pd;
import openpyxl;
import numpy;

path = 'listmat.xlsx';

pd.read_excel("listmat.xlsx");
a = pd.read_excel("listmat.xlsx");

pd.read_excel("prueba.xlsx");
b = pd.read_excel("prueba.xlsx",index_col="calidad");
c = pd.read_excel("prueba.xlsx");



print(a);
db = b.to_numpy();

x = b.index()
