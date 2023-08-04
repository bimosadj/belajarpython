# latihan 4
# belajar casting
# merubah dari satu tipe data ke tipe lain

# INTEGER
data_int = 100
print("====INTEGER====")
print("data =", data_int, "type=", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)  # akan false nilai jika int = 0
print("data =", data_float, ",type =", type(data_float))
print("data =", data_str, ",type =", type(data_str))
print("data =", data_bool, ",type =", type(data_bool))

# FLOAT
print("====FLOAT====")
data_float = 1
print("data =", data_float, "type =", type(data_float))

data_int = int(data_float)  # akan dibulatkan kebawah
data_str = str(data_float)
data_bool = bool(data_float)  # akan false jika nilai int = 0
print("data =", data_int, "type =", type(data_int))
print("data =", data_str, "type =", type(data_str))
print("data =", data_bool, "type =", type(data_bool))

# BOOLEAN
print("====BOOLEAN====")
data_float = False
print("data =", data_bool, "type =", type(data_bool))

data_int = int(data_bool)  # akan dibulatkan kebawah
data_str = str(data_bool)
data_bool = float(data_bool)  # akan false jika nilai int = 0
print("data =", data_int, "type =", type(data_int))
print("data =", data_str, "type =", type(data_str))
print("data =", data_float, "type =", type(data_float))
