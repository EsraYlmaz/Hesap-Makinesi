İlkSayi = float(input("Birinci Sayıyı Giriniz: "))
İkinciSayi = float(input("İkinci Sayıyı Giriniz: "))
hesap_makinesi = input(""" Yapmak İstediğiniz İşlemi Giriniz (Toplama: +, Çıkarma: - Çaprma: *, Bölme: /): """)

if hesap_makinesi == "+":
    print("Sonuç: "+ str (İlkSayi + İkinciSayi))

elif hesap_makinesi == "-":
    print("Sonuç: "+ str (İlkSayi - İkinciSayi))

elif hesap_makinesi == "*":
    print("Sonuç: "+ str (İlkSayi * İkinciSayi))

elif hesap_makinesi == "/":
    print("Sonuç: "+ str (İlkSayi / İkinciSayi))

      
