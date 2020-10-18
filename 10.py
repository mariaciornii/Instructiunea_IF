
gaini=int(input('Nr de gaini = '))
porumb=int(input('Nr de porumb = '))
t1=(porumb//gaini)
t2=(t1*gaini)
clapon=(porumb-t2)
if (clapon==0):
    print ('egalitate, fiecare are ',t1,' boabe')
else:
    print("Curcanul are cu ",clapon,' boabe mai mult')

