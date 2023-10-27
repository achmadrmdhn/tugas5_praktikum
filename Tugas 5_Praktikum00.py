print ("Nomor 1.")
motor = ["Vespa_Sprint", "Motor", "150cc", "Hijau_Tosca", "2"]
print(motor)

motor.append("25.000.000")
motor.append("Matic")
print(motor)

motor.insert(2, "Vespa")
print(motor)

print("")

print ("Nomor 2.")
print ("1. Menghitung persegi")
print ("2. Menghitung lingkaran")
print ("3. Menghitung segitiga")
luasbangundatar = input("Anda ingin menghitung apa ya?")

match luasbangundatar :
    case "1" :
        sisi = int (input("masukkan sisi :"))
        persegi = sisi*sisi
        print("hasil luas persegi :", persegi)
    case "2" :
        r = int(input("Masukkan jari-jari lingkaran :"))
        v = 3.14
        luas_lingkaran = v * r * r
        print("hasil luas lingkaran :", luas_lingkaran)
    case "3" :
        a = int (input("masukkan alas :"))
        t = int (input("masukkan tinggi :"))
        luas_segitiga = a*t/2
        print("hasil luas segitiga :", luas_segitiga)
    case _ :
        print("masukkan sesuai")

print("")

print("Nomor 3.-Tugas Asdos")
print("Menentukan bilangan ganjil-genap")
bilangan = int(input("Masukkan bilangan: "))

if bilangan % 2 == 0:
    print("Bilangan", bilangan, "Adalah bilangan genap.")
else:
    print("Bilangan", bilangan, "Adalah bilangan ganjil.")