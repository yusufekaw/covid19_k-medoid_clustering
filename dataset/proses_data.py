import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


def baca_dataset():
	# Membaca dataset dari file CSV
	dataset = pd.read_csv("/home/ucup/projects/python/ghofur/dataset/dataset.csv")
	return dataset

def atribut_data(dataset):
	# Mengambil atribut yang akan digunakan untuk klastering
	atribut = ['New Cases', 'New Deaths', 'New Recovered', 'New Active Cases', 'Total Cases', 'Total Deaths', 'Total Recovered', 'Total Active Cases']
	data = dataset[atribut].values
	data = pd.DataFrame(data)
	return atribut, data

def normalisasi(data):
	# Normalisasi data
	scaler = StandardScaler()
	data_skala = scaler.fit_transform(data)
	return data_skala
