# Yapay Zekaya Sorulan Sorgu (Prompt)
Ben Python ile Linux tabanlı bir Paket Yönetim Aracı (Package-Handling Tool) geliştiriyorum. Bu aracın amacı; sistem güncellemelerini otomatize etmek ve .deb paketlerini bağımlılık (dependency) sorunlarını çözerek kurmaktır. Ödevim gereği bu projeyi bilimsel ve teknik açıdan temellendirmem gerekiyor. Lütfen aşağıdaki başlıkları detaylandır:



Metodoloji Karşılaştırması: Linux'ta yerel bir paketi kurarken dpkg -i yerine apt install ./paket.deb kullanmanın teknik avantajlarını ve bağımlılık yönetimi (dependency resolution) farklarını açıkla.

Süreç Yönetimi (Subprocess): Python'da sistem komutlarını çalıştırırken os.system yerine neden subprocess.run tercih edilmelidir? stdout, stderr ve return codes kavramlarının hata ayıklamadaki önemini belirt.

Endüstri Standardı Loglama: Kritik bir sistem aracında zaman damgalı (timestamp) log tutmanın önemini ve bir log dosyasında (islem_gecmisi.log) bulunması gereken temel veri alanlarını analiz et.

Güvenlik: Projenin sudo yetkisiyle çalışmasının risklerini ve kullanıcı girdilerinden kaynaklanabilecek "Command Injection" saldırılarına karşı alınabilecek önlemleri açıkla.

Kaynaklar: Bu bilgileri doğrulayan resmi Linux (Debian/Ubuntu) dokümanları ve Python kütüphane referanslarını liste şeklinde sun.

Ek Talepler (Ödev Özel):



Bu araştırma sonuçlarını özetleyen bir infografik metin yapısı oluştur.

Bu araştırmanın bulgularını sunan çok basit bir HTML rapor sayfası kodu hazırla.
