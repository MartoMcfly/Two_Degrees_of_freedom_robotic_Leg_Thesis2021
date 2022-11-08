#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 19:30:27 2021
@author Jaime Nunez
"""

#Imports
import numpy as np
from FuncionesCinematica import MatrizTransformacion 
from FuncionesCinematica import Jacobiana

#Posicion operacional segun la posicion articular
def Cinematica_Directa(a,d,Alfa,Theta,t, Vars):
    #Posicion Operacional
    Px1=[]
    Px2=[]
    x_data=[Px1,Px2]

    Py1=[]
    Py2=[]
    y_data=[Py1,Py2]
    
    Pz1=[]
    Pz2=[]
    z_data=[Pz1,Pz2]
                                  
    #Matriz de Transformacion Homogenea  
    for i in range(len(t)):
        T01=MatrizTransformacion(a[0],d[0],Alfa[0],Theta[0,i],'CD', Vars)[0]
        T12=MatrizTransformacion(a[1],d[1],Alfa[1],Theta[1,i],'CD', Vars)[0]
        T02=T01*T12
    
        #Posicion Operacional: Base
        BaseX=T01[0,3]
        BaseY=T01[1,3]
        BaseZ=T01[2,3]
        
        Px1.append(BaseX)
        Py1.append(BaseY)
        Pz1.append(BaseZ)
        
        #Posicion Operacional: End Effector
        EFX=T02[0,3]
        EFY=T02[1,3]
        EFZ=T02[2,3]
        
        Px2.append(EFX)
        Py2.append(EFY)
        Pz2.append(EFZ)
        
    return x_data, y_data, z_data

#Posicion articular segun la posicion operacional
def Cinematica_Inversa(a,d,Alfa,ThetaI,P,t,Char,Vars): 
       #Posicion Articular Calculada
       Theta=[]
       
       #Matriz Transformacion Homogenea
       T01=MatrizTransformacion(a[0],d[0],Alfa[0],ThetaI[0],Char, Vars[0])[0]
       T12=MatrizTransformacion(a[1],d[1],Alfa[1],ThetaI[1],Char, Vars[1])[0]
       T02=T01*T12
       
       for i in range(len(P[0])-1):
           #Posicion articular calculada[Rad]
           Theta=[]
           
           #Aumento en el plano operacional
           P0=[P[0][i],P[1][i]]
           P1=[P[0][i+1],P[1][i+1]]
           DP=np.subtract(P1,P0)
           
           #Transformacion entre Espacios Vectoriales
           J=np.array(Jacobiana(ThetaI,T02)[0],dtype='float')
           
           #Evitar singularidades de la Trayectoria
           if np.linalg.det(J)!=0:
               DQ=(np.linalg.inv(J)).dot(DP)
           else:
               #Factor para el nuevo P:XYZ Operacional
               Betha=np.deg2rad(1)
               NThetaI=np.add(ThetaI,Betha).tolist()
               J=J=Jacobiana(ThetaI,T02)[0]
               DQ=(np.linalg.inv(J)).dot(DP)
              
           #Posicion Articular Calculada
           Q1=np.add(ThetaI,DQ).tolist()
           Theta.append(Q1)
           ThetaI=Q1 
           
           
       return Theta
       
               
       
   
       

