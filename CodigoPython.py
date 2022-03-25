# -*- coding: utf-8 -*-
import  random

c=0
k=0
bplo=0
ihi=0
ilo=0
aux=0
resta=0
valores=int(input("ingrese la cantidad de valores que va a ingresar: "))

for i in range (1, valores+1):
    valorpp=float(input("ingrese el varlor obtenido:"))
    if valorpp>0 and valorpp<=55:
        print (f"la calidad del aire con un total de {valorpp} es muy buena ")
        bplo=round(random.uniform(0,valorpp - 0.001),3)
        print("El valor de BpLo es: ", bplo)
        ihi=50
        ilo=0
        k= ihi - ilo
        resta= round((valorpp - bplo),3)
        print("El valor de la resta es: ",resta)
        k= round((k / resta),2)
        print("El valor de K es: ",k)
        c=round(random.uniform(bplo+0.001,0.070),3)
        print("El valor redondeado para la concentración del contaminante es: ", c)
        
        print("apartado particulas menores a 10 micrometros")
        valorpp= round(random.uniform(1,40))
        print("El valor de bphi es: ", valorpp)
       
        bplo=round(random.uniform(0,valorpp - 1))
        print("El valor de bplo es: ", bplo)
        k= ihi - ilo
        resta= round((valorpp - bplo))
        print("El valor de la resta es: ",resta)
        k= round((k / resta),3)
        print("El valor de K es: ",k)
        c=round(random.uniform(bplo+1,40))
        print("El valor redondeado para la concentración del contaminante es: ", c)
        indice = k * (c - bplo)
        indice= round((indice + ilo))
        print("El indice de contaminación en Partículas Menores a 10 micrómetros (PM10) es: ", indice)
       
    if valorpp>=51 and valorpp<=110:
        bplo=round(random.uniform(0.071,valorpp - 0.001),3)
        print("El valor de BpLo es: ", bplo)
        ihi=100
        ilo=51
        k= ihi - ilo
        resta= round((valorpp - bplo),3)
        print("El valor de la resta es: ",resta)
        k= round((k / resta),2)
        print("El valor de K es: ",k)
        c=round(random.uniform(bplo+0.001,0.095),3)
        print("El valor redondeado para la concentración del contaminante es: ", c)
       
        print("apartado particulas menores a 10 micrometros")
        valorpp= round(random.uniform(41,75))
        print("El valor de bphi es: ", valorpp)
       
        bplo=round(random.uniform(40,valorpp - 1))
        print("El valor de bplo es: ", bplo)
        k= ihi - ilo
        resta= round((valorpp - bplo))
        print("El valor de la resta es: ",resta)
        k= round((k / resta),3)
        print("El valor de K es: ",k)
        c=round(random.uniform(bplo+1,75))
        print("El valor redondeado para la concentración del contaminante es: ", c)
        indice = k * (c - bplo)
        indice= round((indice + ilo))
        print("El indice de contaminación en Partículas Menores a 10 micrómetros (PM10) es: ", indice)
        
        
        print (f"la calidad del aire con un total de {valorpp} es regular ")
    if valorpp>=111 and valorpp<=165:
        bplo=round(random.uniform(0.096,valorpp - 0.001),3)
        print("El valor de BpLo es: ", bplo)
        ihi=150
        ilo=101
        k= ihi - ilo
        resta= round((valorpp - bplo),3)
        print("El valor de la resta es: ",resta)
        k= round((k / resta),2)
        print("El valor de K es: ",k)
        c=round(random.uniform(bplo+0.001,0.154),3)
        print("El valor redondeado para la concentración del contaminante es: ", c)
        print("\n")
        print("\n")
        print("apartado particulas menores a 10 micrometros")
        valorpp= round(random.uniform(77,214))
        print("El valor de bphi es: ", valorpp)
        
        bplo=round(random.uniform(76,valorpp - 1))
        print("El valor de bplo es: ", bplo)
        k= ihi - ilo
        resta= round((valorpp - bplo))
        print("El valor de la resta es: ",resta)
        k= round((k / resta),3)
        print("El valor de K es: ",k)
        c=round(random.uniform(bplo+1,214))
        print("El valor redondeado para la concentración del contaminante es: ", c)
        indice = k * (c - bplo)
        indice= round((indice + ilo))
        print("El indice de contaminación en Partículas Menores a 10 micrómetros (PM10) es: ", indice)
        
        
        print (f"la calidad del aire con un total de {valorpp} es mala ")
    if valorpp>=166 and valorpp<=220:
        bplo=round(random.uniform(0.155,valorpp - 0.001),3)
        print("El valor de BpLo es: ", bplo)
        ihi=200
        ilo=151
        k= ihi - ilo
        resta= round((valorpp - bplo),3)
        print("El valor de la resta es: ",resta)
        k= round((k / resta),2)
        print("El valor de K es: ",k)
        c=round(random.uniform(bplo+0.001,0.204),3)
        print("El valor redondeado para la concentración del contaminante es: ", c)
        print("\n")
        print("\n")
        print("apartado particulas menores a 10 micrometros")
        valorpp= round(random.uniform(216,354))
        print("El valor de bphi es: ", valorpp)
        
        bplo=round(random.uniform(215,valorpp - 1))
        print("El valor de bplo es: ", bplo)
        k= ihi - ilo
        resta= round((valorpp - bplo))
        print("El valor de la resta es: ",resta)
        k= round((k / resta),3)
        print("El valor de K es: ",k)
        c=round(random.uniform(bplo+1,354))
        print("El valor redondeado para la concentración del contaminante es: ", c)
        indice = k * (c - bplo)
        indice= round((indice + ilo))
        print("El indice de contaminación en Partículas Menores a 10 micrómetros (PM10) es: ", indice)
        
        
        print (f"la calidad del aire con un total de {valorpp} es muy mala ")
    if valorpp>=221 and valorpp<=550:
        
        bplo=round(random.uniform(0.205,valorpp - 0.001),3)
        print("El valor de BpLo es: ", bplo)
        ihi=200
        ilo=151
        k= ihi - ilo
        resta= round((valorpp - bplo),3)
        print("El valor de la resta es: ",resta)
        k= round((k / resta),2)
        print("El valor de K es: ",k)
        c=round(random.uniform(bplo+0.001,0.604),3)
        print("El valor redondeado para la concentración del contaminante es: ", c)
        print (f"la calidad del aire con un total de {valorpp} es extremadamente mala ")
        print("\n")
        print("\n")
        print("apartado particulas menores a 10 micrometros")
        valorpp= round(random.uniform(356,604))
        print("El valor de bphi es: ", valorpp)
        
        bplo=round(random.uniform(355,valorpp - 1))
        print("El valor de bplo es: ", bplo)
        k= ihi - ilo
        resta= round((valorpp - bplo))
        print("El valor de la resta es: ",resta)
        k= round((k / resta),3)
        print("El valor de K es: ",k)
        c=round(random.uniform(bplo+1,604))
        print("El valor redondeado para la concentración del contaminante es: ", c)
        indice = k * (c - bplo)
        indice= round((indice + ilo))
        print("El indice de contaminación en Partículas Menores a 10 micrómetros (PM10) es: ", indice)
