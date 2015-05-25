__author__ = 'fredy'
import random
from math import cos,sin,pi,sqrt,pow,tanh,e
def sumatoria(v):
    sumi = 0
    a=[[-32,-16,0,16,32,-32,-16,0,16,32,-32,-16,0,16,32,-32,16,0,16,32,-32,-16,0,16,32],
       [-32,-32,-32,-32,-32,-16,-16,-16,-16,-16,0,0,0,0,0,16,16,16,16,16,32,32,32,32,32,]]
    for i in range(1,26):
        sumi += ((1)/((i+pow((v[0]-a[0][i-1]),6)+pow((v[1]-a[1][i-1]),6))))
    return sumi

def evaluar1(v):
    fx = pow((0.002 + sumatoria(v)),-1)
    return fx


def sumatoria2(v):
    s=0
    for i in range(0,4):
        s=s+((v[i]**2)-10*cos(2*pi*v[i]))
    return s
def evaluar2(vector):
    fx = 10*4 + sumatoria2(vector)
    #print fx
    return fx

def evaluar3(v):
    #sin2(x) = 1/2 - 1/2 cos(2x)
    fx = 0.5 + (((1/2 - 1/2 *cos(2*(pow(v[0],2)-pow(v[1],2))))-0.5)/pow((1+0.001*(pow(v[0],2)+pow(v[1],2))),2))
    return fx
def evaluar4(v):
    fx = 0.5 + (cos(sin(abs(v[0]**2-v[1]**2))-0.5))/((1+0.001*(v[0]**2+v[1]**2))**2)
    return fx

def sumatoria5(v):
     sumi = 0
     for i in range(0,len(v)):sumi += (v[i] * sin(sqrt(abs(v[i]))))
     return sumi

def evaluar5(v):
    return  (418.9829*4 - sumatoria5(v))

def sumatoria6b(v,i):
    C=[[4.0,1.0,8.0,6.0,3.0,2.0,5.0,8.0,6.0,7.0],
       [4.0,1.0,8.0,6.0,7.0,9.0,3.0,1.0,2.0,3.0],
       [4.0,1.0,8.0,6.0,3.0,2.0,5.0,8.0,6.0,7.0],
       [4.0,1.0,8.0,6.0,7.0,9.0,3.0,1.0,2.0,3.0],]

    B=[1.0/10.0,2.0/10.0,2.0/10.0,4.0/10.0,4.0/10.0,6.0/10.0,3.0/10.0,7.0/10.0,5.0/10.0,5.0/10.0]
    sumi =0
    for j in range(1,5):
        sumi += (pow((v[j-1]-C[j-1][i-1]),2)+B[i-1])
    return sumi
def evaluar6(v):
    sumi = 0
    m=10
    for i in range(1,m+1):
        sumi += pow(sumatoria6b(v,i),-1)
    return -sumi

def evaluar7(v):
    sumi = 0
    suma = 0
    for i in range(1,6):
        sumi += (i*cos((i+1)*v[0]+i))
        suma += (i*cos((i+1)*v[1]+i))
    return sumi * suma

def t(i):
    return 0.1*(i-1)
def Y(i):
    return 58.81*(pow(1.27,t(i)))*tanh(3.013*t(i)+sin(2.13*t(i)))*cos(pow(e,0.507)*t(i))
def primera(v,i):
    return pow((v[0]*v[1]),t(i)) * tanh(v[2]*t(i)+sin(v[3]*t(i))) * cos(t(i)*pow(e,v[4]))-Y(i)

def evaluar8(v):
    sumi=0
    for i in range(1,25):
        sumi += pow(primera(v,i),2)
    return sumi
def Elegir(fun,poblacion):
    aptitudes=[]
    for f in range(0,len(poblacion)):
        if fun==1:
            aptitudes.append(evaluar1(poblacion[f]))
        elif fun==2:
            aptitudes.append(evaluar2(poblacion[f]))
        elif fun==4:
            aptitudes.append(evaluar3(poblacion[f]))
        elif fun==4:
            aptitudes.append(evaluar4(poblacion[f]))
        elif fun==5:
            aptitudes.append(evaluar5(poblacion[f]))
        elif fun==6:
            aptitudes.append(evaluar6(poblacion[f]))
        elif fun==7:
            aptitudes.append(evaluar7(poblacion[f]))
        elif fun==8:
            aptitudes.append(evaluar8(poblacion[f]))
    return aptitudes


#Aptitud Problema 5
'''	if(po==5):
		#print "cinco"
		for x in range(0,len(vector)):
			#print vector[i]
			absoluto=abs(vector[x])
			raiz=math.sqrt(absoluto)
			(math.sin(raiz)))
			fx+=((vector[x])*(math.sin(raiz)))
		fx=((418.9829*len(vector))-fx)
		return fx'''