import os
import re

folder_path = "E:/deneme-bitti/75"  # Eksik dosyaları kontrol etmek istediğiniz klasörün yolu
start_num = 0  # Başlangıç numarası
end_num = 499  # Bitiş numarası

existing_files = set()

# Mevcut dosyaları tarayarak numaraları set'e ekleyin
for filename in os.listdir(folder_path):
    if filename.startswith("compressed-"):
        match = re.search(r"compressed-\d+-(\d+)\.xlsx", filename)
        if match:
            num = int(match.group(1))
            existing_files.add(num)

# Eksik dosya numaralarını bulun ve yazdırın
missing_files = [num for num in range(start_num, end_num + 1) if num not in existing_files]

print("Eksik dosya numaraları:")
print(missing_files)
