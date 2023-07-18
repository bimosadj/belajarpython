# komparasi dan logika
# membuat gabungan arefa rentang dari angka 


# +++++3-----10++++

inputUser = float(input("masukan angka yang bernilai\nkurang dari 3\natau\nlebih besar dari 10\n:"))

# +++++3-----
# memeriksa angka kurang dari 3
iskurangDari = (inputUser < 3)
print("kurang dari 3=",iskurangDari)

# -----10+++++
# memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print ("Lebih dari 10=",isLebihDari)

# +++++3------10+++++
iscorrect = iskurangDari or isLebihDari
print("angka yang anda masukan : ",iscorrect)

# -----3++++++++++10-----
# kasus irisan 
print("\n",10*"=","\n")
inputUser = float(input("masukan angka yang bernilai\nlebih dari 3\ndan\nkurang dari 10\n:"))

# -----3+++++++++
# lebih dari 3
islebihDari = inputUser > 3
print ("Lebih dari 3 = ",islebihDari)


# ++++++++++10-----
# kurang dari
iskurangDari = inputUser < 10
print ("Kurang dari 10 = ",iskurangDari)

# -----3++++++++++10-----
iscorrect = iskurangDari and isLebihDari
print("angka yang anda masukan : ",iscorrect)

