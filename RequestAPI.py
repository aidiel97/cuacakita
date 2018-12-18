import requests
import json
# import numpy as np
from translator import Translate
from check import Check
import time

translate = Translate()
check = Check()

class RequestAPI:
	def get_by_city(self, c):
		self.url = "http://api.openweathermap.org/data/2.5/forecast"
		self.querystring = {"appid":"2651c986fc0256f04e92c5a71d08e870"}
		self.querystring['q'] = c
		response = requests.request("GET", self.url, params=self.querystring)
		# print("Mengumpulkan data cuaca kota", c)
		print("\r" + "Berhasil mengumpulkan data cuaca kota " + c + ".....")
		return json.loads(response.text)

	def get_by_coordinate(self, lat, lon):
		self.url = "http://api.openweathermap.org/data/2.5/forecast"
		self.querystring = {"appid":"2651c986fc0256f04e92c5a71d08e870"}
		self.querystring['lat'] = lat
		self.querystring['lon'] = lon
		response = requests.request("GET", self.url, params=self.querystring)
		return json.loads(response.text)

	def get_sys(self, c):
		self.url = "http://api.openweathermap.org/data/2.5/weather"
		self.querystring = {"appid":"2651c986fc0256f04e92c5a71d08e870"}
		self.querystring['q'] = c
		response = requests.request("GET", self.url, params=self.querystring)
		return json.loads(response.text)

	def get_time(self, date, city):
		response = requests.request("GET", "https://api.aladhan.com/timingsByAddress/"+date+"?address="+city+",Indonesia&method=11")
		return json.loads(response.text)

	def get_syssun(self, lt):
		r = lt['sys']['sunrise']
		s = lt['sys']['sunset']

		sunrise = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(r))
		sunset = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(s))

		return sunrise, sunset


	def get_data(self, data, array):
		for a in range(len(data['list'])):
			# hujan = data['list'][a]['rain']['3h']
			# print(hujan,a)
		# for a in range (0,1):
			n_kota = data['city']['name']
			waktu =  data['list'][a]['dt_txt']
			tgl = str(waktu)[:10]
			jam = (str(waktu)[11:])[:2]
			c = data['list'][a]['weather'][0]["id"]
			cuaca = translate.translate(c)
		
		# for b in range(len(data['list'])):
			#data suhu udara
			suhu = round(data['list'][a]['main']['temp']-273.15)
			# suhu = data['list'][a]['main']['temp']

			# k_suhu = check.check_suhu(suhu)
			
			#data kelembapan
			kelembapan = data['list'][a]['main']['humidity']
			# k_kelembapan = check.check_kelembapan(kelembapan)

			#tiupan angin
			arah_angin = data['list'][a]['wind']['deg']
			kecepatan_angin = data['list'][a]['wind']['speed']
			# kec_angin = check.check_kecepatanangin(kecepatan_angin)
			# a_angin = check.check_arahangin(arah_angin)

			#curah hujan
			hujan = ""
			k_hujan = ""
			if 'rain' in data['list'][a]:
				if  '3h' in data['list'][a]['rain']:
					hujan = data['list'][a]['rain']['3h']
					# k_hujan = check.check_hujan(hujan)

			# urgensi
			if(c >= 800):
				urgensi = check.check_suhu_normal(suhu, n_kota)
			elif(c >= 300 and c <= 312):
				if(c < 312):
					urgensi = 1
				else:
					urgensi = 0
			elif(c >= 500 and c <= 531):
				if(c <= 511 and c >= 503):
					urgensi = 4
				elif(c == 522):
					urgensi = 2
				else:
					urgensi = 0
			elif(c >= 200 and c <= 232):
				if(c >= 211):
					urgensi = 3
				else:
					urgensi = 0
			elif(c >= 701 and c <= 781):
				urgensi = 5
			else:
				urgensi = 6

			array.append({
				'kota':n_kota,
				'waktu':waktu,
				'tgl':tgl,
				'jam':jam,
				'id_cuaca':c,
				'cuaca':cuaca,
				'suhu':suhu,
				'kelembapan':kelembapan,
				'kec_angin':kecepatan_angin,
				'a_angin':arah_angin,
				'hujan' : hujan,
				# 'k_hujan' : k_hujan,
				'urgensi':urgensi
			})
		return array