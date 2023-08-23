import pandas as pd
import os

# Excel dosyalarının bulunduğu ana klasörü belirtin
parent_folder = "E:/deneme-bitti/"

# a değerini 50'den 100'e kadar döngü ile değiştir
for a in range(0, 50):

    # a değerine göre alt klasör yolu oluştur
    folder_path = os.path.join(parent_folder, str(a))

    # Klasördeki tüm excel dosyalarını al
    excel_files = sorted([f for f in os.listdir(folder_path) if f.endswith(".xlsx")])

    # Klasördeki tüm excel dosyalarını sil
    for file in excel_files:
        file_path = os.path.join(folder_path, file)
        os.remove(file_path)
        print(f"{file} silindi.")
