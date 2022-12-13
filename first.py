# print("Hello World")        stringler tırnak içerisine yazılır

# print('Ali' nin evi)      dersek hata alırız çünkü string kesme işaretine bakar ve cümle bitti sanar

# print("Ali'nin evi")      dersek doğru olur çünkü çift tırnak ile başladık bir sonraki çift tırnağa kadar cümlemiz devam ediyor

# print('Ali\'nin Evi')       burada ters slaş koyduk ve hata vermedi. buradaki slaşın anlamı benden sonraki ilk karakterin önemli olmadığıdır

# print("""Merhaba 
# Dünya
#                              bu stringde ,üç tırnak, alt alta yazmamıza yarıyor ve istediğimiz kadar satır atlayabiliyoruz 
# :)""")

# print("Hello\nWorld")          \n satır atlamaya yarıyor. üç nokta kullanmayıp bu şekilde kısayoldan alt satıra atlatıyor

# print("Hello\tWorld")          \t tab a bastığımızı düşünecek ve aralarına 4 boşluk bırakacak. ne kadar t koyarsan \t\t\t bu şekilde o kadar boşluk bırakır

# bir program yazarken her string i yazmakla uğraşmayacağız,bazı bilgileri bilgisayarın aklında tutmasını sağlayacağız bunu da değişkenler deriz 

# mesaj = "Hello World"
# print(mesaj)                işte bu bir değişkendir ve yeni bir değişken atayana kadar mesaj olarak yazdırınca çıktı olarak hello worl ifadesini alacağız

# mesaj = "Hello"
# mesaj2 = "Dünya"
# print(mesaj + " " + mesaj2)    burada araya boş tırnak koyma sebebimiz eğer koymazsak python helloworld ü birleşik yazar bu şekilde

# Name = "Aleyna"       #  komut içerisindeki bir harfi ararken köşeli parantez kullanırız ve saymaya 0 dan başlanır!!!!!
# print(Name[3])        # köşeli parantez komuttaki 3. harfimiz ne ise bize onu veriyor yani y harfi çıktı
# print(Name[-2])       # -2 dediğimiz eksiler burada sondan başladığını gösteriyor aleyna konutundaki n harfini alır bu yüzden 
# print(Name[0:4])        karakter içerisindeki birkaç harfi almak için böyle yaparız yalnız önemli !!!
#                             ilk komut 0 yazdık ilk komutu alır, yani A harfinden başladı 
#                    fakat ikinci komutta 4 yazdık 3 e kadar olan kısmı alıyor yani aleyn değil aley almış oldu 

# print(Name[::2])       ilk iki nokta baştan başladığını ikinci iki nokta sonuna kadar olduğunu 
#                         ve 2 sayısı baştan başlayıp ikişer olarak sona kadar gitmesini gösteriyor   bu str aleyna komutundan Aen çıktısını verir
                        #  2 yerine 3 yazarsak üçer üçer gitmesini sağlarız aynı şekilde uzun karakterlerde 4 5 6... diye yapabiliriz

# print(Name[::-1])         bu eksi ile yazıldığı zaman sondan başlar. bu sefer ilk iki nokta son harfi, ikinci iki nokta başı temsil eder.
#                             eksi bir yazmamız da sondan başa hepsini yazdırır yani çıktımız anyelA olarak gelir                

# print(Name.upper() )       upper dediğimizde komuttaki tüm yazıyı caps lock şeklinde yazar yani çıktımız ALEYNA olarak gelir 
#                                  AMA bu sadece bu str için geçerli yani Name imiz hala Aleyna olarak duruyor. 
# eğer bundan sonraki her çıktıyı bu şekilde büyük almak istiyorsam bilgisayara tekrar bu şekilde bir komut vermem gerekiyor ,aşağıdaki gibi :),
# Name = Name.upper()
# print(Name)             bu şekilde artık bundan sonraki komutlar ALEYNA olarak devam edecek

# Name = Name.upper()      
# print(Name)                     ALEYNA                     burada upper hepsini büyütüyor
# Name = Name.lower()
# print(Name)                     aleyna                            lower hepsini küçültüyor
# Name = Name.capitalize()
# print(Name)                     Aleyna                            capitalize sadece baş harfi büyültüyor 


# print(Name.startswith("na"))     startswith komuttaki başlangıç harfini gösterir aleyna na ile başlamadığı için False sonucunu verir 
# print(Name.startswith("Al"))                  Al ile başladığı için bu çıktıyı True olarak verir 

# print(Name.endswith("en"))           endswith de bittiği harfleri ifade eder aleyna en ile bitmediği için sonuç False oldu
# print(Name.endswith("na"))             bu str miz True olarak çıktı verir çünkü aleyna na ile bitiyor :)

# print(len(Name))                    len fonksiyonu komuttaki harf sayısı gösterir. aleyna komutunda 6 harf vardır 

# print("Merhaba" + " " + Name)       str içinde toplama işlemi yan yana yazmak anlamına gelir. = Merhaba Aleyna olarak çıktı verir.

# print(Name * 4)                       str içinde * yani çarpma işlemi ard arda verilen komut kadar misal 4 yazdık. 4 tane Aleyna çıktısı verir 
#                   = AleynaAleynaAleynaAleyna çıktı bu 


# isim = "Ali"
# yaş = "20"
# print("{} , {} yaşındadır".format(isim,yaş))            burada birinci değişken birinci kümenin içine ikinci ikinciye 
#                                                               yani çıktımız "Ali 20 yaşındadır"

# isim = "Nergis"
# mesaj = "hello"
# print("{} sayed {}".format(isim,mesaj))                 formattan sonrakilere dikkat sırayla koyuyor çünkü

# print(f"{} {} dedi")                      # f string süslü parantez içlerine yazacağımız şeylerin değişken olduğunun farkında ve onların içerisine yazdıracak
# print(f"{isim} {mesaj} dedi")                   çıktısı Nergis hello dedi 

print(everything will be okey)
