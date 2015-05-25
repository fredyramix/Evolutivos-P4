__author__ = 'fredy'

def modificar_exitos(e,Q,n):
    float(e)
    float(Q)
    C=0.817
    if e/n == 0.5:
        return Q
    elif e/n < 0.5:
        return Q*C
    else:
        return Q/C