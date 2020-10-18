
n=int(input('Nr sosirii lui Ionel = '))
if n>0:
    if (n%4==0):
        print ('Casuta ',n//4)
    elif (n%4!=0):
        print ('Casuta ',(n//4)+1)
else:
    print('Eroare')
