# HashSet: Her eleman benzersizdir, sıralama garantisi yoktur

hashset = set()

# Eleman ekleme
hashset.add("elma")
hashset.add("armut")
hashset.add("muz")
hashset.add("elma")  # Aynı eleman tekrar eklenmez

# Eleman silme
hashset.discard("armut")

# Kontrol
print("elma var mı?", "elma" in hashset)

# Tüm elemanları yazdır
print("HashSet:", hashset)






# HashMap: Anahtar -> Değer (key -> value) çiftlerinden oluşur

hashmap = {}

# Anahtar-değer ekleme
hashmap["isim"] = "Mithat"
hashmap["yaş"] = 25
hashmap["şehir"] = "İstanbul"

# Değer güncelleme
hashmap["yaş"] = 26

# Anahtara göre değer okuma
print("İsim:", hashmap.get("isim"))

# Tüm çiftleri yazdırma
for anahtar, değer in hashmap.items():
    print(f"{anahtar}: {değer}")
