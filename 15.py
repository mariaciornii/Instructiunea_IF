
n=int(input('Introduceti locul lui Radu dupa medie = '))
if (n>0) and (n<=125):
    if (n<=25):
        print ('A')
    elif (n>25) and (n<=50):
        print ('B')
    elif (n>50) and (n<=75):
        print ('C')
    elif (n>75) and (n<=100):
        print ('D')
    elif (n>100) and (n<=125):
        print ('E')
else:
    print ('Eroare')