jarakPerjalanan = 100
konsumsiBBM = 40
hargaBensin = 10000
sisaBensin = 1.5
# seluruh total jarak perjalanan
totalJarakPerjalanan = jarakPerjalanan * 2
# total bensin yang di butuhkan
totalBensin = totalJarakPerjalanan / konsumsiBBM
# bensin yang di beli
bensinYangDibeli = totalBensin - sisaBensin
# total 
TotalBiayaBeliBensin = bensinYangDibeli * hargaBensin


print("Total jarak perjalanan:", totalJarakPerjalanan, "Kilometer")
print("Bensin yang di butuhkan:", totalBensin, "Liter")
print("Bensin yang dibeli:", bensinYangDibeli, "Liter")
print("Total biaya beli bensin: Rp", TotalBiayaBeliBensin)