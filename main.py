from compression import analyze_image, plot_images

img_path = "C:/Users/ilker/Desktop/1.jpg"
block_size = 8
num_coefficients = 10
color = "y"
plot_images(*analyze_image(img_path, block_size, num_coefficients, color))


# import os
# import shutil
# import json
#
# source_folder = "C:/Users/ilker/Desktop/pnomoni"  # Resimlerin bulunduğu klasör yolu
# destination_folder = "C:/Users/ilker/Desktop/pnomoni2"  # İsimlendirilmiş resimlerin kopyalanacağı klasör yolu
# start_number = 0  # Başlangıç numarası
#
# # Hedef klasörü oluşturma
# if not os.path.exists(destination_folder):
#     os.makedirs(destination_folder)
#
# count = 0
#
# for filename in os.listdir(source_folder):
#     # print file path
#     file_path = source_folder + "/" + filename
#     print(file_path)
#
#     loaded_quantalama = []
#     with open("veri.json", "r") as file:
#         loaded_quantalama = json.load(file)
#
#     print(len(loaded_quantalama))
#
#     for i in range(0, len(loaded_quantalama)):
#         print(file_path)
#         print(loaded_quantalama[i])
#
