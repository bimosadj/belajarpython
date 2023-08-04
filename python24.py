# latihan perulangan membuat segitiga

sisi = 10

# 1.Menggunakan for

# dummy variabel

print("awal dari for")
count = 1
for i in range(sisi):
    print ("*"*count)
    count += 1
    
print ("akhir dari for\n")
# 2.Menggunakan while

print("awal dari while")
count = 1
while True:
    print ("*"*count)
    count +=1

    if count > sisi:
        break
print("akhir dari while\n")

# 3.Hanya ganjil saja

print("awal dari while")
count = 1
while True:
    if(count%2):
    #print jika ganjil
    print("*"*count)
    count += 1
    
    else:
    # akan kembali keatas jika ganjil
        count += 1
        continue 
    
    # Akan break jika count melebihi sisi   
    if count > sisi:
        break

print("akhir dari while\n")

