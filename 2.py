
l1=int(input("Prima latura= "))
l2=int(input("A doua latura= "))
l3=int(input("A treia latura latura= "))
if (l1<32000) and (l2<32000) and (l3<32000):
    if (l1<(l2+l3)) and (l2<(l1+l3)) and (l3<(l2+l1)):
     print ('Triunghi')
    else:
     print ('Nu este triunghi')
else:
    print ('Eroare')