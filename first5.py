# DİCTİONARY 

# ANAHTAR = DEĞER 
# KEY = VALUE 


kişi = {"isim" : "ali", "yas" : 20, "cinsiyet" : "m", "hobbies" : ["cinema", "concer", "yazılım"]}

# dict larda KEYLER str veya int olmak zorunda ANCAK VALUE değer her şey olabilir 

# print(kişi)    dersek olduğu gibi çıktı verir fakat içinden bir değeri istiyorsak : 

# print(kişi["isim"])   çıktıyı ali verir
# print(kişi["hobbies"])          ['cinema', 'concer', 'yazılım']    çıktısnı verir

# bu şekilde elemanlara teker teker ulaşabiliriz

# dict içinde bir anahtarı vs değiştirmek istersek şu şekil yapıyoruz :

# print(kişi)               {'isim': 'ali', 'yas': 20, 'cinsiyet': 'm', 'hobbies': ['cinema', 'concer', 'yazılım']}
# kişi["isim"] = "ahmet"
# print(kişi)               {'isim': 'ahmet', 'yas': 20, 'cinsiyet': 'm', 'hobbies': ['cinema', 'concer', 'yazılım']}
 
#  aynı anda hem ismini hem de yaşını değiştirmek için yani birden çok değer değiştirmek için update fonk kullanırız

# kişi.update({"isim" : "ahmet", "yas" : 30})
# print(kişi)


# print(kişi)
# kişi["id"] = 12345
# print(kişi)                {'isim': 'ali', 'yas': 20, 'cinsiyet': 'm', 'hobbies': ['cinema', 'concer', 'yazılım'], 'id': 12345}  


# dict de silmek için :
# del kişi["cinsiyet"] 
# -----------------------



# dict lerde for döngüsü : 


# for x in kişi:
#     print(x)  = isim
#                 yas                FOR DÖNGÜSÜYLE HERHANGİ BİR FOR DÖNGÜSÜ YAZDIRMAK İSTERSEK,        
#                 cinsiyet              FOR DÖNGÜSÜNDEKİ DEĞİŞKEN ANAHTARLARIN YERİNE GEÇİYOR, DEĞERLERİN YERİNE GEÇMİYOR 
#                 hobbies


# for x in kişi:
#     print(kişi[x])         ali
#                            20                 BU ŞEKİLDE YAZARSAK BİZE DEĞERLERİ GÖSTERİR
#                            m
#                            ['cinema', 'concer', 'yazılım']



# BEN SADECE KEY LERDEN OLUŞAN BİR LİSTE DÖNDÜRDÜRMEK İSTERSEM 

# print(kişi.keys())         dict_keys(['isim', 'yas', 'cinsiyet', 'hobbies'])
# print(kişi.values())         dict_values(['ali', 20, 'm', ['cinema', 'concer', 'yazılım']])
# print(kişi.items())         dict_items([('isim', 'ali'), ('yas', 20), ('cinsiyet', 'm'), ('hobbies', ['cinema', 'concer', 'yazılım'])])

# for k, v in kişi.items():
#     print(k,v)              isim ali
#                             yas 20
#                             cinsiyet m
#                             hobbies ['cinema', 'concer', 'yazılım']

# eğer listede olmayan bir seyi yazdırmak istersek ama error vermesin dersek :

# # print(kişi.get("id"))            bu bize none ifadesini döndürür
# print(kişi.get("id","bulunamadı"))   çıktıyı bulunamadı olarak verdi çünkü ikisi de listede yoksa ikinci oln vermesini istediği mesaj oldu


