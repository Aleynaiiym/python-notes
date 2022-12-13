# TUPLE AND SETS

# listelerin parantezi köşeli ama tuple ın normal parantez misal 

# demet = ("sarı", "mavi", "yeşil", "kırmızı", "siyah")
# print(type(demet))         = tuple çıktısı verir  
# print(len(demet))                             normal listelerdeki gibi eleman sayısını sorabiliriz
#         çünkü listelerde köşeli parantez [] kullanılırken tuple da normal (). oluşturduğumuz listenin cinsini de type fonk. ile öğrenmiş oluruz. 

# tuple lara herhangi bir eleman eklenemez, silinemez veya var olan herhangi bir elemanı değiştiremezsiniz


# kume = {"sarı", "mavi", "yeşil", "kırmızı", "siyah"}               #  kümenin parantezi süslü parantezdir
# print(type(kume)) 
# print(len(kume))     len fonk ile eleman sayısına ulaşabilriz 
# for renk in kume:
#     print(renk)        for döngüsüyle de yazdırabiliriz
#         ANCAK KUMELERİ FOR DÖNGÜSÜYLE SIRALADIĞIMIZDA HER SEFERİNDE FARKLI SONUÇ ÇIKACAKTIR BUNUN SEBEBİ KÜMELERN SIRASIZ BİR VERİ YAPISINA SAHİP OLMASI

# print(kume)
# kume.add("pembe")         # kümelerin belli bir sırası olmadığı için sonuna ekleme komutu olmaz o yüzden add komutu ile sadece ekleme yaparız
# print(kume)


# kümeden bir eleman çıkartmak istersek remove u kullancağız

# kume.remove("sarı")
# print(kume)            küme içerisinde sarı rengini çıkarmış oldu. AMA OLMAYAN BİR RENGİ ÇIKAR DESEK HATA VERİRDİ

# EĞER KÜME İÇERİSİNDE OLMAYAN BİR ELEMANI ÇIKARMAK İSTERSEK VE O ELEMAN ZATEN KÜMEDE YOKSA, AMA AKIŞTA HATA ALMASINI İSTEMİYORSAK DİSCARD FONK KULLANIRIZ

# kume.discard("gri")
# print(kume)               ZATEN KÜMEDE GRİ RENGİ YOK FAKAT YİNE DE HATA VERMEDEN NORMAL KÜMEMİZİ TEKRARDAN ÇIKTI VERDİ 

# DİSCARD İLE REMOVE ARASINDA ASLINDA FARK YOKTUR YANİ KÜMEDEN HERHANGİ BİR ŞEYİ ÇIKARABİLİR FAKAT OLMAYAN BİR ŞEYİ YALNIZCA DİSCARD HATA VERDİRMEZ 




# kume1 = {"sarı", "mavi", "yeşil", "kırmızı", "siyah"}
# kume2 = {"sarı", "mavi", "yeşil","beyaz", "gri"}

# iki kümedeki ortak olanları bulmak istersek intersection fonk yararlanırız  

# print(kume1.intersection(kume2))    = sarı mavi yeşil 
# print(kume2.intersection(kume1))    bu da aynı çıktıyı verir 

# birleştirmek isteseydik union fonk kullanacağız

# print(kume1.union(kume2))     =  {'siyah', 'mavi', 'gri', 'beyaz', 'sarı', 'kırmızı', 'yeşil'}

# birleştirme yaparken iki kümede de aynı olan ifadeleri 1 defa çıktıda gösterir

# küme 1 de olup küme 2 de olmayanları nasıl bulacağız dersek difference fonk kullanırız 

# print(kume1.difference(kume2))     kırmızı siyah    küme1 de olup küme2 de olmayanların çıktısı 
# print(kume2.difference(kume1))      gri beyaz          küme2 de olup küme1 de olmayanların çıktısı 

# print("sarı" in kume1)      True       in fonk da küme içinde sarı var mı diye sordurur varsa True yoksa False 

# print("beyaz" in kume1.union(kume2))     bu da True çıktısı verir yani bunun anlamı küme1 ve 2 birleşiminde beyaz var mı sorusudur




# bosliste1 = []  
# bosliste2 = list()     bu ikisi de boş bir listedir 

# bostuple1 = ()
# bostuple2 = tuple()    bu ikisi de boş birer tuple dır 

# boskume1 = set()       bu bir boş kümedir
# boskume2 = {}          bu bir boş küme değil bir dictionary yani sözlüktür 



# python = set("PYTHON")
# print(python)                {'P', 'Y', 'N', 'H', 'T', 'O'}        
           
#            SET BİR LİSTEYİ ELEMANLARINA AYIRIR 


# python = set([1,2,3,4,5])
# print(python)                 {1, 2, 3, 4, 5}     bir liste girersek set içine bunu da kümeye çevirir


# python = set((1,2,3,4,5))
# print(python)                  {1, 2, 3, 4, 5}      bir tuple girersek de bunu bize set kümeye veririr 



