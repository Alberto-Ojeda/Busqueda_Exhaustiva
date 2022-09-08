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
    for i in range (0, len(datos.x)):
        puntos.append(Puntos(x[i],y[i],0))
    plt.plot(x,y,'o',picker=5)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("puntos")
    plt.grid()
    inicioA=0
    finalA=int(len(puntos)/2)
    
    inicioB=1
    finalB=len(puntos)
    perpendicular(inicioA, finalA)
    perpendicular(finalA, finalB)
    perpendicular_2(inicioA, finalA,finalB)
    perpendicular_3(inicioB,finalB)

    for i in range(0,len(puntos)):
        print(puntos[i].get_X(),'-',puntos[i].get_Y(),'-',puntos[i].get_rango())
    for i in range(0,len(puntos)):
        rangosnew.append(puntos[i].get_rango())        
           
    for i, label in enumerate(rangosnew):
       plt.text(x[i], y[i],label)
   
    plt.show()


def perpendicular(inicio,final):
    for i in range(inicio,final):
        for j in range(i+1,final):
            if(puntos[i].get_X()>=puntos[j].get_X() and puntos[i].get_Y()>=puntos[j].get_Y()):
              puntos[i].rango=puntos[i].rango+1


def perpendicular_2(inicioA,finalA,finalB):
    for i in range(inicioA,finalA):
        for j in range(finalA,finalB):
          if(puntos[i].get_X()>=puntos[j].get_X() and puntos[i].get_Y()>=puntos[j].get_Y()):
              puntos[i].rango=puntos[i].rango+1

def perpendicular_3(inicioB,finalB):
    for i in range(inicioB,finalB):
        for j in range(0,i):
         # print(j)
          if(puntos[i].get_X()>=puntos[j].get_X() and puntos[i].get_Y()>=puntos[j].get_Y()):
              puntos[i].rango=puntos[i].rango+1


def decremento (num):
    num-=1
    if num >= 0:
 
        decremento(num)
    
if __name__=="__main__":
    inicio=time.perf_counter()
    rangosnew=[]
    puntos=[]  
    abrirExcel('Datos2.xls', puntos)
    final=time.perf_counter()
    print("el tiempo de ejecución es por calcular la cantidad de rangos de :",len(puntos),"es", final-inicio)

    
    
