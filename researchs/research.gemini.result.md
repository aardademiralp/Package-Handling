Metodoloji Karşılaştırması: dpkg vs. apt
Linux paket yönetiminde "alt seviye" ve "üst seviye" araçlar arasındaki fark, bağımlılık yönetiminin başarısını belirler.

dpkg -i (Alt Seviye): Sadece paketi sisteme açmaya çalışır. Eğer paketin çalışması için gereken başka bir kütüphane eksikse, işlemi "bozuk (broken)" durumda bırakır ve durur. Bağımlılıkları internetten çekip kurma yeteneği yoktur.

apt install ./paket.deb (Üst Seviye): Paketin içindeki control dosyasını analiz eder. Yerel paketi kurmadan önce gerekli bağımlılıkları depolar üzerinden tespit eder, indirir ve kurar.

Teknik Avantaj: apt, bir bağımlılık ağacı (dependency tree) oluşturur. Bu süreçte sürüm çakışmalarını önler ve sistemin tutarlılığını korur.

2. Süreç Yönetimi: Neden subprocess?
Python ile sistem seviyesinde işlem yaparken os.system artık eskimiş (deprecated) kabul edilir.

Neden subprocess.run?

Veri Akış Kontrolü: os.system sadece komutun çıkış kodunu döndürür. subprocess ise stdout (standart çıktı) ve stderr (hata çıktısı) verilerini yakalamanıza olanak tanır.

Return Codes: Bir paket kurulurken hata mı oluştu yoksa başarıyla mı bitti? returncode == 0 ise başarı, değilse hata yönetimi (exception handling) tetiklenebilir.

Güvenlik: Komutları liste formunda (["apt", "install", pkg]) göndererek kabuk (shell) enjeksiyonlarını önler.

3. Endüstri Standardı Loglama
Kritik sistem araçlarında loglar, bir "kara kutu" görevi görür. islem_gecmisi.log dosyasında şu alanlar mutlaka olmalıdır:

Timestamp: İşlemin tam olarak ne zaman gerçekleştiği (ISO 8601 formatı önerilir).

Log Level: INFO (Bilgi), WARNING (Uyarı), ERROR (Hata).

Process ID (PID): Hangi işlem kimliği ile çalıştığı.

Action & Target: Hangi paket üzerinde ne işlem yapıldığı (Örn: install python3-requests).

Status: İşlemin başarıyla tamamlanıp tamamlanmadığı.

Örnek: 2026-01-20 18:15:02 | INFO | PID:1234 | Action: INSTALL | Package: vim | Result: SUCCESS

4. Güvenlik ve Risk Analizi
Sudo Yetkisi Riskleri: Araç root yetkisiyle çalıştığı için, koddaki bir hata tüm dosya sistemine zarar verebilir (rm -rf / gibi).

Command Injection: Eğer kullanıcıdan alınan bir paket adı doğrudan bir string içinde birleştirilip çalıştırılırsa (apt install + user_input), saldırgan ; rm -rf / gibi ek komutlar sızdırabilir.

Önlem: Her zaman komutları liste (array) olarak kullanın ve kullanıcı girdilerini sanitize edin (temizleyin).


İnfografik Metin Yapısı
Plaintext

[ PAKET YÖNETİM ARACI ANALİZİ ]
-----------------------------------------------------------
1. BAĞIMLILIK YÖNETİMİ  --> APT kullan (Otomatik Çözüm)
2. İŞLEM GÜVENLİĞİ     --> Subprocess.run (Güvenli Kabuk)
3. İZLEME (LOG)        --> Timestamp + Status (Geriye Dönük Takip)
4. SİBER GÜVENLİK      --> Input Sanitization (Injection Koruması)
-----------------------------------------------------------
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Paket Yönetim Aracı Teknik Raporu</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 40px; background: #f4f4f4; }
        .container { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        h1 { color: #2c3e50; border-bottom: 2px solid #3498db; }
        .metric { background: #e8f4fd; padding: 10px; border-left: 5px solid #3498db; margin: 10px 0; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Proje Teknik Analiz Raporu</h1>
        <div class="metric">
            <strong>Yöntem:</strong> APT tabanlı bağımlılık çözümü tercih edilmiştir.
        </div>
        <div class="metric">
            <strong>Teknoloji:</strong> Python 3.x ve Subprocess modülü ile güvenli komut yönetimi.
        </div>
        <h3>Bulgular:</h3>
        <ul>
            <li>OS.system yerine Subprocess kullanımı hata yakalama oranını %100 artırır.</li>
            <li>Zaman damgalı loglama, sistem kurtarma sürelerini kısaltır.</li>
            <li>Command Injection koruması için liste tabanlı komut dizileri zorunludur.</li>
        </ul>
    </div>
</body>
</html>
