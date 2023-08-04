# continue , pass, break

# pass--> dia berfungsi sebagai dummy, tidak bisa di eksekusi
#ini bagian pass
angka = 0

while angka < 5:
    angka += 1

    if angka == 3:
        pass #tidak akan dieksekusi
   
    print(angka)

# #ini bagian continue

angka = 0
print (f"angka sekarang -> {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}") #aksi 1

    if angka == 3:
        print ("nice!!")
        continue #akan membuat loop loncar keatas

    print("whassuppp bro!!")#aksi 2

print ("finish")

##bagian break ada di next filee






