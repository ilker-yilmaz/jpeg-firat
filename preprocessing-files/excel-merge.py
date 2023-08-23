#
# import pandas as pd
# import os
#
# # Boş bir DataFrame oluştur
# combined_data = pd.DataFrame(columns=["Tablo", "PSNR", "Compression Ratio"])
# a=50
# # Excel dosyalarının bulunduğu klasörü belirtin
# folder_path = "E:/deneme-bitti/"+str(a)
#
# # Klasördeki tüm excel dosyalarını al
# excel_files = sorted([f for f in os.listdir(folder_path) if f.endswith(".xlsx")])
#
# # Her excel dosyasını oku, verileri numaralandır ve combined_data DataFrame'e ekle
# for file in excel_files:
#     file_path = os.path.join(folder_path, file)
#     df = pd.read_excel(file_path)
#
#     # Dosya adından tablo numarasını al
#     table_number = int(file.split("-")[-1].replace("compressed", "").replace(".xlsx", ""))
#
#     # Verilere tablo numarasını ekle
#     df.insert(0, "Tablo", table_number)
#
#     combined_data = pd.concat([combined_data, df])
#
# # Tablo numarasına göre DataFrame'i sırala
# combined_data_sorted = combined_data.sort_values(by="Tablo")
#
# # Birleştirilmiş verileri yeni bir excel dosyasına kaydet
# combined_data_sorted.to_excel("compressed-"+str(a)+".xlsx", index=False)

import pandas as pd
import os

# Excel dosyalarının bulunduğu ana klasörü belirtin
parent_folder = "E:/deneme-bitti/"

# a değerini 50'den 100'e kadar döngü ile değiştir
for a in range(50, 101):
    # Boş bir DataFrame oluştur
    combined_data = pd.DataFrame(columns=["Tablo", "PSNR", "Compression Ratio"])

    # a değerine göre alt klasör yolu oluştur
    folder_path = os.path.join(parent_folder, str(a))

    # Klasördeki tüm excel dosyalarını al
    excel_files = sorted([f for f in os.listdir(folder_path) if f.endswith(".xlsx")])

    # Her excel dosyasını oku, verileri numaralandır ve combined_data DataFrame'e ekle
    for file in excel_files:
        file_path = os.path.join(folder_path, file)
        df = pd.read_excel(file_path)

        # Dosya adından tablo numarasını al
        table_number = int(file.split("-")[-1].replace("compressed", "").replace(".xlsx", ""))

        # Verilere tablo numarasını ekle
        df.insert(0, "Tablo", table_number)

        combined_data = pd.concat([combined_data, df])

    # Tablo numarasına göre DataFrame'i sırala
    combined_data_sorted = combined_data.sort_values(by="Tablo")

    # Birleştirilmiş verileri yeni bir excel dosyasına kaydet
    output_file_name = "compressed-" + str(a) + ".xlsx"
    combined_data_sorted.to_excel(output_file_name, index=False)
    print(f"{output_file_name} dosyası oluşturuldu.")
