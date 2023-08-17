import json

# JSON verisini dosyadan oku
with open('../quantization-table.json', 'r') as file:
    data = json.load(file)

# İlk 100 tabloyu koru, geriye kalanları sil
data = data[:100]

# Güncellenmiş JSON verisini dosyaya yaz
with open('../veri.json', 'w') as file:
    json.dump(data, file)
