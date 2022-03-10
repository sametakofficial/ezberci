import random
import time
from re import A


print("Ezberleme yardımcısına hoş geldiniz. Programı kapatmak için q tuşuna basın")

data_1 = input("Ezberlenecek birinci değer: ")
answer_1 = input("Ezberlenecek birinci değerin cevabı: ")

data_2 = input("Ezberlenecek ikinci değer: ")
answer_2 = input("Ezberlenecek ikinci değerin cevabı: ")

data_3 = input("Ezberlenecek üçüncü değer: ")
answer_3 = input("Ezberlenecek üçüncü değerin cevabı: ")

data_4 = input("Ezberlenecek dördüncü değer: ")
answer_4 = input("Ezberlenecek dördüncü değerin cevabı: ")

data_5 = input("Ezberlenecek beşinci değer: ")
answer_5 = input("Ezberlenecek beşinci değerin cevabı: ")

data_6 = input("Ezberlenecek altıncı değer: ")
answer_6 = input("Ezberlenecek altıncı değerin cevabı: ")

secenek=[data_1,data_2,data_3,data_4,data_5,data_6]


while True:
        karistirici = random.choice(secenek)
        print(karistirici,'\'nın')
        secim = input('değeri nedir?')
        if karistirici==data_1:
            if secim==answer_1:
                print("")
                time.sleep(0.5)
                print("Doğru cevap")
                print("")
                time.sleep(1) 
            else:
                print("")
                time.sleep(0.5)
                print("Yanlış Cevap. Doğru cevap:")
                time.sleep(0.5)
                print(answer_1)
                print("")
                time.sleep(1)     
        elif karistirici==data_2:
            if secim==answer_2:
                print("")
                time.sleep(0.5)
                print("Doğru cevap")
                print("")
                time.sleep(1) 
            else:
                print("")
                time.sleep(0.5)
                print("Yanlış Cevap. Doğru cevap:")
                time.sleep(0.5)
                print(answer_2)
                print("")
                time.sleep(1) 
        elif karistirici==data_3:
            if secim==answer_3:
                print("")
                time.sleep(0.5)
                print("Doğru cevap")
                print("")
                time.sleep(1) 
            else:
                print("")
                time.sleep(0.5)
                print("Yanlış Cevap. Doğru cevap:")
                time.sleep(0.5)
                print(answer_3)
                print("")
                time.sleep(1) 
        elif karistirici==data_4:
            if secim==answer_4:
                print("")
                time.sleep(0.5)
                print("Doğru cevap")
                print("")
                time.sleep(1) 
            else:
                print("")
                time.sleep(0.5)
                print("Yanlış Cevap. Doğru cevap:")
                time.sleep(0.5)
                print(answer_4)
                print("")
                time.sleep(1) 
        elif karistirici==data_5:
            if secim==answer_5:
                print("")
                time.sleep(0.5)
                print("Doğru cevap")
                print("")
                time.sleep(1) 
            else:
                print("")
                time.sleep(0.5)
                print("Yanlış Cevap. Doğru cevap:")
                time.sleep(0.5)
                print(answer_5)
                print("")
                time.sleep(1) 
        elif karistirici==data_6:
            if secim==answer_6:
                print("")
                time.sleep(0.5)
                print("Doğru cevap")
                print("")
                time.sleep(1) 
            else:
                print("")
                time.sleep(0.5)
                print("Yanlış Cevap. Doğru cevap:")
                time.sleep(0.5)
                print(answer_6)
                print("")
                time.sleep(1) 
        elif karistirici=='q':
            print("Çıkılıyor...")
            break