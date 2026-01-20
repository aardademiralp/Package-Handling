1. Metodoloji Karşılaştırması
dpkg -i paket.deb vs apt install ./paket.deb
dpkg -i yaklaşımı

Düşük seviye (low-level) bir araçtır.

Sadece verilen .deb paketini kurar.

Bağımlılık çözümlemesi yapmaz.

Eksik bağımlılıklar varsa kurulum başarısız olur ve sistem “half-configured” durumda kalabilir.

Bağımlılıkların manuel olarak kurulması gerekir:

sudo apt -f install

apt install ./paket.deb yaklaşımı

apt, dpkg’yi arka planda kullanan yüksek seviye (high-level) bir paket yöneticisidir.

Yerel .deb paketini kurarken:

Gerekli bağımlılıkları depo (repository) üzerinden otomatik indirir

Bağımlılık çakışmalarını analiz eder

Kurulum sırasını doğru şekilde planlar

Transaction (işlem) mantığına daha yakındır.

Teknik Karşılaştırma Tablosu
Özellik	dpkg -i	apt install ./
Bağımlılık Çözümü	❌ Yok	✅ Var
Repository Kullanımı	❌	✅
Hata Kurtarma	Zayıf	Güçlü
Kullanıcı Dostu	Düşük	Yüksek
Otomasyon Uygunluğu	Orta	Yüksek

📌 Sonuç: Otomatik güncelleme ve güvenilir kurulum hedefleyen bir araç için apt install ./paket.deb endüstri standardına daha uygundur.

2. Süreç Yönetimi (Subprocess Management)
os.system neden yetersizdir?

Komut çıktısını ayrıntılı şekilde yakalayamaz

stdout ve stderr ayrımı yoktur

Hata kodları sınırlı şekilde kontrol edilir

Komut enjeksiyonuna açıktır

os.system("apt install paket.deb")

subprocess.run neden tercih edilmelidir?
import subprocess

result = subprocess.run(
    ["apt", "install", "./paket.deb"],
    capture_output=True,
    text=True
)

Avantajları:

stdout: Standart çıktı

stderr: Hata mesajları

returncode: Komutun başarı/başarısızlık durumu

Shell kullanılmadan çalıştırılabilir (güvenli)

Hata Ayıklama Açısından Önemi
if result.returncode != 0:
    print("Hata:", result.stderr)


📌 Bilimsel gerekçe: Süreçlerin deterministik kontrolü, hata analizinin tekrarlanabilirliği ve güvenli komut çalıştırma.

3. Endüstri Standardı Loglama
Neden Timestamp’li Log Tutulmalı?

Sistem hatalarının zamanla korelasyonu

Geriye dönük hata analizi (post-mortem)

Denetlenebilirlik (auditability)

Adli bilişim (forensics)

islem_gecmisi.log Dosyasında Bulunması Gereken Alanlar
Alan	Açıklama
Timestamp	ISO 8601 formatı
İşlem Türü	install / update / remove
Paket Adı	Örn: nginx
Versiyon	1.18.0
Kullanıcı	UID / username
Komut	Çalıştırılan komut
Çıkış Kodu	returncode
Durum	SUCCESS / FAIL
Hata Mesajı	stderr içeriği
Python Loglama Örneği
import logging

logging.basicConfig(
    filename="islem_gecmisi.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logging.info("nginx paketi başarıyla kuruldu")

4. Güvenlik Analizi
sudo ile Çalışmanın Riskleri

Hatalı bir komut tüm sistemi etkileyebilir

Log silme, dosya bozma riski

Yetki yükseltme (privilege escalation)

📌 Öneri:

Aracı root olarak değil, yalnızca gerekli komutlar için sudo ile çalıştırmak

/etc/sudoers içinde sınırlı yetki tanımlamak

Command Injection Tehlikesi

❌ Tehlikeli kullanım:

os.system(f"apt install {paket_adi}")


Eğer paket_adi = "vim; rm -rf /" ise → FELAKET

Güvenli Yaklaşım
subprocess.run(
    ["apt", "install", paket_adi],
    check=True
)


Ek Önlemler:

Girdi doğrulama (regex)

Whitelist (izinli paket listesi)

shell=False kullanımı


İnfografik Metin Yapısı (Özet)

Başlık:

Python Tabanlı Linux Paket Yönetim Aracı – Teknik Analiz

Bölümler:

Problem: Manuel paket kurulumlarında bağımlılık hataları

Çözüm: apt tabanlı otomatik bağımlılık çözümü

Teknoloji: Python + subprocess + logging

Güvenlik: Command Injection önleme

Sonuç: Güvenilir, otomatik, izlenebilir sistem aracı


<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Paket Yönetim Aracı – Teknik Rapor</title>
    <style>
        body { font-family: Arial; margin: 40px; }
        h1, h2 { color: #2c3e50; }
        code { background: #f4f4f4; padding: 4px; }
    </style>
</head>
<body>

<h1>Python Tabanlı Linux Paket Yönetim Aracı</h1>

<h2>1. Metodoloji</h2>
<p>Bu projede <code>apt install ./paket.deb</code> yöntemi tercih edilmiştir çünkü bağımlılık çözümleme yeteneği vardır.</p>

<h2>2. Süreç Yönetimi</h2>
<p><code>subprocess.run</code> kullanılarak stdout, stderr ve hata kodları kontrol edilmiştir.</p>

<h2>3. Loglama</h2>
<p>İşlemler zaman damgalı olarak <code>islem_gecmisi.log</code> dosyasına kaydedilmiştir.</p>

<h2>4. Güvenlik</h2>
<p>Command Injection risklerine karşı shell kullanılmamıştır.</p>

<h2>5. Sonuç</h2>
<p>Geliştirilen araç, güvenli ve otomatik paket yönetimi sağlamaktadır.</p>

</body>
</html>

