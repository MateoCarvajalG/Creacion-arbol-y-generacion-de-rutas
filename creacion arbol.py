# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 18:01:33 2020

@author: MATEO
"""

class Arbol(object):
  def __init__(self,elemento):
    self.hijos= []
    self.elemento = elemento
    
arbol = Arbol(1)


def agregarelemento(arbol,elemento,elementopadre):
    
    if arbol.elemento == elementopadre: 
        arbol.hijos.append(Arbol(elemento))
   #buscar arbol
    else:
       subarbol=buscararbol(arbol, elementopadre)
       subarbol.hijos.append(Arbol(elemento))
              
def buscararbol(arbol,elementoPadre):
    if arbol.elemento == elementoPadre:
        return arbol
    for subarbol in arbol.hijos:
        arbolbuscado= buscararbol(subarbol,elementoPadre)
        if arbolbuscado != None:
            return arbolbuscado
        
def crearutas(arbol,elemento): 
    for subarbol in arbol.hijos:
        if elemento == subarbol.elemento:
                ruta.append(elemento)
                elemento= arbol.elemento
                crearutas(arbol,elemento)
        
        for arbolito in subarbol.hijos: 
            if elemento == arbolito.elemento:
                ruta.append(elemento)
                elemento= subarbol.elemento
                crearutas(arbol,elemento)
                
            for hijos  in arbolito.hijos: 
                if elemento == hijos.elemento:
                    ruta.append(elemento)
                    elemento= arbolito.elemento
                    crearutas(arbol,elemento)
            
        
        
        
def preorden(arbol):
    print(arbol.elemento)
    for subarbol in arbol.hijos:
        preorden(subarbol)

agregarelemento(arbol, 2, 1)
agregarelemento(arbol, 3, 1)
agregarelemento(arbol, 4, 1)
agregarelemento(arbol, 5, 2)
agregarelemento(arbol, 6, 2)
agregarelemento(arbol, 7, 3)
agregarelemento(arbol, 10, 5)
agregarelemento(arbol, 8, 6)
agregarelemento(arbol, 9, 6)


ruta=[]
crearutas(arbol,10)
ruta.append(arbol.elemento)
