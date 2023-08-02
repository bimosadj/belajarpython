# string
data = "ini adalah string"
print (data)
print (type(data))
# 1.cara membuat string
'''
    1.dengan menggunakan single quote '...'
    2.dengan menggunakan double quote "..."
'''

data = 'menggunakan sigle quote'
print (data)

data = "menggunakan double quote"
print (data)



# 2.menggunakan tanda \

# membuat tanda ' menjadi string
print ('p balap')
print ('g\'day, isn\'t it?')

# print ('"Halo,apa kabar"')
# print ("'Halo,apa kabar'")
# print ("ini adalah hari jum'at")
# backlash
print ("C:\\user\\jamal")

# tab 
print ("ucup\tjamal,gelud")

# backspace
print ("ucup \bjamal,jadi deket")

# newline
print ("baris pertama.\nbaris kedua.") #LF -->line feed -> unix, macos, linux
print ("baris pertama.\rbaris kedua.") #CR  -->carriage return -> commodore, acorn, lisp
print ("baris pertama.\r\nbaris kedua") #CRLF -->line feed carriage return -> dipakai oleh windows

# 3.string literall atau raw

# hati-hati
print ('C:\\new folder')#akan salah pathnya

# menggunakan raw string
print (r'C:\new folder')

# mulri line literal string
print ("""
Nama : jamal
Kelas : xii smk
""")
       
# multiline literal string dan RAW
print (r"""
Nama : jamal
Kelas : xii smk \new noermal
Website : www.jamal.com/newID
""")
