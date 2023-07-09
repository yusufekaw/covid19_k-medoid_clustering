import pandas as pd
from dateutil.parser import parse

# Membaca file CSV
data = pd.read_csv('covid-19.csv')

# Mengubah format tanggal menjadi "yyyy-mm-dd"
data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')

print(data)

# Mengambil data berdasarkan kriteria
tanggal_awal = '2021-03-01'
tanggal_akhir = '2021-06-30'

filter_data = data.loc[(data['Location'] == 'Jawa Timur') & (data['Date'] > '2021-01-01')]

# Menyimpan kolom yang diinginkan
filter_data = filter_data[['New Cases', 'New Deaths', 'New Recovered', 'New Active Cases', 'Total Cases', 'Total Deaths', 'Total Recovered', 'Total Active Cases']]

# Mengekspor kembali ke file CSV
filter_data.to_csv('dataset.csv', index=False)

print(filter_data)