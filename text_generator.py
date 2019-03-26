import random
from data_processing import Data_processing
from datetime import datetime
from verba_finder import Verba_finder
import pytz
# import nltk
# from nltk import ngrams
# from check import Check
# import operator
# import difflib
# from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
# from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

# from sentenceTemplate import SentenceTemplate

class Text_generator:
	def getData(self):
		data = Data_processing()

		forecast_data = data.dataProcessing(data.getArray())

		return forecast_data

	def generator(self, sample_array):
		this = Text_generator()
		verba = Verba_finder()
		print("\n\n"+ "Memulai proses pembangkitan kalimat...")

		#CONTOH SPOK : cuaca kota medan diprediksi hujan pada pagi hari
		#di kota medan diprediksi cuaca akan hujan pada pagi hari , di kota medan diprediksi suhu akan normal pada pagi hari
		#CONTOH TOPIK KOMEN : kota medan, cuacanya diprediksi hujan pada pagi hari
		sentence_temp = ["[SUBJEK][PREDIKAT][OBJEK][KETERANGAN]","[TOPIK], [KOMEN]"]
		topik = "[KETERANGAN_S]"
		komen = "[SUBJEK][PREDIKAT][OBJEK][KETERANGAN]"
		subjek = ["[NOMINA] [KETERANGAN_S]","[KETERANGAN_S]"]
		predikat = verba.main()

		print("Mendapatkan data terproses...")
		# print(sample_array[0]['jam'])
		
		# jika data yang akan diolah pukul 12 malam
		if(sample_array[0]['jam'] == 0):
			waktu = "pukul 00.00 nanti"
		else:
			time = str(sample_array[0]['jam']) + ':01:00'
			tz = pytz.timezone('Asia/Jakarta')
			now = str(datetime.now(tz).time()).split('.', 1)[0]
			FMT = '%H:%M:%S'
			tmdelta = datetime.strptime(time, FMT) - datetime.strptime(now, FMT)
			tdua = ":"
			beda = "tidak teridentifikasi"
			jam = str(tmdelta)[:1]
			menit = str(tmdelta)[2:].split(tdua, 2)[0]
			# if (jam == "0"): 
			# 	if(menit[:1] == "0"):
			# 		beda = menit[1:] + " menit"
			# 	else:
			# 		beda = menit + " menit"
			# elif(jam == "0" and menit =="00"):
			# 	beda = str(tmdelta)[5:] + " detik"
			# else:
			# 	if(menit == "00" or menit == ""):
			# 		beda = jam + " jam"
			# 	else:
			# 		beda = jam + " jam " + menit + " menit"

			# waktu = str(beda) + " kedepan"
			waktu = str(jam) + " jam kedepan"

		c_hujan = sample_array[0]['k_hujan']

		ket = {'kota': sample_array[0]['kota'],'tanggal':sample_array[0]['tgl'],'waktu':waktu}
		nom = {'cuaca': sample_array[0]['cuaca'], 'suhu': sample_array[0]['k_suhu'], 'kelembaban udara': sample_array[0]['k_kelembapan'], 'curah hujan':c_hujan}
		
		ket_sebelum = ''
		sentenceTemplate = random.choice(sentence_temp)
		if(sentenceTemplate == "[TOPIK], [KOMEN]"):
			topik_r = sentenceTemplate.replace("[TOPIK]",topik)
			komen_r = topik_r.replace("[KOMEN]",komen)

			subjek_temp = this.cekKelengkapan('subjek', topik)
			sub_r1 = komen_r.replace("[SUBJEK]",subjek_temp)
			s_keterangan, ket_sebelum = this.keteranganGenerator('waktu', ket)
			sub_r2 = sub_r1.replace("[KETERANGAN_S]",s_keterangan)
			sub_final = sub_r2.split(' ',1)[1] #menghapus awalan dari keterangan

			predikat_temp = random.choice(predikat)
			pred_final = sub_final.replace("[PREDIKAT]",predikat_temp)

			objek_temp = this.cekKelengkapan('objek', subjek_temp)
			obj_r1 = pred_final.replace("[OBJEK]",objek_temp)
			nomina, pronomina = this.objekGenerator(nom, c_hujan)
			obj_r2 = obj_r1.replace("[NOMINA]", nomina)
			obj_final = obj_r2.replace("[PRONOMINA]", pronomina)

			keterangan, ket_sebelum = this.keteranganGenerator(ket_sebelum, ket)
			final_sentence = obj_final.replace("[KETERANGAN]",keterangan)

		else:
			subjek_temp = random.choice(subjek)
			sub_r1 = sentenceTemplate.replace("[SUBJEK]",subjek_temp)
			s_keterangan, ket_sebelum = this.keteranganGenerator(ket_sebelum, ket)
			sub_final = sub_r1.replace("[KETERANGAN_S]",s_keterangan)

			predikat_temp = random.choice(predikat)
			pred_final = sub_final.replace("[PREDIKAT]",predikat_temp)

			objek_temp = this.cekKelengkapan('objek', subjek_temp)
			obj_r1 = pred_final.replace("[OBJEK]",objek_temp)
			nomina, pronomina = this.objekGenerator(nom, c_hujan)
			obj_r2 = obj_r1.replace("[NOMINA]", nomina)
			obj_final = obj_r2.replace("[PRONOMINA]", pronomina)

			keterangan, ket_sebelum = this.keteranganGenerator(ket_sebelum, ket)
			final_sentence = obj_final.replace("[KETERANGAN]",keterangan)

		# hapus spasi di akhir kalimat jika ada
		if final_sentence.endswith(" "):
			final_sentence = final_sentence[:len(final_sentence)-1]

		# mengubah awal kalimat menjadi huruf kapital
		g = list(final_sentence)
		if g[0].islower():
			g[0]=g[0].upper()
		final_sentence = "".join(g)

		generated_sentence = final_sentence+ "." + "\n\nSumber data : OpenWeather"#menambah titik
		print("-----PROSES PEMBANGKITAN KALIMAT BERHASIL-----"+"\n\n")
		return generated_sentence
		# return sample_array

	def cekKelengkapan(self, param1, param2):
		subjek = ["[NOMINA][KETERANGAN_S]","[KETERANGAN_S]"]
		if(param1 == 'objek'):
			if(param2 == '[KETERANGAN_S]'):
				return '[NOMINA]nya akan [PRONOMINA]'
			else:
				return '[PRONOMINA]'

		elif(param1 == 'subjek'):
			if(param2 == '[KETERANGAN_S]'):
				return "[NOMINA]nya"
			else:
				return random.choice(subjek)

	def objekGenerator(self, nom, k_hujan):
		if(k_hujan==""):
			opsi = ['cuaca', 'suhu', 'kelembaban udara']
		else:
			opsi = ['cuaca', 'suhu', 'kelembaban udara', "curah hujan"]
		nomina = random.choice(opsi)
		pronomina = nom[nomina] + " "
		return nomina , pronomina

	def keteranganGenerator(self, parameter, ket):
		# pembentukan klausa keterangan 1
		opsi = ['kota', 'waktu', 'dua']

		if parameter=="":
			keterangan = random.choice(opsi)
		elif parameter=="dua":
			return "", 'dua'
		else:
			x=0
			while x < len(opsi):
				if opsi[x] == parameter:
					del opsi[x]
				else:
					x+=1
			keterangan = opsi[0]


		if(keterangan == 'kota'):
			keterangan_temp ='di '+keterangan+" "+ket[keterangan]
		elif(keterangan == 'dua'):
			keterangan_temp = 'di '+opsi[0]+" "+ket['kota']+' pada '+ket['waktu']
		else:
			keterangan_temp ='pada '+ket[keterangan]
		
		return keterangan_temp, keterangan

a = Text_generator()
x = a.getData()
print(a.generator(x))
# time = str(x[0]['jam']) + ':00:00'
# now = str(datetime.now().time()).split('.', 1)[0]
# FMT = '%H:%M:%S'
# tmdelta = datetime.strptime(time, FMT) - datetime.strptime(now, FMT)
# tdua = ":"
# beda = str(tmdelta)
# print("sekarang",now)
# print("waktu array",time)
# print("perbedaan",beda)

#pada waktu pagi, kelembaban udara di kota medan diperkirakan rendah
# Di kota #Medan pada waktu pagi diprediksi kelembaban udara akan rendah. <tidak bisa> 
# --> kelembabn udara di kota medan pada waktu pagi diprediksi rendah
# nlg lexicalization near synonym <pelajari yg dictionary base>
# pada tiga jam kedepan, kelembaban udara di kota medan di perkirakan rendah<contoh>
# pada tiga jam -> waktu dari data - waktu sekarang