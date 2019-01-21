# website-blocker
Python ile yazılan website engelleyici script'i ile belirlenen internet sitelerine,istenilen saatler arasında girilmesi engellenebilir.


Python script'ini normal şartlarda her seferinde bizim çalıştırmamız gerekiyordu.Böyle bir uğraş içerisine girmemek için powershell kullanarak  bir görev zamanlayıcısı script'i oluşturdum.Bu powershell script'i, her bilgisayar oturumu açıldığında python script'inin arka planda çalışmasını sağlar.

Powershell ile oluşturduğum zamanlanmış görev script'ini kullanmadan Windows'un zamanlanmış görevler ayarlarından da,powershell script'inin yaptığı işlemi yaparak zamanlanmış görev oluşturabilirsiniz.


### Engellenecek web siteleri  ve saatleri belirleme
***websiteBlocker.pyw*** dosyasının içerisinden,  
**website_liste** listesinin içerisine engellenmesi istenilen internet siteleri yazılır.  
Belirlenen web sitelerinin engellenmesi için başlangıç ve bitiş saatleri **baslangicSaati** ve **bitisSaati** değişkenlerine yazılır.




### Örnek Kullanımı
Örnek olarak  Google'yi  sabah 08:00 ile akşam 18:00 arasında engelleyeceğim.<br /><br />   



     
Powershell ile oluşturduğum zamanlanmisGorev.ps1 dosyasını çalıştırarak zamanlanmış görev oluşturuyorum.Zamanlanmış görev oluşturduktan sonra her oturum açıldığında python script'i arka planda çalışacak.

![zamanlanmisgorev](https://user-images.githubusercontent.com/25087769/51472328-2ed64f00-1d8a-11e9-85c5-778b28372331.PNG)



Bir sonraki oturum açılışında webBlocker devreye girdi.
Saat 02:06:09 PM(14:06:09) olduğu için https://www.google.com, google.com ve www.google.com adresleri hosts dosyasının içerisine eklendi.

 #### Host dosyası

![hosts_dosyasi](https://user-images.githubusercontent.com/25087769/51473466-80cca400-1d8d-11e9-8f0d-0372355502e0.PNG)


 #### Google
![engellenen site2](https://user-images.githubusercontent.com/25087769/51472877-ce481180-1d8b-11e9-9300-a644c2dbac0e.png)


Saat 09:06:26 PM(21:06:26) olduğunda ise https://www.google.com, google.com ve www.google.com adresleri hosts dosyasının içerisinden siliniyor.

 #### Host dosyası
![hosts_dosyasi2](https://user-images.githubusercontent.com/25087769/51473195-bc1aa300-1d8c-11e9-89ba-4b6d1311e517.PNG)

 #### Google
![engellenmemis site](https://user-images.githubusercontent.com/25087769/51473202-c2a91a80-1d8c-11e9-8749-8368c06abacf.PNG)







