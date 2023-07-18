# oprasi logika atau boolean

# not, or,and xor

# not
print ('===NOT===') 
a = True
c = not a
print ('data a =',a)
print ('-----------NOT')
print ('data c =',c)

 #or (Jika salah satu nilainya true ,maka hasil true)
print ('===OR===') 
a = False
b= False
c = a or b
print (a,'OR',b,'=',c)
a = False
b = True
c = a or b
print (a,'OR',b,'=',c)
a = True
b= False
c = a or  b
print (a,'OR',b,'=',c)
a = True
b= True
c = a or b
print (a,'OR',b,'=',c)

# AND (Jika dua buah nilai true ,maka hasil true)
print ('===AND===') 
a = False
b= False
c = a and b
print (a,'AND',b,'=',c)
a = False
b = True
c = a and b
print (a,'AND',b,'=',c)
a = True
b= False
c = a and  b
print (a,'AND',b,'=',c)
a = True
b= True
c = a and  b
print (a,'AND',b,'=',c)

# AND (akan true jika salah satu true,sisanya akan false)
print ('===XOR===') 
a = False
b= False
c = a ^ b
print (a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b
print (a,'XOR',b,'=',c)
a = True
b= False
c = a ^ b
print (a,'XOR',b,'=',c)
a = True
b= True
c = a ^ b
print (a,'XOR',b,'=',c)















