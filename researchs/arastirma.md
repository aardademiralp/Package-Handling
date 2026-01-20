# Araştırma Raporu: Paket Yönetim Yöntemleri

Bu projeyi geliştirirken iki farklı yöntem incelenmiştir:

## Yöntem 1: dpkg -i (Eski Yöntem)
`dpkg`, Debian'ın temel paket yöneticisidir. Ancak en büyük eksikliği, paketlerin ihtiyaç duyduğu diğer kütüphaneleri (dependencies) internetten otomatik indirememesidir. Bu yüzden sık sık kurulum hatalarına sebep olur.

## Yöntem 2: apt install ./dosya.deb (Seçilen Yöntem)
Yeni `apt` sürümleri, yerel `.deb` dosyalarını kurarken aynı zamanda eksik bağımlılıkları da depodan çekebilmektedir.

## Sonuç
Projemizde kararlılık ve kullanım kolaylığı için **Yöntem 2** tercih edilmiştir. Ancak yedek plan olarak script, ilk yöntemin başarısız olması durumunda `dpkg` ve `fix-broken` komutlarını devreye sokacak şekilde kodlanmıştır.
