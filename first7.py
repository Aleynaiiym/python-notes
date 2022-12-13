# DÖNGÜLER 

# liste = (1,2,3,4,5,6)
# for rakam in liste:
#     print(rakam)

                                #    for dan sonra uzun uzun bir şey yazma i de geç
# isim = ("aleyna")
# for harf in isim:
#     print(harf)    


# demet = (1,2,3,4)
# for i in demet:
#     print(i)


# RANGE 

# for i in range(1,10):
#     print(i)                   ilk sayıyı dahil eder sonraki sayıyı dahil etmez yani çıktımız 1 den 9 a kadar 


# for i in range(1,17,2):      1 den başla 16 ya kadar ( 17 yi almaz) 2 şer olarak git 
#     print(i)                 


# for i in range(10)   başka sayı yazmazsan, sıfırdan alır 9 a kadar sayar


# sonuc = 1
# for i in range(0,10):
#     sonuc *= 2
# print(sonuc)              


# liste1 = ["a", "b", "c"]
# liste2 = [1,2,3]
# for harf in liste1:                for u içine yazdığımız için önce 123 oldu yani a önce 1 onra2 sonra 3 oldu döngü bitti b ye geçti
#     for rakam in liste2:
#         print(harf,rakam)             a 1
#                                       a 2
#                                       a 3
#                                       b 1
#                                       b 2
#                                       b 3
#                                       c 1
#                                       c 2
#                                       c 3       


# liste = [1,2,3,4,5,6,7,8,9]
# for i in liste:
#     if i == 3:
#         print("3 ü atladık")
#         continue                  continue kelimesi belirli bir koşuldan sonra devam etmesini sağlıyor
#     print(i)



# for i in liste:
#     if i == 3:
#         print("3 ü atladık")
#         break                          1
#     print(i)                           2
#                                        3 ü atladık
                        
# BREAK:   3 e kadar yazdı 3 de (3 ü atladık) yazdı ve döngüyü kapattı




# x = 'a'

# if(x < 'c'):

#     x += 'b'

# if(x > 'z'):

#     x += 'c'

    

# print(x)




if not True:

   print("1")

elif not (1 + 1 == 3):

   print("2")

else:

   print("3")


