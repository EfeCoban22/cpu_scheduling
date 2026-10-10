# Adım 1: Elimizdeki verileri tabloya uygun şekilde listeliyoruz
islemler = [
    {"id": "P1", "gelis": 4, "burst": 5},
    {"id": "P2", "gelis": 6, "burst": 4},
    {"id": "P3", "gelis": 0, "burst": 3},
    {"id": "P4", "gelis": 6, "burst": 2},
    {"id": "P5", "gelis": 5, "burst": 4},
]

# Adım 2: İşlemleri önce geliş zamanına, eşitlik varsa işlem ID'sine göre sıralıyoruz
islemler.sort(key=lambda x: (x["gelis"], x["id"]))

# Adım 3: Zamanı ve toplamları tutacağımız değişkenleri başlatıyoruz
su_anki_zaman = 0
toplam_bekleme = 0
toplam_turnaround = 0

print("İşlem Sırası ve Detaylar:")
print("-" * 50)

# Adım 4: Her bir işlemi sırayla CPU'ya sokuyoruz
for islem in islemler:
    # Eğer CPU boşta kaldıysa (örneğin 3 ile 4. ms arası), zamanı işlemin gelişine ilerlet
    if su_anki_zaman < islem["gelis"]:
        su_anki_zaman = islem["gelis"]
    
    # İşlemin başlangıç ve bitiş zamanlarını hesaplıyoruz
    baslama_zamani = su_anki_zaman
    bitis_zamani = baslama_zamani + islem["burst"]
    
    # Senin formüllerin: TT ve WT hesaplamaları
    turnaround_time = bitis_zamani - islem["gelis"]
    waiting_time = turnaround_time - islem["burst"]
    
    # Toplamlara ekliyoruz (Ortalama hesaplamak için)
    toplam_bekleme += waiting_time
    toplam_turnaround += turnaround_time
    
    # Detayları ekrana yazdırıyoruz
    print(f"{islem['id']} -> Başlama: {baslama_zamani}, Bitiş: {bitis_zamani}, WT: {waiting_time}, TT: {turnaround_time}")
    
    # Bir sonraki işlem için zamanı güncelliyoruz
    su_anki_zaman = bitis_zamani

# Ortalama değerleri bulup yazdırıyoruz
islem_sayisi = len(islemler)
ortalama_wt = toplam_bekleme / islem_sayisi
ortalama_tt = toplam_turnaround / islem_sayisi

print("-" * 50)
print(f"Ortalama Bekleme Süresi (AWT): {ortalama_wt} ms")
print(f"Ortalama Geri Dönüş Süresi (ATT): {ortalama_tt} ms")