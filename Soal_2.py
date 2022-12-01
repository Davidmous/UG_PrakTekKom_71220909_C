print("Pemeriksa Kelipatan 9")
kelip=int(input("Masukan Kelipatan 9 yang ingin diperiksa:"))

def kelipatan_sembilan():
   angka=kelip % 9
   return angka


if kelipatan_sembilan() == 0:
    print("Benar")
else:
    print("Salah")
