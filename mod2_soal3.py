suhu = int(input("Masukan suhu: "))
tekanan = int(input("Masukan tekanan: "))

if suhu > 1000:
    if tekanan > 50:
        print("MELTDOWN! SEGERA EVAKUASI!")
    else:
        print("Bahaya Suhu: Segera Turunkan Daya!")
elif suhu > 500:
    if tekanan > 30:
        print("Tekanan Tidak Stabil")
    else:
        print("Operasi Reaktor Normal")
else:
    print("Reaktor Belum Cukup Panas")

pompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"

print(suhu)
print(tekanan)
print(pompa)
kunci = "Python"
password = input ("Masukan password : ")
if password == kunci:
    print ("Password Benar")
else :
    print ("Password Salah")




angka = int (int("Masukan sebuah bilangan :"))
if angka > 0 :
    print ("Angka merupakan bilangan positif")
elif angka < 0 :
    print ("Angka merupakan bilangan Negatif")
else:
    print ("Angka merupakan 0")