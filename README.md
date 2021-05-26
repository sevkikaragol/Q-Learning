# Q-Learning

### Daha fazla bilgi için --> [Proje Raporu](https://github.com/sevkikaragol/Q-Learning/blob/main/rapor.pdf)

## Giriş
Bu projede ilk olarak açılan arayüzde kullanıcıdan başlangıç ve bitiş konumlarına atama yapmak için veri alındı. Daha sonra ise alınan bu veriler doğrultusunda rastgele engellerden ve geçişlerden oluşan bir çevre (matris) tanımlandı ve bunun ardından rastgele oluşturulan çevreye göre bir ödül tablosu (reward table) oluşturuldu. Elde ettiğimiz çevre ve ödül tablosu üzerinden Q-Learning algoritması kullanılarak Q-table dolduruldu. Algoritma, geliştiriciler tarafından belirlenen süre boyunca çalıştırıldı ve doldurulan Q-table doğrultusunda optimum yol (rota) bulunarak arayüz üzerinde bu yol gösterildi. Ardından da bölüm başına elde edilen ödül ve atılan adım sayısına bağlı olarak iki adet grafik çizdirildi. En son ise engellerin, geçişlerin ve başlangıç-bitiş noktalarının konumları “engel.txt” içerisine yazdırıldı.

## Proje İsterleri
Burada robotun Q learning algoritması kullanarak engel sütunlarından kaçması ve beyaz alanlardan
geçerek doğru yol alması gerekiyor. Aşağıdaki verilen matrisleri gerçek ortamdaki bir yol olarak düşünün.
Robotumuz mavi kareden başlayıp kırmızı kutulara çarpmadan bitiş kısmına en kısa(maliyetle) yoldan
ulaşırsa başarılı sayılacaktır.
Ajan, herhangi bir beyaz kareden başlayarak sağa, sola, aşağı, yukarı ve çapraz hareket edebilir. Atılan 
adımlar belirleyici olmalı ve engele çarpışmadıkça başarılı olur. Robot en son duvara geldiğinde robot 
sadece aşağı hareket ederek istenilen noktaya “37” gelecektir. Sonuç olarak robot başlangıç noktasından 
istenilen hedefe gelinceye kadar hiçbir engele çarpmadan ve en kısa yolu bularak ödülü alır. Rr: ajan[1,2,8] karelere 
çarparsa işlem bitirir. Aksi takdirde, diğer her kareden herhangi bir işlem yapmak rs ödüllendirilir. <br>

![unknown](https://user-images.githubusercontent.com/65903573/119260508-be4ecf80-bbdb-11eb-8109-701190753b8f.png) <br>

İndirim faktörü γ = 0.9, kırmızıya çarparsa -5 ödül puanı,yeşil bitiş noktasına +5, diğer geçişlere
+3 ödül puanı olarak hesaplanacaktır.

* Verilen 50 * 50’lİk matriste her bir kullanıcı kendine özgü engel oluşturup,matristeki değerleri
random olarak atayacaktır.Bu matris değerlerini engel.txt dosyasına yazdırılacak.Örnek gösterim
(1,1,K).
* Grafiksel ara yüzde belirlenen yollar, engeller ve duvarlar gösterilecektir.
* Kullanıcı tarafından bir grafiksel arayüz tasarlanacak, bu ara yüzde ajan başlangıç noktası, hedef
noktası istenecektir.
* Herhangi bir başlangıç noktasından hedef noktaya ulaşıncaya kadar ajanın yaptığı
kazançların/maliyetin(episode via cost) ve bölüm adım sayısının (episode via step) grafiği
çizdirecek.
* Sonuç olarak ise başlangıç karesinden hedef kareye giden en kısa yol grafiksel ara yüzde
gösterilerek yol planı grafik üzerinde çizdirilecek.

## Yöntem
Bu projede izlenilen yol aşağıda anlatılmıştır:
İlk olarak “Tkinter” modülü kullanılarak başlangıç-bitiş noktalarının konumları kullanıcıdan alınmıştır. <br>
![input](https://user-images.githubusercontent.com/65903573/119260595-31f0dc80-bbdc-11eb-8607-3bf8da6a61c5.png) <br>

Başla butonuna basıldığında girilen konum değerleri doğrultusunda uygulama çalışmaya başlayacaktır.
Daha sonra Q-Learning gerçekleştirilmesi için rastgele bir çevre oluşturulur. <br>

![1](https://user-images.githubusercontent.com/65903573/119260684-8d22cf00-bbdc-11eb-8496-d65d88f73bdc.png) <br>

Oluşturulan çevreye alınan girdi doğrultusunda başlangıç-bitiş noktaları eklenir. <br>

![2](https://user-images.githubusercontent.com/65903573/119260713-ab88ca80-bbdc-11eb-9b8c-97d4e90a62ef.png) <br>

Hemen ardından her şeyiyle tamamlanmış çevre baz alınarak bir ödül tablosu (reward table) oluşturulur. <br>

![3](https://user-images.githubusercontent.com/65903573/119260736-c52a1200-bbdc-11eb-89b9-b2295ddeeaf5.png) <br>

Elde edilen çevre ve ödül tablosu doğrultusunda <br>

![4](https://user-images.githubusercontent.com/65903573/119260751-e559d100-bbdc-11eb-9e64-b02e3da19c46.png) <br>

şeklinde olan Q-Learning formülü kullanılarak algoritma çalışmaya başlar.
Algoritma sonucu bölüm başına elde edilen ödül ve atılan adım sayısı <br>

![5](https://user-images.githubusercontent.com/65903573/119260781-ff93af00-bbdc-11eb-8bbd-2d02b1cbdd94.png) <br>

üstte görüldüğü gibi tasarlanmış olup <br>

![6](https://user-images.githubusercontent.com/65903573/119261011-0242d400-bbde-11eb-8794-937323d4c7bd.png) <br>

şeklinde görülmektedir. <br>
İsterlerden biri olan “engel.txt” içerisine yazdırma işlemi <br>

![7](https://user-images.githubusercontent.com/65903573/119260817-34a00180-bbdd-11eb-9124-ff33dd3dde4f.png) <br>

şeklinde yapılmakta ve <br>

![unknown2](https://user-images.githubusercontent.com/65903573/119260840-58fbde00-bbdd-11eb-82fe-f6541d4f2bde.png) <br>

şeklinde görülmektedir. <br> <br>

![ekran](https://user-images.githubusercontent.com/65903573/119260870-74ff7f80-bbdd-11eb-804f-b30b9b9ab964.png) <br>

En sonunda ise Q-Learning algoritması ile elde edilen optimum yol (rota) Pygame modülü kullanılarak görselleştirilmiş hali üstte gösterildiği gibi kullanıcıya sunulur.

## Kaba Kod
* Kullanıcı metin kutularını doldurdu ve “Başla” butonuna tıkladı.
* Ajanın öğrenme işlemini yapacağı ortam (çevre) oluşturuldu.
* “engel.txt” dosyası oluşturuldu ve dol-duruldu.
* Ajan Q-Learning algoritmasını kullana-rak hareket etmeye başladı ve bu doğrultu-da Q-table içeriğini doldurdu.
* Ajan engele çarptı ve başa döndü (bu adım öğrenme işlemi tamamlanana kadar sürekli tekrarlandı).
* Yapılan hareketler sonucu optimum rota (yol) elde edildi. 
* Plot table ve optimum yolun gösterildiği arayüz kullanıcıya sunuldu. 

