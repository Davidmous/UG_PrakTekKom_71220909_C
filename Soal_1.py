print("==========================")
print("Operasi Matematika")
print("1. Jumlah   [+]")
print("2. Kurang   [-]")
print("3. Kali     [*]")
print("4. Bagi     [/]")
def penjumlahan():
    Menu=="1" 
    Jumlah=a+b
    return Jumlah
def pengurangan():
    Menu=="2" 
    Kurang=a-b
    return Kurang
def perkalian():
    Menu=="3" 
    Kali=a*b
    return Kali
def pembagian():
    Menu=="4"
    Bagi=a//b
    return Bagi

print("==========================")
Menu= input("Pilihan Operasi (1/2/3/4) :")
print("==========================")
a=int(input("Masukan Bilangan Pertama :"))
b=int(input("Masukan Bilangan Kedua :"))

if Menu=="1" :
    print("Hasil Operasi dari", a,'+', b, '=', penjumlahan())
elif Menu=='2' :
     print("Hasil Operasi dari", a,'-', b, '=', pengurangan())
elif Menu=='3' :
     print("Hasil Operasi dari", a,'*', b, '=', perkalian())
elif Menu=='4' :
     print("Hasil Operasi dari", a,'/', b, '=', pembagian())
#Created by David
