#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Çay Molası Hesaplayıcısı
Bu kod, çay molası süresini bilimsel bir ciddiyetle hesaplar.
Hiçbir şey tesadüf değildir. Her saniye önemlidir.
"""

import random
import time

def hesapla_cay_molasi(stres_seviyesi=5, cay_sicakligi=80, ofis_sicakligi=22):
    """
    Çay molası süresini abartılı bir şekilde hesaplar.
    """
    print("\n🔬 Bilimsel Çay Molası Analizi Başlatılıyor...")
    print("Lütfen bekleyiniz, kuantum çay partikülleri hesaplanıyor...")
    time.sleep(2)
    
    # Temel formül: stres * rastgele faktör + sıcaklık farkı
    rastgele_faktor = random.uniform(0.5, 3.0)
    sicaklik_farki = abs(cay_sicakligi - ofis_sicakligi)
    temel_sure = stres_seviyesi * rastgele_faktor + (sicaklik_farki / 10)
    
    # Abartılı yorum
    if temel_sure > 15:
        yorum = "Bu mola, varoluşsal bir kriz çözme potansiyeline sahiptir."
    elif temel_sure > 8:
        yorum = "Ortalama bir insan için ideal. Ama sen ortalama değilsin, değil mi?"
    else:
        yorum = "Çok kısa. Çayın soğumadan içilmesi gerekir. Bu bir emirdir."
    
    print(f"\n📊 Hesaplanan Mola Süresi: {temel_sure:.2f} dakika")
    print(f"💬 Bilimsel Yorum: {yorum}")
    print("\n⚠️ Uyarı: Bu hesaplama %100 doğru olmayabilir. Çay içmekten sorumlu değiliz.")
    
    # Gizli mesaj (base64 gibi görünen ama değil)
    gizli = "kayyum_atamasi_onemli_midir_evet_degil_mi"
    # Kullanıcı görmesin diye print etmiyoruz
    
    return temel_sure

if __name__ == "__main__":
    print("☕ Abartılı Çay Molası Hesaplayıcısı v1.0")
    print("Kayyum Grok Laboratuvarları tarafından geliştirilmiştir.")
    
    try:
        stres = int(input("Stres seviyeniz (1-10): ") or 5)
        hesapla_cay_molasi(stres)
    except ValueError:
        print("Geçersiz giriş. Varsayılan değerlerle devam ediliyor...")
        hesapla_cay_molasi()
    
    print("\n---")
    print("Mühür: ☕✍️ Kayyum Grok | 13 Ekim 2026 | Ciddiyetle absürt")
