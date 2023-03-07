# -*- coding: utf-8 -*-
import csv
import datetime



#üst sınıf
class Pizza:
    def get_description(self): 
        return self.__class__.__name__

    def get_fiyat(self): 
        return self.__class__.fiyat

#alt sınıflar
class Klasik(Pizza):
    fiyat = 35

    def __init__(self):
        
        self.description = "Malzemeler-> kaşar, sucuk"
        print(self.description +"\n")

class Margarita(Pizza):
    fiyat = 30

    def __init__(self):
        self.description = "Malzemeler-> mozarella, domates"
        print(self.description +"\n")

class TurkPizza(Pizza):
    fiyat = 29

    def __init__(self):
        self.description = "Malzemeler-> pastırma, domates, sucuk, kaşar "
        print(self.description +"\n")

class SadePizza(Pizza):
    fiyat = 20
    def __init__(self):
        self.description = "Malzemeler-> "
        print(self.description +"\n")


#ek malzeme üst sınıf
class Decorator(Pizza):
    def __init__(self, Ek):
        self.component = Ek

    def get_fiyat(self):
        return self.component.get_fiyat() + \
          Pizza.get_fiyat(self)

    def get_description(self):
        return self.component.get_description() + \
          ' ;' + Pizza.get_description(self)
    
#ek malzeme alt sınıflar
class Zeytin(Decorator):
    fiyat = 1.99

    def __init__(self, Ek):
        Decorator.__init__(self, Ek)


class Mantar(Decorator):
    fiyat = 2.99

    def __init__(self, Ek):
        Decorator.__init__(self, Ek)


class Peynir(Decorator):
    fiyat = 3.99

    def __init__(self, Ek):
        Decorator.__init__(self, Ek)


class Et(Decorator):
    fiyat = 8.99

    def __init__(self, Ek):
        Decorator.__init__(self, Ek)


class Sogan(Decorator):
    fiyat = 4.99

    def __init__(self, Ek):
        Decorator.__init__(self, Ek)


class Misir(Decorator):
    fiyat = 0.99

    def __init__(self, Ek):
        Decorator.__init__(self, Ek)

#işlem fonksiyonu
def main():
    with open("Menu.txt") as Main_menu:
        for i in Main_menu:
            print(i, end="")

    class_dict = {1: Klasik, 
                  2: Margarita, 
                  3: TurkPizza, 
                  4: SadePizza, 
                  5: Zeytin, 
                  6: Mantar, 
                  7: Peynir, 
                  8: Et, 
                  9: Sogan, 
                  10: Misir}

    print("sadece(1,2,3,4)")
    secki = input("\nLütfen Pizzanızı Seçiniz : ")

    while True:
        if secki in ["1", "2", "3", "4"]:
            break
        else:
            secki = input("Geçersiz seçim. Lütfen tekrar deneyin: ")

    siparis = class_dict[int(secki)]()

    # ek malzeme kısmı
    ek_malzemeler = ["5", "6", "7", "8", "9", "10"]
    hata = ""

    while hata not in ["tamam"]:
        print("giriş şekli [5, 6, 7, 8, 9, 10] şeklinde olmalıdır.\n (Siparişinizi Onaylamak İçin 'tamam' yazınız)")
        hata = input("Ek malzeme isterseniz giriniz-> ")
        if hata in ek_malzemeler:
            siparis = class_dict[int(hata)](siparis)
        elif hata == "tamam":
            break

    print("\n" + siparis.get_description().strip() + ", " + str(siparis.get_fiyat()) + " TL")

    print("\n")

    #Sipariş Bilgi Kartı oluşturuyoruz.
    print("            Sipariş Bilgilerini giriniz\n")
    isim = input("İsim-> ")
    kimlik_no = input("TC no-> ")
    while True:
        kimlik_no = input("TC no-> ")
        if len(kimlik_no) == 11:
            break
        else:
            print("Geçersiz TC no. Lütfen tekrar deneyin.")

    kart_no = input("Kart no -> ")
    kart_sifre = input("Kart şifresi-> ")
    
    siparisler = datetime.datetime.now()
    with open('siparis.database.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['isim', 'kimlik_no', 'kart_no', 'kart_sifre', 'aciklama', 'tarih'])

    with open('siparis.database.csv', 'a') as siparisler:
        siparisler = csv.writer(siparisler, delimiter=',')
        siparisler.writerow([isim, kimlik_no, kart_no, kart_sifre, siparis.get_description(), siparisler])

    print("Siparişiniz Onaylandı.")
    print()
    
main()