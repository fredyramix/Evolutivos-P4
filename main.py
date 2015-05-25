# -*- encoding: utF-8 -*-
__author__ = 'fredy'
import random
from math import cos,sin
from math import pi
from funciones import *
from GeneraAleatorios import aleatorios
from Mutacion import Mutar
from VerificarExitos import modificar_exitos
from Comparacion import comparar
from Salida import Escribir




def main():
    variables = [[],[2,-65.536,65.536,1000,"funcion1.txt",10000],
                 [4,-5.12,5.12,100,"funcion2.txt",100000],
                 [2,-100,100,1,"funcion3.txt",100000],
                 [2,-100,100,1,"funcion4.txt",10000],
                 [4,-500,500,15,"funcion5.txt",10000],
                 [4,0,10,10000,"funcion6.txt",10000],
                 [2,-10,10,10,"funcion7.txt",10000],
                 []]
    pob = 20
    numerito = 20
    exitos = 0
    Q=[]
    f = raw_input("Ingresa el numero del ejercicio: \n")
    fun  = int(f)
    m =int(variables[fun][1])
    M =int(variables[fun][2])
    generaciones = variables[fun][5]
    #En este paso agregamos todas nuestras sigmas
    for b in range(0,pob):
        Q.append(variables[fun][3])
    d=int(variables[fun][0])
    #abrimos el archivo con el nombre de la función.
    outfile=open("Resultados/"+variables[fun][4],'w')
    #Comienza la población aleatoria
    poblacion = []
    for t in range(0,pob):
        poblacion.append(aleatorios(m,M,d))
    aptitudes=Elegir(fun,poblacion)
    a ="Poblacion Inicial:"
    print a
    Escribir(outfile,a)
    for  l in range(0,len(poblacion)):
        a = "Indiviuo: " +str(l)
        Escribir(outfile,a)
        a = "\tVector: "+ str(poblacion[l])
        Escribir(outfile,a)
        a= "\tAptitud: " + str(aptitudes[l])
        Escribir(outfile,a)
    mutaciones = []
    for f in range(0,len(poblacion)):
        mutaciones.append(Mutar(poblacion[f],Q[f]))
    aptitudeshijos = Elegir(fun,mutaciones)
    arregloexitos=[]
    for s in range(0,len(poblacion)):
        if comparar(aptitudes[s],aptitudeshijos[s]):
            arregloexitos.append(1)
            m = mutaciones[s]
            ap = aptitudeshijos[s]
            poblacion[s] = m[:] #sustituimos al padre
            aptitudes[s]=ap
        else:
            arregloexitos.append(0)
    g=0
    a = "======================================================================================================================"
    Escribir(outfile,a)
    print "Calculando...."
    while g != generaciones:
        for f in range(0,len(poblacion)):
            mutaciones[f]=Mutar(poblacion[f],Q[f])
        aptitudeshijos = Elegir(fun,mutaciones)
        for s in range(0,len(poblacion)):
            if comparar(aptitudes[s],aptitudeshijos[s]):
                ar= arregloexitos[s]
                arregloexitos[s] = arregloexitos[s]+1
                m = mutaciones[s]
                ap = aptitudeshijos[s]
                poblacion[s] = m[:] #sustituimos al padre
                aptitudes[s]=ap
            if g%numerito ==0:
                Q[s]=modificar_exitos(exitos,Q[s],numerito)
                exitos=0
        g = g+1
    dic = {}
    a= "Poblacion Final:"
    Escribir(outfile,a)

    for  l in range(0,len(poblacion)):
        a= "Indiviuo: " +str(l)
        print a
        Escribir(outfile,a)
        a= "\tVector: "+ str(poblacion[l])
        print a
        Escribir(outfile,a)
        a= "\tAptitud: " + str(aptitudes[l])
        print a
        Escribir(outfile,a)
        a ="\tSigma: " + str(Q[l])
        print a
        Escribir(outfile,a)
        dic[str(l)] = aptitudes[l]
    print dic
    diccionario = dic.items()
    diccionario.sort(key=lambda x: x[1])
    a= "================================El Mejor es==========================================================="
    Escribir(outfile,a)
    a= "Indiviuo: " + str(diccionario[0][0])
    Escribir(outfile,a)
    a= "\tVector: "+ str(poblacion[int(diccionario[0][0])])
    Escribir(outfile,a)
    a= "\tAptitud: " + str(aptitudes[int(diccionario[0][0])])
    Escribir(outfile,a)
    a= "\tSigma: " + str(Q[int(diccionario[0][0])])
    Escribir(outfile,a)
    outfile.close()
main()