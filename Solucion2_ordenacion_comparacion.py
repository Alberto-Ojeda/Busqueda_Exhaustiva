# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 12:05:51 2021

@author: alberto
"""
import matplotlib.pyplot as plt
import pandas as pd
import time
class Puntos:
    def __init__(self, x,y,rango):
        self.x=x
        self.y=y
        self.rango=rango
    def get_X(self):
        return self.x
    def set_X(self,x):
        self.x=x
    def get_Y(self):
        return self.y
    def set_Y(self,y):
        self.y=y
    def get_rango(self):
        return self.rango
    def set_rango(self,rango):
        self.rango=rango       
    
def abrirExcel(archivo,puntos):
    datos=pd.read_excel(archivo, "Hoja2")
    x=datos.x
    y=datos.y
    #print(x)
    #print(y)
    for i in range (0, len(datos.x)):
        puntos.append(Puntos(x[i],y[i],0))
    plt.plot(x,y,'o',picker=5)
    
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("puntos")
    #plt.legend(('burbuja',' '),prop={'size':10},loc='upper right')
    plt.grid()
    plt.show()     
   
    for a in range (0, len(datos.x)):
        lista_nueva.append(x[a])
    for a in range (0, len(datos.x)):
        lista_nueva1.append(y[a])
    for a in range (0, len(datos.x)):
        lista_nueva2.append(puntos[i].get_rango())        
    

    eleccion_metodo(lista_nueva)
    for i in range (0, len(datos.x)):
       puntos1.append(Puntos(lista_nueva[i],lista_nueva1[i],puntos[i].get_rango()))
   
   
    inicioB=1
    finalB=len(puntos)
    comparacion(inicioB,finalB)
 

 
    
    for i in range(0,len(puntos)):
        rangosnew.append(puntos1[i].get_rango())        
           
    for i, label in enumerate(rangosnew):
       plt.text(lista_nueva[i], lista_nueva1[i],label)   

def comparacion(inicioB,finalB):
    for i in range(inicioB,finalB):
        for j in range(0,i):
          if(puntos1[i].get_X()!=puntos1[j].get_X() and puntos1[i].get_Y()>puntos1[j].get_Y()):
                puntos1[i].rango=puntos1[i].rango+1
          else:
                 puntos1[i].rango=puntos1[i].rango+0

def burbuja(lista):
    
    for b in range(1, len(lista_nueva)):
        for c in range (0, len(lista_nueva)-b):
            if(lista_nueva[c]>lista_nueva[c+1]):
                aux=lista_nueva[c]
                aux1=lista_nueva1[c]
                lista_nueva[c]=lista_nueva[c+1]
                lista_nueva1[c]=lista_nueva1[c+1]
                lista_nueva[c+1]=aux
                lista_nueva1[c+1]=aux1

def metodo_inserccion_directa(lista):
    for j in range(1,len(lista_nueva)):
        i=j-1
        x=lista_nueva[j]
        y=lista_nueva1[j]
        while(x<lista_nueva[i] and i>=0):
            lista_nueva[i+1]=lista_nueva[i]
            lista_nueva1[i+1]=lista_nueva1[i]
            i=i-1
        lista_nueva[i+1]=x
        lista_nueva1[i+1]=y

def quicksort(lista):
    izquierda = []
    centro = []
    derecha = []
    if len(lista_nueva) > 1:
        pivote = lista_nueva[0]
        for i in lista_nueva:
      
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            elif i > pivote:
                derecha.append(i)
        #quicksort(izquierda)+centro+quicksort(derecha)
        for b in range(1, len(lista_nueva)):
            for c in range (0, len(lista_nueva)-b):
                if(lista_nueva[c]>lista_nueva[c+1]):
                    aux=lista_nueva[c]
                    aux1=lista_nueva1[c]
                    lista_nueva[c]=lista_nueva[c+1]
                    lista_nueva1[c]=lista_nueva1[c+1]
                    lista_nueva[c+1]=aux
                    lista_nueva1[c+1]=aux1

def ordenamiento_shell(lista):
    incremento=len(lista_nueva)
    while(incremento>0):
        for i in range(incremento,len(lista_nueva)):
            j=i
            temporal=lista_nueva[i]
            temporal1=lista_nueva1[i]
            while((j>=incremento) and (lista[j-incremento]>temporal)):
                lista_nueva[j]=lista_nueva[j-incremento]
                lista_nueva1[j]=lista_nueva1[j-incremento]
                j=j-incremento
            lista_nueva[j]=temporal
            lista_nueva1[j]=temporal1
        if(incremento==2):incremento=1
        else:
            incremento=int(incremento/2.2)
def ordenamientoPorSeleccion(lista):
   for llenarRanura in range(len(lista_nueva)-1,0,-1):
       posicionDelMayor=0
       for ubicacion in range(1,llenarRanura+1):
           if lista_nueva[ubicacion]>lista_nueva[posicionDelMayor]:
               posicionDelMayor = ubicacion

       temp = lista_nueva[llenarRanura]
       temp1 = lista_nueva1[llenarRanura]
       lista_nueva[llenarRanura] = lista_nueva[posicionDelMayor]
       lista_nueva1[llenarRanura] = lista_nueva1[posicionDelMayor]
       lista_nueva[posicionDelMayor] = temp
       lista_nueva1[posicionDelMayor] = temp1

def eleccion_metodo(lista):
    n=len(lista_nueva)
    if n<=100:
        print("METODO BURBUJA")
        burbuja(lista_nueva)
    elif n<=500:
        print("METODO INSERCIÓN DIRECTA")
        metodo_inserccion_directa(lista_nueva)              
    elif n<=1000:
        print("METODO POR SELECCIÓN")
        ordenamientoPorSeleccion(lista_nueva) 
    elif n<=2000:
        print("METODO SHELL")
        ordenamiento_shell(lista_nueva)
    elif n>=2001:
        print("METODO QUICKSHORT")
        quicksort(lista_nueva)

                
    
          


    
if __name__=="__main__":
    inicio=time.perf_counter()
    lista_nueva=[]
    lista_nueva1=[]
    lista_nueva2=[]
    rangosnew=[]
    puntos=[]
    puntos1=[]
    abrirExcel('Datos.xls', puntos)    
    
    for i in range(0,len(puntos)):
        print(puntos1[i].get_X(),'-',puntos1[i].get_Y(),'-',puntos1[i].get_rango())    
    final=time.perf_counter()
    print("el tiempo de ejecución es por calcular la cantidad de rangos de :",len(puntos),"es", final-inicio)
    
    
    