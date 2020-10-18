

ac=int(input('Introduceti anul curent = '))
lc=int(input('Introduceti luna curenta = '))
zc=int(input('Introduceti ziua curenta = '))
an=int(input('Introduceti anul nasterii = '))
ln=int(input('Introduceti luna nasterii = '))
zn=int(input('Introduceti ziua nasterii = '))
varsta=(ac-an)
if (ac>an):
    if lc<ln :
     print ((varsta-1))
    elif (lc==ln) and (zc<zn):
     print ((varsta-1))
    elif (lc==ln) and (zc>=zn):
     print (varsta)
    elif lc>ln :
        print (varsta)
else:
    print ('Eror')
