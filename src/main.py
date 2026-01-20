import subprocess
import datetime
import os

# Log dosyasının yolu
LOG_FILE = "islem_gecmisi.log"

def log_tut(mesaj):
    """Yapılan işlemleri tarihçesiyle dosyaya kaydeder."""
    zaman = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_satiri = f"[{zaman}] {mesaj}"
    
    print(log_satiri) # Ekrana yaz
    with open(LOG_FILE, "a") as f:
        f.write(log_satiri + "\n") # Dosyaya yaz

def komut_calistir(komut, aciklama):
    """Terminal komutlarını çalıştırır ve sonucu loglar."""
    log_tut(f"BAŞLATILIYOR: {aciklama}")
    
    try:
        # Komutu çalıştır
        sonuc = subprocess.run(komut, shell=True, check=True, text=True, capture_output=True)
        log_tut(f"BAŞARILI: {aciklama}")
        return True
    except subprocess.CalledProcessError as e:
        log_tut(f"HATA: {aciklama} işlemi başarısız oldu.")
        log_tut(f"Hata Detayı: {e.stderr}")
        return False

def sistem_guncelle():
    log_tut("Sistem güncelleme süreci başlatılıyor...")
    komut_calistir("sudo apt-get update", "Paket listelerini güncelleme")
    komut_calistir("sudo apt-get upgrade -y", "Mevcut paketleri yükseltme")

def deb_kur(dosya_yolu):
    if not os.path.exists(dosya_yolu):
        log_tut(f"HATA: Dosya bulunamadı -> {dosya_yolu}")
        return

    log_tut(f"{dosya_yolu} kurulumu için hazırlık yapılıyor.")
    
    # En güvenli yöntem: apt install ./dosya.deb (Bağımlılıkları çözer)
    full_path = os.path.abspath(dosya_yolu)
    basari = komut_calistir(f"sudo apt install -y {full_path}", f"{dosya_yolu} kurulumu")
    
    if not basari:
        log_tut("Alternatif yöntem deneniyor: dpkg + fix-broken")
        komut_calistir(f"sudo dpkg -i {full_path}", "dpkg ile zorla kurulum")
        komut_calistir("sudo apt --fix-broken install -y", "Eksik bağımlılıkları tamamlama")

def menu():
    print("\n--- Linux Paket Yönetim Aracı ---")
    print("1. Sistemi Güncelle (Update & Upgrade)")
    print("2. .deb Dosyası Kur")
    print("3. Çıkış")
    
    secim = input("Seçiminiz (1/2/3): ")
    
    if secim == '1':
        sistem_guncelle()
    elif secim == '2':
        yol = input("Kurulacak .deb dosyasının yolu: ")
        deb_kur(yol)
    elif secim == '3':
        print("Çıkış yapılıyor...")
        exit()
    else:
        print("Geçersiz seçim.")
        menu()

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("UYARI: Bu scripti 'sudo' ile çalıştırmanız önerilir.")
    menu()
