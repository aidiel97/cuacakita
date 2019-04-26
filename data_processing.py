from RequestAPI import RequestAPI
from check import Check
import datetime
from data import Data
# import operator,re
import random
from translator import Translate
import pytz
request = RequestAPI()
check = Check()

array_data = []

class Data_processing:
	def getArray(self):
		print("Mengumpulkan data mentah.....")
		request.get_data(request.get_by_city('Medan'), array_data)
		request.get_data(request.get_by_city('Jakarta'), array_data)
		request.get_data(request.get_by_city('Surabaya'), array_data)
		request.get_data(request.get_by_city('Bandung'), array_data)
		request.get_data(request.get_by_city('Makassar'), array_data)
		request.get_data(request.get_by_city('Semarang'), array_data)
		request.get_data(request.get_by_city('Palembang'), array_data)
		request.get_data(request.get_by_city('Balikpapan'), array_data)
		request.get_data(request.get_by_city('Ambon'), array_data)
		request.get_data(request.get_by_city('Denpasar'), array_data)

		# d = Data()
		# array_data = d.getSampleData()

		print("-----PENGUMPULAN DATA SUKSES-----")
		return array_data

	def getCityData(self, city):
		request.get_data(request.get_by_city(city),array_data)

		return array_data

	def dataProcessing(self,array_data):
		
		print("\n\n"+ "Memulai pemrosesan data.....")
		tz = pytz.timezone('Asia/Jakarta')

		today = datetime.datetime.now(tz) 
		# today = datetime.datetime(2018, 11, 28, 21, 35, 50, 593000) 
		# print(today)
		# exit()
		tgl_sekarang = str(today)[:10]
		tomorrow = today + datetime.timedelta(1)
		tgl_besok = str(datetime.datetime.strftime(tomorrow,'%Y-%m-%d'))[:10]
		jam_sekarang = int((str(today)[11:])[:2])
		# print(tgl_besok)
		# print(jam_sekarang)

		# membuang data yang bukan hari ini
		i=0
		while i < len(array_data):	
			# print("sekarang jam: ",array_data[i]['waktu'])
			waktu = str(array_data[i]['waktu'])
			jam = int((waktu[11:])[:2])
			tanggal = waktu[:10]
			
			if(jam_sekarang >= 21 and jam == 0 and tanggal == tgl_besok):
				i += 1
			elif(tanggal != tgl_sekarang):
				del array_data[i]
			else:
				i += 1

		# membuang data lampau
		j=0
		while j < len(array_data):
			waktu = str(array_data[j]['waktu'])
			jam = int((waktu[11:])[:2])
			tanggal = waktu[:10]
			if(jam_sekarang >= 21 and jam == 0 and tanggal == tgl_besok):
				j += 1
			elif(jam <= jam_sekarang):
				del array_data[j]
			else:
				j += 1

		max = 0
		k = 0
		for j in range(len(array_data)):
			urg = array_data[j]['urgensi']
			if(urg > max):
				max = urg
				k = j
			else:
				max = 0
				k = 0

		if(max!=0):
			choosen = array_data[k]
		else:
			choosen = random.choice(array_data)

		# choosen = []
		# if(max!=0):
		# 	for data in range(len(array_data)):
		# 		choosen.append(array_data[k])
		# else:
		# 	choosen.append(random.choice(array_data))

		# for data in range(len(array_data)):
		# 		choosen.append(array_data[k])
	
		# get sunrise&sunset time
		# sunrise, sunset = request.get_syssun(request.get_sys(choosen['kota']))
		# r = int((str(sunrise)[11:])[:2])
		# s = int((str(sunset)[11:])[:2])

		# suhu_sebelum = 0
		# cuaca_sebelum = ""
		# print(choosen)
		data_process = []
		# dp = []
		# for data in range(len(choosen)):
		for x in range(len(array_data)):
			if(array_data[x]['kota'] == choosen['kota']):
				jam = int(array_data[x]['jam'])
				hashtag_kota = "#"+array_data[x]['kota']

				# time = request.get_time(array_data[x]['tgl'], array_data[x]['kota'])
				print("\n\n"+ "Memulai lexicalisasi data.....")
				#data suhu udara
				suhu = round(array_data[x]['suhu']-273.15)
				# suhu = data['list'][a]['main']['temp']
				k_suhu = check.check_suhu(suhu)
				
				#data kelembapan
				kelembapan = array_data[x]['kelembapan']
				k_kelembapan = check.check_kelembapan(kelembapan)

				#tiupan angin
				arah_angin = array_data[x]['a_angin']
				kecepatan_angin = array_data[x]['kec_angin']
				kec_angin = check.check_kecepatanangin(kecepatan_angin)
				a_angin = check.check_arahangin(arah_angin)

				#curah hujan
				hujan = array_data[x]['hujan']
				if(hujan != ""):
					k_hujan = check.check_hujan(int(hujan))
				else:
					k_hujan = ""

				print("-----LEXICALISASI DATA SUKSES-----")

				data_process.append({
					'kota':hashtag_kota,
					'tgl':array_data[x]['tgl'],
					'waktu':array_data[x]['waktu'],
					# 'waktu':check.check_lexwaktu(jam, r, s),
					'jam':jam,
					# 'waktu':check.check_detailwaktu(jam, time),
					'id_cuaca':array_data[x]['id_cuaca'],
					'cuaca':array_data[x]['cuaca'],
					'suhu':array_data[x]['suhu'],
					'k_suhu':k_suhu,
					'kec_angin':kec_angin,
					'hujan':array_data[x]['hujan'],
					'k_hujan':k_hujan,
					'a_angin':a_angin,
					'kelembapan':array_data[x]['kelembapan'],
					'k_kelembapan':k_kelembapan
				})
			# dp.append(data_process)
			# dp = data_process

		del array_data[:]
		print("-----PEMROSESAN DATA SUKSES-----")
		print(data_process)
		return data_process

	def kalimatTemplate(self,kota,waktu,cuaca,suhu,angin,aangin,kelembapan,sentence):
		thp1 = sentence.replace("x_kota",kota)
		thp2 = thp1.replace("x_waktu",waktu)
		thp3 = thp2.replace("x_cuaca",cuaca)
		thp4 = thp3.replace("x_suhu",suhu)
		thp5 = thp4.replace("x_angin",angin)
		thp6 = thp5.replace("x_aangin",aangin)
		thp7 = thp6.replace("x_kelembapan",kelembapan)
		return thp7

# a = Data_processing()
# print(a.getArray())
# a.dataProcessing(a.getArray())
# a.dataProcessing(a.getCityData("Medan"))
# print(x)
# today = datetime.datetime.now() 
# print(today)