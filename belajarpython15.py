# width and multiline

# data

data_nama = "Ucup Surucup"
data_umur = 17
data_tinggi = 150.1
data_nomer_sepatu = 44

# string standard
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_nomer_sepatu}"
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# string multiline (dengan menggunakan enter,newline, \n)
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nsepatu = {data_nomer_sepatu}"
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# string multiline (kutip triplets)
data_string = f"""
nama = {data_nama} 
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomer_sepatu}
"""

print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# mengatur lebar
data_nama = "Ucup Surucup"
data_string = f"""
nama   = {data_nama:>5}
umur   = {data_umur:>5}
tinggi = {data_tinggi:>5}
sepatu = {data_nomer_sepatu:>5}
"""

print("\n"+5*"="+"Data String"+5*"=")
print(data_string)
