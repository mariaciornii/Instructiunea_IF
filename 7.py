n1=int(input('Introduceti primul nr = '))
n2=int(input('Introduceti al doilea nr = '))
n3=int(input('Introduceti al treilea nr = '))
a=n1+n2
if (n1>=0) and (n2>=0) and (n3>=0):
    if (n2>n3):
        print (n2)
    elif (n3>n2):
        print (n3)
elif (n1<0) or (n2<0) or (n3<0):
    print (a)

