# bagian break looping

# contoh 1

angka = 0

while angka < 5:
    angka += 1
    print (f" angka sekarang = {angka}")

    if angka ==3:
        print ("nice!!")
        break

    print("wassup!!!")
print("cukuuuup!!")


# contoh 2

data_int = int(input("hitung sampai = "))

angka = 0

while angka < 5:
    angka += 1
    print(f"count = {angka}")
    # print (f" angka sekarang --> {angka}")

    if angka ==3:
        print ("nice!!")
        break

    print("wassup!!!")
print("cukuuuup!!")


