
a=int(input('Nr concurentului = '))
if (a<100):
    if (a%4==1):
        print('alb')
    elif (a%4==2):
        print('rosie')
    elif (a%4==3):
        print('albastru')
    elif (a%4==0):
        print('negru')
else :
    print('Eroare')