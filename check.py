class Check:
	def check_suhu(self, suhu):
		if suhu<=10:
			k_suhu = "sangat dingin"
		elif suhu>10 and suhu<=19:
			k_suhu = "dingin"
		elif suhu>19 and suhu<=27:
			k_suhu = "normal"
		elif suhu>27 and suhu<=33:
			k_suhu = "panas"
		else:
			k_suhu = "sangat panas"

		return k_suhu

	def check_suhu_normal(self, suhu, kota): #https://id.climate-data.org
		if(kota=='medan' or kota=='jakarta' or kota=='surabaya' or kota=='makassar' or kota=='semarang' or kota=='palembang' or kota=='denpasar'):
			if(suhu >= 32 or suhu < 21):
				return 4
			else:
				return 0
		elif(kota=='ambon' or kota=='bandung' or kota=='balikpapan'):
			if(suhu > 30 or suhu < 18):
				return 4
			else:
				return 0
		else:
			return 0;

	def check_kelembapan(self, kelembapan):
		if kelembapan < 70 :
			k_kelembapan = "sangat rendah"
		elif kelembapan >= 70 and kelembapan <= 80 :
			k_kelembapan = "rendah"
		elif kelembapan > 80 and kelembapan <= 90:
			k_kelembapan = "normal"
		elif kelembapan > 90 and kelembapan <= 95:
			k_kelembapan = "tinggi"
		else:
			k_kelembapan = "sangat tinggi"

		return k_kelembapan

	def check_arahangin(self, deg):
		
		def mata_angin(arah):
			if arah != 0:
				mata_angin = {
					1: "timur laut",
					2: "timur",
					3: "tenggara",
					4: "selatan",
					5: "barat daya",
					6: "barat",
					7: "barat laut",
					8: "utara"
				}
			else:
				return "utara"			
			return mata_angin[arah]

		arah = round(deg/45)
		sisa = round(deg%45)
		# print(str(sisa) + "° dari arah " + str(mata_angin[arah]))

		hasil = str(sisa) + "° dari arah " + str(mata_angin(arah))

		return hasil

	def check_kecepatanangin(self, kec):
		if kec == 0:
			k_kec = "sangat tenang"
		elif kec > 0 and kec <= 5:
			k_kec = "pelan"
		elif kec > 5 and kec <= 8: 
			k_kec = "sedang"
		elif kec > 8 and kec <= 11:
			k_kec = "cukup kencang"
		elif kec > 11 and kec <= 17:
			k_kec = "kencang"
		else:
			k_kec = "sangat kencang"

		return k_kec

	def check_hujan(self, hjn):
		if hjn <= 100:
			k_hjn = "rendah"
		elif hjn > 100 and hjn <=300:
			k_hjn = "menengah"
		elif hjn > 300 and hjn <=400:
			k_hjn = "tinggi"
		elif hjn > 400:
			k_hjn = "sangat tinggi"

		return k_hjn 

	def check_lexwaktu(self, jam, sr, ss):
		if jam >= sr and jam <= 12:
			lex = "pagi"
		elif jam >= 12 and jam <= ss:
			lex = "siang"
		else:
			lex = "malam" 

		return lex

	def check_detailwaktu(self, jam, time):
		sunrise = int((time['data']['timings']['Sunrise'])[:2])
		petang = int((time['data']['timings']['Asr'])[:2])
		sunset = int((time['data']['timings']['Sunset'])[:2])
		midnight = int((time['data']['timings']['Midnight'])[:2])
		

		if jam >= sunrise and jam <= 11:
			lex = "pagi"
		elif jam >= 11 and jam < petang:
			lex = "siang"
		elif jam >= petang and jam <= sunset:
			lex = "petang"
		elif jam > sunset:
			lex = "malam"
		else:
			lex = "dini hari" 

		return lex

	def check_perubahan(self, a, b):
		if a >= b :
			perubahan = "naik"
		elif a == b :
			perubahan = "tetap"
		elif a <= b :
			perubahan = "turun"

	def check_perubahan(self, a, b):
		if a != b :
			perubahan = "cuaca berubah"
		elif a == b :
			perubahan = "cuaca tidak berubah"