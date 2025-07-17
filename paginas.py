

def pag(par_impar):
    if par_impar == 1:
        for x in range(lim_inf,lim_sup+1):
            if x % 2 == 0:
                print(",",x,end=" ")
    elif par_impar == 2:
        for x in range(lim_inf,lim_sup+1):
            if x % 2 == 1:
                print(",",x,end=" ")
    else:
        print("Ingrese una opción válida")


lim_inf = int(input("Ingrese el limite inferior\n"))
lim_sup = int(input("Ingrese el limite superior\n"))

par_impar = int(input("Quiere par o impar?\n1. par\n2. impar\n"))
pag(par_impar)