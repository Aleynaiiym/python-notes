# LİSTELER

# renkler = []    köşeli parantezin içine bir şey yazmasan bile python bunu bir liste olarak alır 

# renkler = ["siyah", "beyaz", "mavi", "sarı", "yeşil"]
# print(type(renkler))   = list 
# print(renkler)    = ['siyah', 'beyaz', 'mavi', 'sarı', 'yeşil']    print, içine veriğimiz komutu yazdırmaya yarıyor listleler de direk ekrana yazdırılabilen yapılar

# print(len(renkler))  = 5    listenin içinde 5 tane eleman vardır bunu len fonksiyonuyla öğreniyoruz

# print(renkler[1])   = beyaz   1 dedik neden siyah değil beyaz oldu deme çünkü ilk saymaya sıfırdan başlıyor yani sıfır yazsaydık siyah çıktısı verirdi

# print(renkler[2:])   = mavi sarı yeşil renklerini verir çünkü 2 den başladı ve iki noktadan sonra bir şey yazmadık ve liste sonuna kadar olan yerleri verdi
# print(renkler[1:4])   = beyaz mavi sarı verdi çünkü ilk komut 1 ve 1 beyaz a denk geliyor.  4 e kadar dedik ama 4 ü almaz 3 e kadar olan kısmı alır 3 de sarıya denk geliyor
# print(renkler[:2])    = siyah beyaz  çıktısını verir neden? sayı yazmadan iki nokta koyarsak listenin başından başla komutudur bu
# print(renkler[::2])   = siyah mavi yeşil çıktısı gelir çünkü ::2 yani sıfırdan başla sonuna kadar 2 şer 2 şer git demek oluyor bu
# print(renkler[1:4:2])  = beyaz sarı çıktısı gelir 1. sayıdan başla 4 e kadar 2 şer anlamı vardır 






# append metodu   listenin sonuna eleman eklemeye yarar 
# insert metodu   elemanı listenin aralarına bir yere eklemek için kullanılır 
# remove metodu   listeden bir elemanı silmeye yarıyor
# extend metodu   listeye birden fazla eleman eklemeye yarar
# pop metodu      listenin en son elemanını siler ve silinen dersek hangisini sildiğini de gösterir 
# reserve metodu  listeyi tersten sıralamaya yarıyor 
# sort ve sorted metodu  sort listeyi alfabetik sırayla yazdırır sorted ise 

# renkler = ["siyah", "beyaz", "mavi", "sarı", "yeşil"]

# renkler.append("gri")
# print(renkler)           = ["siyah", "beyaz", "mavi", "sarı", "yeşil", "gri"]

# renkler.insert(0, "lila")            sıfır yerine 2 deseydik mavinin yerine lila gelecekti ve mavinin sayısı artık 3 olacaktı 
# print(renkler)            = ["lila", siyah", "beyaz", "mavi", "sarı", "yeşil", "gri"]

# renkler.remove("sarı")
# print(renkler)             = ['siyah', 'beyaz', 'mavi', 'yeşil']  sarıyı sildi

# renkler2 = ["turuncu", "pembe"]
# renkler.append(renkler2)
# print(renkler)                =  ['siyah', 'beyaz', 'mavi', 'yeşil'['turuncu', 'pembe']]   append ile yaparsak hata vermez listenin sonuna ekler
#                                      fakat renkler2 listesini olduğu gibi alır. farkettiysen turuncu ve pembe hala parantez içinde ayrı 

# renkler.extend(renkler2)
# print(renkler)               = ['siyah', 'beyaz', 'mavi', 'sarı', 'yeşil', 'turuncu', 'pembe'] extend sayesinde turuncu ve pembeyi ayrı ayrı eleman olarak aldı 


# renkler.pop()
# print(renkler)                = ['siyah', 'beyaz', 'mavi', 'sarı']  yeşili sildi
# silinen = renkler.pop()
# print(silinen)                = yeşil      silinen komutu pop un listede neyi sildiğini gösteriyor

# renkler.reverse()
# print(renkler)                 = ['yeşil', 'sarı', 'mavi', 'beyaz', 'siyah'] listeyi tersten sıraladı

# renkler.sort()
# print(renkler)                 = ['beyaz', 'mavi', 'sarı', 'siyah', 'yeşil']  listeyi alfabetik sırayla yazdırdı. 
#                                                   liste içinde sayılar olsaydı onları da küçükten büyüğe sıralardı


# renkler.sort()
# renkler.reverse()
# print(renkler)                   = ['yeşil', 'siyah', 'sarı', 'mavi', 'beyaz'] bu şekilde sort önce listeyi alfabetik olarak sıraladı
#                                                                              sonrasında reverse de ters olarak sıraladı 
#                                                                       numara listemiz olsaydı büyükten küçüğe sıralanmış olacaktı

# üstteki gibi uğraşmak istemiyor ve alfabetik olarak sondan sıralamak istiyorsak şöyle yaparız: 

# renkler.sort(reverse= True)
# print(renkler)                = ['yeşil', 'siyah', 'sarı', 'mavi', 'beyaz'] bu şekilde kısa yoldan da yapılabilir

# bu şekilde sıraladığımız zaman listemiz artık değişmiş oluyor ilk hali kalmıyor 
# ama biz sadece o anlık değişsin diğer zamanlar ilk hali kalsın istersek şunu kullanıyoruz

# print(renkler)
# liste2 = sorted(renkler)               ['siyah', 'beyaz', 'mavi', 'sarı', 'yeşil']
# print(liste2)                          ['beyaz', 'mavi', 'sarı', 'siyah', 'yeşil']
# print(renkler)                         ['siyah', 'beyaz', 'mavi', 'sarı', 'yeşil']

# bir listeyi sıralamak istiyorsak ancak ilk hali bozulmasın dersek bu şekilde sorted fonksiyonundan yapmalıyız




# min listedeki en küçük olanı gösterir
# max listedeki en büyük olanı gösterir
# sum listedeki sayıların toplamını verir
# for döngüsü ile listeyi yazdırabiliriz 
# enumerate fonksiyonu bir listeyi numaralandırmaya yarıyor  
# in liste içinde bir şeyi sorabiliriz True False sonuçlarını verir
# join fonksiyonu listedeki elemanları birleştir, aralarına da tırnak içinde ne varsa onu koy boşluk olabilir virgül olabilir / olabilir 

# renkler = ["siyah", "beyaz", "mavi", "sarı", "yeşil"]
# sayılar = [1,2,56,8,7,4,0]

# print(min(renkler))   = beyaz. renkler listesinde alfebetik sırayla bakacaktır ve ilk olarak b geliyor
# print(min(sayılar))     = 0      sayılar listesindeki en küçük sayı 0 dır 
#                      MİN komutu küçükten başlayıp sıralamaz sadece en küçük olanı gösterir

# print(max(renkler))        = yeşil  alfabetik olarak en ileridekini verir
# print(max(sayılar))      = 56 en büyük değer budur

# print(sum(sayılar))       = 78    SUM listedeki sayıların toplamını verir
# print(sum(renkler))    bunun çıktısını vermez çünkü liste içinde toplanabilecek değer yok 

# for k in renkler:        iki nokta üst üste bütün döngülerde olmazsa olmazdır        
#     print(k)                k yerine istenilen harf veya kelime yazılabilir 
# siyah
# beyaz
# mavi                k önce siyahın yerine geçiyor ve siyahı yazdırıyor daha sonra beyaz mavi... bu şekilde sırayla hepsinin yerine geçip yazdırıyor 
# sarı
# yeşil


# print(list(enumerate(renkler)))       =    [(0, 'siyah'), (1, 'beyaz'), (2, 'mavi'), (3, 'sarı'), (4, 'yeşil')]

# eğer saymaya sıfırdan başlasın istemiyorsak şunu kullanırız:

# print(list(enumerate(renkler,start=3)))   =    [(3, 'siyah'), (4, 'beyaz'), (5, 'mavi'), (6, 'sarı'), (7, 'yeşil')]   numaralandırmaya 3 ten başladı 

# print("siyah" in renkler)      = True      in'in kullanımı: renkler listesinin içinde siyah var mı            
# print("gri" in renkler)         = False


# stringrenkler = " ".join(renkler)    = siyah beyaz mavi sarı yeşil      tırnka arasına boşluk yapmasaydık birleşik yazardı
# stringrenkler = ",".join(renkler)     = siyah,beyaz,mavi,sarı,yeşil     



# tirelere göre böleceğim ve her bir elemanı bir listeye atayacağım 

# renkler = ["siyah", "beyaz", "mavi", "sarı", "yeşil"]
# stringrenkler = "-".join(renkler)                       #  = siyah-beyaz-mavi-sarı-yeşil
# print(stringrenkler)

# renkler2 = stringrenkler.split("-")
# print(renkler2)                                        ['siyah', 'beyaz', 'mavi', 'sarı', 'yeşil'] hem tire olan yerden böldüm hem de ayrı ayrı tırnaklarla listelere böldüm

