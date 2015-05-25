import random

__author__ = 'fredy'

def aleatorios(m,M,d):
    vector = []
    for i in range(d):
        vector.append(random.uniform(m,M))
    return vector