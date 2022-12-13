# integer, float ve type fonksiyonu 

# integer = tam sayı = 3
# float = ondalık sayı = 3.0


# sayı1 = 5
# sayı2 = 3.8
# print(type(sayı1))                    type komutu içerisine yazdığımız komutun hangi veri tipinde olduğunu gösteriyor sayı1 = int
# print(type(sayı2))  = float

# sayı1 = 5 ** 100 
# sayı2 = 22 / 7
# # print(sayı1)      bu şekilde büyük işlemleri kolaylıkla yapılabilir
# print(sayı2) 

# matematiksel işlemler 
# toplama +
# çıkarma - 
# çarpma *
# üssü **
# bölme /
# tamsayı bölmesi //
# mutlak değer abs
# yuvarlama round

# print(3 + 4)   = 7
# print(3 - 4)   = -1
# print(3 * 4)   = 12
# print(16 / 5)  = 3.2
# print(16 // 5)    = 3           bu ifade // bölme işleminin sadece tam sayı kısmını yazdırıyor
# print(3 ** 4)     = 81          bu ** 3 üzeri 4 anlamına geliyor
# print(abs(-2))    = 2           abs mutlak değer fonksiyonudur içerisine ister int ister float yazabilirsin
# print(abs(-2.16))   = 2.16
# print(round(22 / 7))  = 3         normalde 22 / 7 sonucu ondalık bir sayı fakat round komutu sayıyı yuvarladı
# print(round(3.864546725)) = 4      çıktıyı 4 verdi çünkü hangi tam sayıya daha yakınsa ona yuvarlar
# print(round(3.879684,3))    = 3.88   şimdi buradaki virgülden sonraki 3 sayısı noktadan sonraki üç sayıyı da açıktıda gösteriyor demektir
#                                      879 değil de 88 demesi 879 u 880 e yuvarladı ve 0 ı değersiz gördüğü için çıktıda sadece 88 sayısını verdi
#                                      noktadan sonraki sayı 878 olsaydı cıktıda 879 olacaktı 

# print(round(3.879684,4))   = 3.8797      uzun basamaklı işlemler yaparken tüm ondalık ayıyı görmek istemezsek 
#                                            noktadan sonraki ilk 4 basamağı bu şekilde görebiliriz

# python da işlem önceliği :
# parantez, çarpma, bölme, toplama, çıkarma 
# print((3 + 2) * 4 + 3)   = 23     ilk önce parantez içi 5 çıktı sonra 5 çarpı 4 = 20 eder, +3 = 23 eder 



# Karşılaştırma operatörleri 
# eşittir ==
# küçüktür <
# büyüktür >
# küçük eşittir <=
# büyük eşittir >=
# eşit değildir !

# print(3 == 5)    = False
# print(3 == 3)    = True      BOOLEAN
# print(3 = 3)           dersek yanlış olur çünkü 3 e 3 ü atıyormuşuz gibi olur  
# sayı = 3               tek = eşittir python da atama işlemidir, şu sayıya eşittir olarak kullanamayız 



# sayı1 = 7
# sayı2 = 10

# print(sayı1 < sayı2)   = True
# print(sayı1 > sayı2)   = False
# print(sayı1 != sayı2)    = True      çünkü ünlemin anlamı bunlar eşit değil dimi tarzında bir şey... kürtçe sanki, buraya çöp dökülüür :)
# print(10 <= 10)      = True 



# a = 1 
# b = a 
# a = 5
# print(b)    = 1    hemen 5 olur diye atlamayın çünkü ilk a daki değeri b ye verdik sonraki a değeri b yi etkilemez !!!!!



# STRİNG VE İNTEGERLARI BİRBİRİNE ÇEVİRME

# sayı1 = "100"
# sayı2 = 100
# print(type(sayı1))     = str
# print(type(sayı2))     = int
# print(sayı1 == sayı2)  = False çünkü biri str biri int    str deki 100 bir sayısal değer ifade etmez sadece parantez içerisinde bir metin

# sayı1 = "100"
# sayı2 = 100
# sayı3 = int(sayı1)
# print(sayı2 == sayı3)         şimdi True oldu çünkü sayı1 i int e çevirdik 

# sayı1 = "100asd"
# sayı2 = int(sayı1)
# print(sayı2)             error çünkü sayı1 i int e çeviremeyiz içerisinde harflerde var 

# sayı = int(3.9)
# print(sayı)           = 3       ondalık ifadeyi int e çevirdi noktadan sonrasını almayarak, 
#                                  noktadan sonrası 9 ama 4 e yuvarlamadı çünkü bu yuvarlama işlemi değil 






# k = 1 
# # k = k + 2
# # print(k)         3 verir çıktı olarak ama bu şekilde uzatmak istemeyiz kısa yoldan şunu yaparız :
# !!!!!!!      k += 2       !!!!!!!!!!

# veya         k *= 2
#              k /= 2      gibi gibi kısa yoldan yapabilirsin 

