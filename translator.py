import re

class Translate:
	def translate(self,idt):
		dictionary = {
			200: "petir disertai hujan dengan instensitas rendah",
			201: "petir disertai hujan",
			202: "petir disertai hujan dengan instesitas tinggi",
			210: "badai petir dengan intensitas rendah",
			211: "hujan badai",
			212: "badai petir dengan intensitas tinggi",
			221: "badai topan",
			230: "badai petir disertai hujan dengan instensitas rendah",
			231: "badai petir disertai hujan dengan instensitas sedang",
			232: "badai petir disertai hujan dengan instensitas tinggi",
			300: "hujan dengan intensitas sangat rendah (rintik-rintik)",
			301: "hujan dengan intensitas rendah (gerimis",
			302: "hujan",
			310: "gerimis saat terang",
			311: "hujan dengan instensitas rendah",
			312: "gerimis dengan awan tebal",
			313: "hujan",
			314: "hujan dengan intensitas tinggi",
			321: "gerimis besar",
			500: "hujan gerimis",
			501: "hujan",
			502: "hujan dengan intensitas tinggi",
			503: "hujan dengan intensitas tinggi disertai angin kencang",
			504: "hujan dengan intensitas yang sangat tinggi",
			511: "hujan es",
			520: "hujan intensitas rendah disertai awan tebal",
			521: "hujan disertai awan tebal",
			522: "hujan intensitas tinggi disertai awan tebal",
			531: "hujan badai",
			600: "salju ringan",
			601: "salju",
			602: "salju lebat",
			611: "hujan es",
			612: "hujan es deras",
			615: "hujan ringan dengan salju",
			616: "hujan dengan salju",
			620: "salju ringan",
			621: "salju lebat",
			622: "badai salju",
			701: "kabut",
			711: "kabut asap",
			721: "kabut tipis",
			731: "debu pasir",
			741: "embun",
			751: "pasir",
			761: "debu",
			762: "abu vulkanik",
			771: "hujan badai disertai angin kencang",
			781: "angin topan",
			800: "cerah",
			801: "sedikit mendung",
			802: "berawan",
			803: "sebagian besar berawan",
			804: "mendung"
		}
		return dictionary[idt] if idt in dictionary else "-"

	def kamusDaerah(self, x):
		#pembuatan corpus		
		# withouthduplicate = list(dict.fromkeys(corps))
		# print(withouthduplicate)

		# print(call.replace(" ",""))
		# v = call.replace("\n"," ") #ubah newline jadi spasi
		# w = call.replace(" ","") #hapus spasi
		#hapus kurung
		# x = call.replace("("," ")
		# y = x.replace(")","")

		# xfile = open("daerah.txt", "w")

		# for x in range(len(withouthduplicate)):
		# 	xfile.write(withouthduplicate[x] + " ")

		# xfile.close()


		# # print(daerah)

		# ayam = "ayam bakar #enak #gokil"
		# j = re.findall(r"#(\w+)", ayam)
		# print(j)

		file = open("daerah.txt", "r")
		call = file.read()
		corps = call.split()
		file.close()

		qt = open("quotes.txt", "r", encoding="utf8")
		qt_call = qt.read()
		qt_corps = qt_call.split()
		qt.close()

		if len(x) != 0:
			# print(x)
			y = x[0].replace("#","")

			for lines in corps:
				if y == lines.lower():
			# if y in corps:
					last = re.sub(r"(\w)([A-Z])", r"\1 \2", y)
					# print(last)
					return last
			else:
				z = x[0].replace("#","")

				if z in qt_corps:
					return "quotes"
				else:
					return "idk"

		else:
			# print("no")
			return "no"

	def quotes(self, x):
		quotes = []
		filepath = 'quotes.txt'  
		with open(filepath, encoding="utf8") as fp:  
		   line = fp.readline()
		   cnt = 1
		   while line:
		   	# if "galau" in line :
		   		# print("Line {}: {}".format(cnt, line.strip()))
		   		quotes.append(format(line.strip()))
		   		line = fp.readline()
		   		cnt += 1
		   		
		for qt in quotes:
			if x in qt:
				return qt
			else:
				return "empty"

	def kamusCuaca(self, x):
		
		cuaca = ['gerimis', 'hujan', 'salju', 'kabut', 'embun', 'pasir', 'debu', 'berawan', 'mendung', 'cerah', 'badai', 'topan', 'ringan', 'berat', 'lokal', 'besar', 'deras', 'es', 'lebat', 'asap', 'tipis', 'abu', 'vulkanik', 'langit', 'sedikit', 'petir', 'hebat', 'saat', 'terang', 'sangat', 'sebagian', 'awan', 'tebal', 'kencang']

		cuaca1=['gerimis', 'hujan', 'salju', 'kabut', 'embun', 'pasir', 'debu', 'berawan', 'mendung', 'cerah']
		cuaca2=['cerah berawan','hujan badai', 'badai topan', 'gerimis ringan', 'gerimis berat', 'hujan gerimis', 'hujan lokal', 'gerimis besar', 'hujan gerimis', 'hujan deras', 'hujan es', 'hujan badai', 'salju ringan', 'salju lebat', 'hujan es', 'salju ringan', 'salju lebat', 'badai salju', 'kabut asap', 'kabut tipis', 'debu pasir', 'abu vulkanik', 'angin topan', 'langit cerah', 'sedikit mendung']
		cuaca3=['petir disertai hujan', 'badai petir ringan', 'badai petir hebat', 'gerimis saat terang', 'hujan sangat deras', 'hujan es deras', 'hujan dengan salju', 'sebagian besar berawan']
		cuaca4=['petir disertai hujan ringan', 'petir disertai hujan deras', 'badai petir disertai gerimis', 'gerimis dengan awan tebal', 'hujan ringan awan tebal', 'hujan disertai awan tebal', 'hujan ringan dengan salju']
		cuaca5=['badai petir disertai gerimis ringan', 'badai petir disertai hujan deras', 'hujan deras di beberapa tempat', 'hujan deras disertai angin kencang', 'hujan deras disertai awan tebal', 'hujan badai disertai angin kencang']
		
		if x==1:
			return cuaca1
		elif x==2:
			return cuaca2
		elif x==3:
			return cuaca3
		elif x==4:
			return cuaca4
		elif x==5:
			return cuaca5

		elif x==0:
			return cuaca
		
# 	def weatherDict(self):

# 		weather = ['gerimis', 'hujan', 'salju', 'kabut', 'embun', 'pasir', 'debu', 'berawan', 'mendung', 'cerah', 'badai', 'topan', 'ringan', 'berat', 'lokal', 'besar', 'deras', 'es', 'lebat', 'asap', 'tipis', 'abu', 'vulkanik', 'angin', 'langit', 'sedikit', 'petir', 'hebat', 'saat', 'terang', 'sangat', 'sebagian', 'awan', 'tebal', 'kencang']

# 		return weather



# 	def addWeather(self):

# 		array = []

# 		translate = Translate()

# 		data = translate.kamusCuaca(5)
# 		cek = translate.weatherDict()

# 		for i in range(len(data)):
# 			for j in data[i].split():
# 				if j not in cek and j not in array:
# 					array.append(j)

# 		print(array)

translate = Translate()
translate.kamusDaerah("#medan")
# translate.addWeather()