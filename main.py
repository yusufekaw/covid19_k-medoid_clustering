from sklearn.metrics import silhouette_score
from dataset.proses_data import baca_dataset, atribut_data, normalisasi
from algoritma.kmedoid import sampel_kmedoid, data_medoid, visualisasi

dataset = baca_dataset() # Membaca dataset dari file CSV
atribut, data = atribut_data(dataset) # Mengambil atribut yang akan digunakan untuk klastering
data_skala = normalisasi(data) # Normalisasi data

print("dataset") #cetak dataset
print(dataset) #cetak dataset

# Meminta input jumlah klaster dari pengguna
n_klaster = int(input("Masukkan jumlah klaster yang diinginkan: ")) 

sampel_kmedoid =  sampel_kmedoid(n_klaster, data, data_skala) # Melakukan klastering

label_klaster = sampel_kmedoid.predict(data_skala) # Mendapatkan label klaster untuk setiap sampel


data_medoid = data_medoid(sampel_kmedoid, dataset, atribut) #mendapatkan data medoid
print("medoid : ") # Menampilkan medoid
print(data_medoid) # Menampilkan medoid

dataset['Klaster'] = label_klaster # Menambahkan kolom "Cluster" ke dalam dataset
print("klaster") # Menampilkan hasil klastering
print(dataset[atribut + ['Klaster']]) # Menampilkan hasil klastering

visualisasi(data_skala, label_klaster) # Visualisasi klaster

# Menghitung silhouette score
silhouette= silhouette_score(data_skala, label_klaster)
print("Skor Silhouette :", round(silhouette,2))