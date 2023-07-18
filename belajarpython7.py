# latihan konversi satuan temperatur

# program konversi celcius ke satuan lain

print ("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float (input('masukan suhu dalam celcius : '))
print ("suhu adalah ",celcius, "celcius")

# reamur
reamur = (4/5) * celcius
print ("suhu dalam reamur adalah ",reamur,"reamur")

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32 
print ("suhu dalam fahrenheit adalah ",fahrenheit,"fahrenheit")

# kelvin
kelvin = celcius + 273
print ("suhu dalam kelvin adalah ",kelvin,"kelvin")


# pr
# tentukan rumus konversi fahrenheit ke kelvin
print ("\n PROGRAM KONVERSI TEMPERATUR\n")

fahrenheit = float(input('masukan suhu dalam fahrenheit : '))
print ("suhu adalah ",fahrenheit,"fahrenheit")

celcius = ((5/9)*fahrenheit)- 32 
kelvin = celcius + 273
print ("suhu dalam kelvin adalah ",kelvin,"kelvin")

# tentukan rumus konversi kelvin ke fahrenheit

print ("\n PROGRAM KONVERSI TEMPERATUR\n")

kelvin = float(input('masukan suhu dalam kelvin : '))
print ("suhu adalah ",kelvin,"kelvin")

celcius = kelvin - 273
kelvin = ((5/9)*fahrenheit)- 32 
print ("suhu dalam fahrenheit adalah ",fahrenheit,"fahrenheit")
