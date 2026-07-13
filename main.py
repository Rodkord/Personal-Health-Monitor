
trii= 0
numb=[5,10,15,20,25]
for a in numb:
    for b in range(len(numb)):
        if numb[a] >= numb[b+1]:
           trii= numb[a]
           numb[a]= numb[b+1]
           numb[b+1]= trii
   print("the smallest=", numb[0])
   print("the biggest=",numb[]
   