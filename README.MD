# Linux Paket ve Sistem Yönetim Aracı

Bu proje, Linux tabanlı işletim sistemlerinde (Ubuntu/Debian) sistem yöneticilerinin en sık karşılaştığı paket kurulumu ve güncelleme sorunlarını otomatize etmek amacıyla geliştirilmiştir.

Manuel olarak yapılan 'dpkg' kurulumlarında yaşanan bağımlılık (dependency) hatalarını otomatik olarak çözer ve tüm süreci kayıt altına alır.

## Proje Klasör Yapısı
Proje, düzenli bir geliştirme ortamı sağlamak için aşağıdaki hiyerarşiye göre tasarlanmıştır:

PackageProject/
├── src/
│   └── main.py          # Projenin kaynak kodları (Python)
├── specs/
│   └── proje_tanimi.md  # Teknik gereksinimler ve analiz
├── researchs/
│   └── arastirma.md     # Yöntem araştırmaları ve notlar
├── docs/                # Ek dokümantasyon dosyaları
└── README.md            # Proje hakkında genel bilgi

## Gereksinimler
Bu aracı çalıştırmak için sisteminizde aşağıdakilerin bulunması gerekir:
- İşletim Sistemi: Ubuntu, Debian, Kali Linux veya Mint.
- Python Sürümü: Python 3.6 veya üzeri.
- Yetki: Sistem dosyalarına müdahale edildiği için 'sudo' (root) yetkisi şarttır.

## Kurulum ve Kullanım
Proje herhangi bir harici kütüphane kurulumu gerektirmez (Standart Python kütüphaneleri kullanılmıştır).

1. Proje dizinine terminalden giriş yapın.
2. Aşağıdaki komutla scripti başlatın:
   sudo python3 src/main.py
3. Açılan menüden yapmak istediğiniz işlemi seçin.

## Özellikler
* Akıllı Güncelleme: 'apt update' ve 'apt upgrade' komutlarını sırasıyla çalıştırarak sistemi güvenli bir şekilde günceller.
* Hata Ayıklamalı Kurulum: .deb dosyalarını kurarken 'apt install ./dosya.deb' yapısını kullanır. Eğer hata oluşursa otomatik olarak 'fix-broken install' moduna geçer.
* Loglama Sistemi: Yapılan her işlem, tarih ve saat etiketiyle 'islem_gecmisi.log' dosyasına kaydedilir. Bu sayede geriye dönük hata takibi yapılabilir.

## Gelecek Planları (Geliştirilecekler)
Projenin ilerleyen versiyonlarında eklenmesi planlanan özellikler:
- [ ] Birden fazla .deb dosyasını aynı anda toplu kurma özelliği.
- [ ] İşlem bittiğinde kullanıcıya e-posta veya bildirim gönderme.
- [ ] Basit bir grafik arayüz (GUI) tasarımı.

## Geliştirici Notu
Bu proje, Linux Sistem Yönetimi dersi kapsamında açık kaynak felsefesine uygun olarak hazırlanmıştır.
