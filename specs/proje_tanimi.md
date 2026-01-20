# Proje: Linux Package Automation Tool

## 1. Projenin Amacı
Bu proje, sistem yöneticilerinin günlük tekrar eden görevleri olan paket kurulumu ve sistem güncellemelerini otomatize etmek için geliştirilmiştir. Python kullanılarak, manuel hataların önüne geçilmesi ve yapılan işlemlerin kayıt altına alınması hedeflenmiştir.

## 2. Teknik Gereksinimler
* **Dil:** Python 3
* **İşletim Sistemi:** Debian/Ubuntu tabanlı Linux dağıtımları.
* **Yetki:** Root (sudo) yetkisi gerektirir.

## 3. Temel Fonksiyonlar
1. **Sistem Güncelleme:** `apt update` ve `upgrade` işlemlerini tek adımda yapar.
2. **Akıllı .deb Kurulumu:** İndirilen paketleri kurarken `dependency` (bağımlılık) hatası verirse otomatik olarak `fix-broken install` komutunu çalıştırarak sorunu çözer.
3. **Loglama:** Her işlemin sonucunu tarih ve saat etiketiyle `islem_gecmisi.log` dosyasına kaydeder.
