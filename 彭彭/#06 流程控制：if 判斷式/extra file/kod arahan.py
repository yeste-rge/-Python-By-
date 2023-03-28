x=int(input("Masukkan umur anda:"))
if x > 59:
    print("Anda ialah seorang warga emas.")
elif x > 30:
    print("Anda ialah seorang  dewasa.")
elif x > 14:
    print("Anda ialah seorang belia(青年).")
elif x > 12:
    print("Anda ialah seorang awal remaja.")
elif x < 13:
    print("Anda masih kanak-kanak.")
else:
    print("Saya tak tahu awak umur di mana?")