print("="*20 , "KASIR" , "="*20)
harga = int(input('\nHarga Barang: '))
pilih = input("Apakah anda membeli barang lagi? [yes/no]: ")


for i in pilih :
    if pilih == 'yes': 
        print(harga)
        harga += harga
    elif pilih == 'no':
        print("TOTAL BELANJA: " , harga )
    else:
        print('INVALID')

print()