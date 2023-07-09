import pandas as pd
import numpy as np
from pyclustering.cluster.kmedoids import kmedoids
import matplotlib.pyplot as plt

def sampel_kmedoid(n_klaster, data, data_skala):
    # Inisialisasi indeks medoid secara acak
    insial_medoid = np.random.choice(range(len(data)), size=n_klaster, replace=False)
    # Membuat objek KMedoids
    sampel_kmedoid = kmedoids(data_skala, insial_medoid)
    # Melakukan klastering
    return sampel_kmedoid.process()
def data_medoid(sampel_kmedoid, dataset, atribut):
    # Menampilkan medoid
    medoid_indeks = sampel_kmedoid.get_medoids()
    medoid = dataset.iloc[medoid_indeks][atribut]
    return medoid

def visualisasi(data_skala, label_klaster):
    # Visualisasi klaster
    colors = ['red', 'green', 'blue', 'orange', 'purple']
    markers = ['o', 's', 'D', '^', 'v']


    # Mengambil kolom pertama dan kedua dari data untuk visualisasi
    data_visualisasi = data_skala[:, :2]

    # Mengatur ukuran plot
    plt.figure(figsize=(10, 6))
    
    for i in range(len(data_visualisasi)):
        klaster_idx = label_klaster[i] % len(colors)
        plt.scatter(data_visualisasi[i, 0], data_visualisasi[i, 1], c=colors[klaster_idx], marker=markers[klaster_idx], s=5)
    
    plt.xlabel('New Cases')
    plt.ylabel('New Deaths')
    plt.title('K-Medoids Clustering')
    plt.show()