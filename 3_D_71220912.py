tinggi = eval(input('\nMasukkan Angka: '))

for baris in range(tinggi):
    print(" " * (tinggi - baris) , end=" ")
    print("* " * (baris + 1))
for baris in range(1,tinggi):
    print(" " * (baris + 1) , end=" ") 
    print("* " * (tinggi-baris))

print ()