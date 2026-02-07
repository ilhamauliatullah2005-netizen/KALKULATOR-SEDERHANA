#buatlah program kalkulator sederhana menggunakan 4 pilihan operasi (tambah, bagi, kali,dan pengurangan)

print("==================")
print("Numerare Numerarus")
print("==================")

print("powered by:")
print("Ilham Auliatullah_250511022 \n")

print("===============")
print("Pilihan Operasi")
print("1. Tambah")
print("2. Kurang")
print("3. Bagi")
print("4. Kali")
print("===============")

operasi = int(input("Masukan pilihan operasi (1/2/3/4) : "))

if operasi == 1:
    x = int (input("Masukan nilai pertama : "))
    y = int (input("Masukan nilai kedua : "))
    z = x + y
    print("Hasilnya adalah : ", x, "+", y, "=", z)
    print("=========================")

elif operasi == 2:
    x = int (input("Masukan nilai pertama : "))
    y = int (input("Masukan nilai kedua : "))
    z = x - y
    print("Hasilnya adalah : ", x, "+", y, "=", z)
    print("=========================")

elif operasi == 3:
    x = float (input("Masukan nilai pertama : "))
    y = float (input("Masukan nilai kedua : "))
    z = x / y
    print("Hasilnya adalah : ", x, "/", y, "=", z)
    print("=========================")

elif operasi == 4:
    x = int (input("Masukan nilai pertama : "))
    y = int (input("Masukan nilai kedua : "))
    z = x * y
    print("Hasilnya adalah : ", x, "x", y, "=", z)
    print("=========================")