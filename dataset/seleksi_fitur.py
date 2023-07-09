import pandas as pd
from dateutil.parser import parse

# Membaca file CSV
data = pd.read_csv('covid-19.csv')
# Mengubah format tanggal menjadi "yyyy-mm-dd"
data['Date'] = data['Date'].apply(lambda x: parse(x, dayfirst=True).strftime('%Y-%m-%d'))

# Mengambil data berdasarkan kriteria
tanggal_awal = '2021-01-01'
tanggal_akhir = '2021-09-07'

dataset = data[(data['Island'] == 'Jawa') & (data['Date'].between(tanggal_awal, tanggal_akhir))]

# Menyimpan kolom yang diinginkan
dataset = dataset[['New Cases', 'New Deaths', 'New Recovered', 'New Active Cases', 'Total Cases', 'Total Deaths', 'Total Recovered', 'Total Active Cases']]

# Mengekspor kembali ke file CSV
dataset.to_csv('dataset.csv', index=False)

print(dataset)