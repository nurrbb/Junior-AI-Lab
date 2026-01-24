import cv2 #kütüphanemizi çağırıyorz
#open sourse computer vision

#1. adım resmi okumak
#manzara dosyasını sayı matrisine dönüştürüyoruz 
resim = cv2.imread("manzara.jpg")

#ekranda göster
# cv2.imshow("Benim ilk resmim", resim)

# #bir tuşa basana dek pencereyi açık tutar
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# (b, g, r) = resim[100,100]
# print(f"Mavi: {b}, Yesil: {g}, Kirmizi: {r}")

# resim[100:150, 100:150] = [0,0,0]

# cv2.imshow("Piksel Mudahalesi", resim)
# cv2.waitKey(0)

# gri_resim = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)

# cv2.imshow("Renkli", resim)
# cv2.imshow("Gri",gri_resim)
# cv2.waitKey(0)
# cv2.destroyAllWindows

# cv2.rectangle(resim,(50,50),(200,300),(0,162,0),-1)
# cv2.circle(resim,(20,20),5,(255,0,0),-1)

# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(resim,'Bu bir manzara mıdır', (100,400), font,1,(255,255,255),2)
# cv2.imshow("Mudehale edilmis resim", resim)
# cv2.waitKey(0)

# negatif_resim = 255 - resim
# cv2.imshow("Zit dunya", negatif_resim)
# cv2.waitKey(0)

# yatay = cv2.flip(resim,0)
# cv2.imshow("Ayna", yatay)
# cv2.waitKey(0)

# b,g,r = resim[100,100]
# print(f"100x100 noktasındaki renkler -> M:{b}, Y:{g}, K: {r}")

bulanik = cv2.GaussianBlur(resim,(15,15),0)
cv2.imshow("Sansurlu goruntu", bulanik)
cv2.waitKey(0)