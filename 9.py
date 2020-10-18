
Bilealbemari=int(input('Nr de bile albe mari = '))
Bilealbemici=int(input('Nr de bilea albe mici = '))
Bilerosiimari=int(input('Nr de bile rosii mari = '))
Bilerosiimici=int(input('Nr de bile rosii mici = '))
bileverzimari=int(input('Nr de bile verzi mari = '))
bileverzimici=int(input('Nr de bile verzi mici = '))
total=Bilealbemari+Bilealbemici+Bilerosiimari+Bilerosiimici+bileverzimari+bileverzimici
totalmici=Bilealbemici+Bilerosiimici+bileverzimici
totalmari=Bilealbemari+Bilerosiimari+bileverzimari
totalverzi=bileverzimari+bileverzimici
totalrosii=Bilerosiimari+Bilerosiimici
totalalbe=Bilealbemari+Bilealbemici
print ('Totalul = ',total)
if (Bilealbemari>=0) and (Bilealbemici>=0) and (Bilerosiimari>=0) and (Bilealbemici>=0) and (bileverzimari>=0) and (bileverzimici>=0):
    if (totalmici>totalmari):
        print (totalmici, 'mici')
    elif (totalmari>totalmici):
        print (totalmari, 'mari')
    if (totalalbe>totalrosii) and (totalalbe>totalverzi):
        print (totalalbe, 'albe')
    elif (totalrosii>totalalbe) and (totalrosii>totalverzi):
        print (totalrosii, 'rosii')
    elif (totalverzi>totalalbe) and (totalverzi>totalrosii):
        print (totalverzi, 'verzi')
else:
    print ('Eroare')