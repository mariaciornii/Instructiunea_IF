n1=int(input('Introduceti 1 nr = '))
n2=int(input('Introduceti 2 nr = '))
if ((n2%2)==0) and ((n1%2)==0):
    if (n2>n1):
        print (n2)
    else:
        print (n1)
if ((n2%2)==0) and ((n1%2)!=0):
    print (n2)
elif ((n1%2)==0) and ((n2%2)!=0):
    print (n1)
if ((n1%2)!=0) and ((n2%2)!=0):
    print ('Nu exista nr par')
