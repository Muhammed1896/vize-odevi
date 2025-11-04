import time
import random

# --- Ayarlar ---
ISTENEN_SICAKLIK = 25.0  # Hedef sıcaklık (°C)
TOLERANS_DEGERI = 1.0    # Bu değerin altındaysa ısıtıcı açılır (25.0 - 1.0 = 24.0°C)
SIMULE_SICAKLIK_ARTISI = 1.5 # Isıtıcı açıkken sıcaklık bu kadar artar
SIMULE_SICAKLIK_DUSUSU = 0.5 # Isıtıcı kapalıyken sıcaklık bu kadar düşer

# --- Durum Değişkenleri ---
isitici_acik = False
mevcut_sicaklik = 20.0  # Başlangıç sıcaklığı
dongu_sayisi = 0

# --- Fonksiyonlar (Gerçek hayatta donanım kontrolünü temsil eder) ---

def isiticiyi_ac():
    """Isıtıcıyı açma komutunu simüle eder."""
    global isitici_acik
    if not isitici_acik:
        isitici_acik = True
        print("    [Durum] Isıtıcı AÇILIYOR.")

def isiticiyi_kapat():
    """Isıtıcıyı kapatma komutunu simüle eder."""
    global isitici_acik
    if isitici_acik:
        isitici_acik = False
        print("    [Durum] Isıtıcı KAPATILIYOR.")

def sicaklik_simulasyonu(current_temp):
    """
    Sıcaklığı, ısıtıcının durumuna göre simüle eder.
    Gerçek bir projede bu fonksiyon yerine sensörden okuma yapılır.
    """
    if isitici_acik:
        # Isıtıcı açık: Sıcaklık artar (biraz rastgelelik eklenir)
        return current_temp + SIMULE_SICAKLIK_ARTISI + random.uniform(0, 0.2)
    else:
        # Isıtıcı kapalı: Sıcaklık düşer (biraz rastgelelik eklenir)
        return current_temp - SIMULE_SICAKLIK_DUSUSU - random.uniform(0, 0.1)

# --- Ana Kontrol Döngüsü ---

print(f"--- Otomatik Isıtıcı Kontrol Sistemi Başlatıldı ---")
print(f"Hedef Sıcaklık: {ISTENEN_SICAKLIK}°C")
print(f"Başlangıç Sıcaklığı: {mevcut_sicaklik:.1f}°C")
print("-------------------------------------------------")

# Örneğin 15 kontrol döngüsü çalıştıralım.
try:
    while dongu_sayisi < 15:
        dongu_sayisi += 1
        print(f"\n--- DÖNGÜ {dongu_sayisi} ---")
        
        # 1. Kontrol: Isıtıcıyı Açma Kararı
        if mevcut_sicaklik < ISTENEN_SICAKLIK - TOLERANS_DEGERI:
            print(f"   🚨 Sıcaklık ({mevcut_sicaklik:.1f}°C) çok düşük. Hedef: {ISTENEN_SICAKLIK}°C")
            isiticiyi_ac()
            
        # 2. Kontrol: Isıtıcıyı Kapatma Kararı (Hedefin üzerindeyse)
        elif mevcut_sicaklik >= ISTENEN_SICAKLIK:
            print(f"   ✅ Sıcaklık ({mevcut_sicaklik:.1f}°C) hedefe ulaştı/geçti.")
            isiticiyi_kapat()
        
        # 3. Kontrol: Mevcut Durumu Koruma Kararı (Tolerans aralığındaysa)
        else:
            print(f"   ➡ Sıcaklık {mevcut_sicaklik:.1f}°C. Hedefe yakın. Mevcut durum korunuyor.")

        # Sıcaklığı simüle et ve güncelle
        mevcut_sicaklik = sicaklik_simulasyonu(mevcut_sicaklik)
        
        print(f"   Yeni Sıcaklık: {mevcut_sicaklik:.1f}°C | Isıtıcı Durumu: {'AÇIK' if isitici_acik else 'KAPALI'}")
        
        time.sleep(1) # Bir sonraki kontrol için 1 saniye bekle

except KeyboardInterrupt:
    # Kullanıcı Ctrl+C ile programı durdurursa bu kısım çalışır.
    print("\nKullanıcı tarafından durdurma sinyali alındı.")
    
finally:
    # --- 🔒 GÜVENLİK KAPATMASI ---
    # Program, döngü normal bitse de (try) veya hata oluşsa da (except)
    # her zaman buradan geçer. Bu, sizin istediğiniz fonksiyondur!
    
    print("\n*")
    print("⚠ GÜVENLİK KAPATMASI: Program sonlanıyor.")
    if isitici_acik:
        isiticiyi_kapat() # Isıtıcı açıksa kapatma komutu gönder
        print("Isıtıcı, güvenlik amaçlı KAPATILDI.")
    else:
        print("Isıtıcı zaten KAPALI durumdaydı.")
    print("*")

print("Program tamamlandı ve tüm sistemler güvenle kapatıldı.")