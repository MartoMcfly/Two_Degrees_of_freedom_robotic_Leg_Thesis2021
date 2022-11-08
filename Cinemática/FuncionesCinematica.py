#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 21:41:22 2021

@author: Jaime Nunez
"""

import sympy as sp
import numpy as np

def Rotacion(TipoR):
    
    #Rotacion del Sistema p,u,v,w
    vars=sp.symbols('alpha phi theta')
    
    #Tipo de Rotacion: X-Alpha,Y-Phi,Z-Theta
    if TipoR=='RotacionX':
        MatrizRotacion=sp.Matrix([[1,0,0,0],
        [0,sp.cos(vars[0]),-1*sp.sin(vars[0]),0],
        [0,sp.sin(vars[0]),sp.cos(vars[0]),0],
        [0,0,0,1]])
        
    elif TipoR=='RotacionY':
          MatrizRotacion=sp.Matrix([[sp.cos(vars[1]),0,sp.sin(vars[1]),0],
          [0,1,0,0],
          [-sp.sin(vars[1]),0,sp.cos(vars[1]),0],
          [0,0,0,1]])
          
    elif TipoR=='RotacionZ':
          MatrizRotacion=sp.Matrix([[sp.cos(vars[2]),-sp.sin(vars[2]),0,0],
           [sp.sin(vars[2]),sp.cos(vars[2]),0,0],
           [0,0,1,0],
           [0,0,0,1]])       
   
    return MatrizRotacion

def Traslacion(TipoT):
    
    #Parametros Denavit Hartenberg
    vars=sp.symbols('a d')
    
    #Traslacion en el eje X:a
    if TipoT=='TraslacionX':
        MatrizTraslacion=sp.Matrix([[1,0,0,vars[0]],
        [0,1,0,0],
        [0,0,1,0],
        [0,0,0,1]])
    
    #Traslacion en el eje Z:d
    elif TipoT=='TraslacionZ':
          MatrizTraslacion=sp.Matrix([[1,0,0,0],
          [0,1,0,0],
          [0,0,1,vars[1]],
          [0,0,0,1]])
                                
    return MatrizTraslacion

def MatrizTransformacion(A,D,Alfa,Theta,Char,Vars):
    
    #Variables
    vars=sp.symbols('a d alfa theta')
    
    if Char=='CD':
        
        #Matriz Transformacion Homogenea Denavit Hartenberg Simbolica
        MS=Rotacion('RotacionZ')*(Traslacion('TraslacionX'))
        
        #Matriz Transformacion Homogenea Denavit Hartenberg Numerica
        MN=MS.subs({vars[0]:A, vars[1]:D, vars[2]:Alfa, vars[3]:Theta})
    elif Char=='CI':
        
        #Matriz Transformacion Homogenea Denavit Hartenberg Simbolica
        MS=Rotacion('RotacionZ')*(Traslacion('TraslacionX'))
        
        #Matriz Transformacion Homogenea Denavit Hartenberg Numerica
        MN=MS.subs({vars[0]:A, vars[1]:D, vars[2]:Alfa, vars[3]:Vars})
        
    return MN, MS, vars
    
def  Jacobiana(ThetaI,T0i):
    
     #Variables
     vars=sp.symbols('q1 q2')
     Vars=sp.Matrix([vars])
     
     #Estado Operacional End Effector
     T0i=T0i.tolist()
     x=T0i[0][3]
     y=T0i[1][3]
     z=T0i[2][3]
     
     #Angulos de Euler:Roll-Pitch-Yaw
     TH=sp.atan2(-T0i[2][0],(sp.sqrt((T0i[2][1])**2 + (T0i[2][2])**2)))
     PH=sp.atan2(T0i[1][0],T0i[0][0])
     PS=sp.atan2(T0i[2][1],T0i[2][2])
            
     #Matriz Jacobiana Simbolica
     MS=sp.Matrix([x,y], dtype='object')
     JS=MS.jacobian(Vars)
     
     #Matrix Jacobiana Numerica
     JN=JS.subs({vars[0]:ThetaI[0], Vars[1]:ThetaI[1]})
     
     
     return JN,JS
 

  