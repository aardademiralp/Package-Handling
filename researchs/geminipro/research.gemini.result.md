1. Metodoloji Karşılaştırması: dpkg -i vs. apt install ./paket.deb
Bu ayrım, projenin "Bağımlılık Yönetimi" (Dependency Resolution) yeteneğini belirleyen temel mimari karardır.

dpkg (Debian Package): Düşük seviyeli (low-level) bir araçtır. Sadece kendisine verilen .deb dosyasını sisteme kopyalar ve yapılandırır.

Teknik Kısıt: Eğer kurmaya çalıştığın paketin sistemde olmayan bir bağımlılığı varsa (örneğin libssl kütüphanesi eksikse), dpkg işlemi hata koduyla durdurur. Eksik parçayı internetten bulup indirme yeteneği yoktur.

apt (Advanced Package Tool): Yüksek seviyeli (high-level) bir paket yöneticisidir. dpkg'yi bir backend (arka uç) olarak kullanır.

Teknik Avantaj: apt install ./dosya.deb komutunu kullandığında, APT önce paketin meta verisini (metadata/control file) okur. Gerekli bağımlılıkları listeler, kendi veritabanındaki (repositories) paketlerle karşılaştırır, eksikleri internetten indirir ve en son adımda senin yerel paketini kurar.

Bilimsel Temel: Bu, "Dependency Hell" (Bağımlılık Cehennemi) olarak bilinen sorunu çözer ve sistem bütünlüğünü (system integrity) korur.

2. Süreç Yönetimi: os.system vs. subprocess.run
Python'da sistem komutlarını yönetirken os.system artık "deprecated" (önerilmeyen/eski) kabul edilir. Modern ve güvenli yaklaşım subprocess modülüdür.

Neden subprocess.run?

Akış Kontrolü: os.system sadece komutun çıkış kodunu (exit status) döndürür; komutun çıktısını (output) değişkene atayamazsınız. subprocess.run ile hem stdout (standart çıktı) hem de stderr (hata çıktısı) yakalanabilir (capture_output=True).

Esneklik: subprocess, bir komutu "shell" (kabuk) üzerinden değil, doğrudan işletim sistemi çekirdeğine (kernel) process olarak gönderebilir (shell=False). Bu performans ve güvenlik sağlar.

Hata Ayıklama (Debugging) Önemi:

Return Codes: Linux'ta 0 başarı, 0 dışındaki her sayı (1-255) bir hatayı temsil eder. Kodunuzda if result.returncode != 0: kontrolü yaparak, paketin neden kurulmadığını (örneğin disk dolu hatası) anlayabilir ve kullanıcıya doğru geri bildirim verebilirsiniz.

3. Endüstri Standardı Loglama
Kritik sistem araçlarında loglama, "Nice to have" değil, zorunluluktur. Bir güncelleme sistemi çökertirse, "Forensic Analysis" (Adli Analiz) için loglara bakılır.

Zaman Damgası (Timestamp): ISO 8601 formatı (Örn: 2025-11-21 14:30:05) kullanılmalıdır. Sorunun ne zaman başladığını ve ne kadar sürdüğünü gösterir.

Log Dosyası Veri Alanları:

Level: (INFO, WARNING, ERROR, CRITICAL) - Olayın ciddiyeti.

Timestamp: Olayın gerçekleşme zamanı.

Module/Function: Hatayı üreten fonksiyon adı (Örn: InstallManager.install_package).

Action: Çalıştırılan komut (Örn: apt install ./vlc.deb).

Result/Message: Çıktı veya hata mesajı.

4. Güvenlik: Sudo ve Command Injection
Aracın paket kurabilmek için root yetkisine (sudo) ihtiyacı vardır. Ancak bu yetki, büyük sorumluluk getirir.

Command Injection Riski: Kullanıcıdan alınan bir girdi (örneğin paket adı), doğrudan bir shell komutuna eklenirse saldırı olabilir.

Senaryo: Kullanıcı paket adı olarak vlc; rm -rf / girerse ve siz bunu os.system("apt install " + paket_adi) şeklinde çalıştırırsanız, sistem önce VLC'yi kurmaya çalışır, ardından tüm dosya sistemini siler.

Önlemler:

Sanitization (Temizleme): Girdinin sadece izin verilen karakterlerden (a-z, 0-9, ., -) oluştuğunu Regex ile kontrol etmek.

shell=False Kullanımı: subprocess.run(["apt", "install", paket_adi], shell=False) şeklinde komutu liste olarak verirseniz, Python girdiyi bir komut zinciri olarak değil, tek bir argüman (dosya adı) olarak işler. Bu, en etkili defans yöntemidir.

İnfografik Metin Yapısı
Ödev sunumun için kullanabileceğin görsel hiyerarşi taslağı:

BAŞLIK: Yeni Nesil Paket Yöneticisi Mimarisi

GİRİŞ KATMANI (User Interface)

Simge: Terminal Ekranı

Metin: Kullanıcı .deb dosyasını seçer.

Güvenlik: Girdi Regex ile taranır (Input Sanitization).

İŞLEM KATMANI (Python Controller)

Simge: Dişli Çarklar (Process)

Metod: subprocess.run (Shell=False)

Karar Mekanizması:

✅ apt kullanılır (Bağımlılıkları Çözer)

❌ dpkg kullanılmaz (Bağımlılık Hatası Riski)

SİSTEM KATMANI (Kernel & Logs)

Simge: Kilit (Root) ve Dosya (Log)

Eylem: sudo yetkisi ile kurulum yapılır.

Kayıt: islem_gecmisi.log -> [TIMESTAMP] [INFO] Kurulum Başarılı.
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Paket Yönetim Aracı - Teknik Rapor</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; background-color: #f4f4f4; }
        .container { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        h1 { color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }
        h2 { color: #e67e22; margin-top: 25px; }
        code { background: #eee; padding: 2px 5px; border-radius: 4px; font-family: monospace; color: #c0392b; }
        .box { background-color: #e8f6f3; border-left: 5px solid #1abc9c; padding: 15px; margin: 20px 0; }
        ul { list-style-type: square; }
        .footer { margin-top: 40px; font-size: 0.8em; text-align: center; color: #777; }
    </style>
</head>
<body>

<div class="container">
    <h1>Linux Paket Yönetim Aracı: Teknik Analiz</h1>
    <p>Bu rapor, Python tabanlı paket yönetim sisteminin arkasındaki metodolojik ve güvenlik kararlarını özetler.</p>

    <h2>1. Metodoloji: APT vs DPKG</h2>
    <p>Projede yerel paket kurulumları için <code>dpkg -i</code> yerine <code>apt install ./dosya.deb</code> tercih edilmiştir.</p>
    <ul>
        <li><strong>Neden?</strong> <code>apt</code>, eksik kütüphaneleri otomatik tespit eder ve repolardan indirir (Dependency Resolution).</li>
        <li><strong>Sonuç:</strong> Kullanıcı deneyimi iyileştirilir ve kurulum hataları minimize edilir.</li>
    </ul>

    <h2>2. Süreç Yönetimi: Subprocess</h2>
    <p>Sistem çağrıları için <code>os.system</code> yerine <code>subprocess.run</code> kullanılmıştır.</p>
    <div class="box">
        <strong>Teknik Avantaj:</strong> Standart çıktı (stdout) ve hata çıktıları (stderr) ayrı ayrı yakalanarak log dosyasına işlenebilir. Ayrıca "Exit Code" kontrolü ile işlem başarısı doğrulanır.
    </div>

    <h2>3. Güvenlik Önlemleri</h2>
    <p>Uygulama <code>sudo</code> yetkileriyle çalıştığı için "Command Injection" saldırılarına karşı şu önlemler alınmıştır:</p>
    <ul>
        <li><strong>Input Sanitization:</strong> Kullanıcı girdileri özel karakterlerden arındırılır.</li>
        <li><strong>Shell=False:</strong> Python subprocess modülü, komutları liste formatında alarak kabuk (shell) yorumlamasını devre dışı bırakır.</li>
    </ul>

    <div class="footer">
        © 2025 - Paket Yönetim Aracı Proje Raporu
    </div>
</div>

</body>
</html>
