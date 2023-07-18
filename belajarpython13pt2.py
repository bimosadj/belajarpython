# operator dalam bentuk methods

# merubah case dari string

# merubah semua ke upper case

salam = "bro!"
print("normal = " + salam)
salam = salam.upper ()
print ("upper = " + salam)

# merubah semua ke lower case
alay = "bacot kau dek"
print ("normal =" + alay)
alay = alay.lower ()
print ("lower = " + alay) 

# pengecekan dengan isX method

# contoh pengecekan lower case
salam = "sist"
apakah_lower = salam.islower() # hasilnya bool
print (salam + " is lower = " + str(apakah_lower)) 
apakah_upper = salam.isupper () #hasilnya bool
print (salam + "is upper =" + str(apakah_upper))

# isalpha () <== untuk mengecek semuanya huruf
# isalnum () <== huruf dan angka
# isdecimal () <=== untuk angka saja
# isspace () <== spasi, tab , newline \n
# istitle () <=== semua kata dimulai dengan huruf besar

judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle () #hasilnya bool

print (judul + " is title = " +str(cek_judul))

# mengecek komponen starswith () endswith  <== keren
cek_star = "Freya Istri Aying".startswith("Freya")
print ("star = " + str(cek_star))

cek_end = "Freya Istri Aying".endswith("Aying")
print ("star = " + str(cek_end))

# penggabungan komponen join () split ()
pisah = ['aying','sayang','freya']
gabungan = ','.join(pisah)
print (pisah)
print (gabungan)

gabungan = ' '.join(pisah)
print (gabungan)

gabungan = 'ehm'.join(pisah)
print (gabungan)

gabungan = "akuehmsayangehmfreya"
print (gabungan.split('ehm'))


