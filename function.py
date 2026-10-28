def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def keliling_persegi_panjang(panjang, lebar):
    return 2 * (panjang + lebar)

def ubah_angka(angka):
    return f"{angka:,}".replace(",", ".")
    
def check_stock(stock, jumlah):
    return stock >= jumlah

print(luas_persegi_panjang(20, 50))
print(keliling_persegi_panjang(20, 50))
print(ubah_angka(125000))
print(check_stock(50, 20))
print(check_stock(20, 50))


