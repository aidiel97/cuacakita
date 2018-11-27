from nltk.tag import CRFTagger
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

# ct = CRFTagger()
# ct.set_model_file('all_indo_man_tag_corpus_model.crf.tagger')
# # hasil = ct.tag_sents([['Saya','bekerja','di','Bandung', 'memprediksi','meramalkan']])
# hasil = ct.tag_sents([corpus]) 

# for x in range(len(hasil[0])):
# 	if hasil[0][x][1] == 'VB':
# 		print(hasil[0][x])

#Dengan training

# jumSample = 500000
# namaFile = "Indonesian_Manually_Tagged_Corpus.tsv"
# with open(namaFile, 'r', encoding='utf-8') as f:
#     lines = f.read().split('\n')
 
# pasangan = []
# allPasangan = []
 
# for line in lines[: min(jumSample, len(lines))]:
#     if line == '':
#         allPasangan.append(pasangan)
#         pasangan = []
#     else:
#         kata, tag = line.split('\t')
#         p = (kata,tag)
#         pasangan.append(p)
 
# ct = CRFTagger()
# ct.train(allPasangan,'all_indo_man_tag_corpus_model.crf.tagger')
# ct.set_model_file('all_indo_man_tag_corpus_model.crf.tagger')
# #test
# hasil = ct.tag_sents([['Saya','bekerja','di','Bandung','suhu'],['Nama','saya','Yudi']])
# print(hasil)

class Verba_finder:
	def main(self):
		# metode SENDIRI
		file = open("forecast_corpus.txt", "r")
		call = file.read()
		corpus = call.split()
		file.close()
		verba = []

		# stopword removal
		# sfactory = StopWordRemoverFactory()
		# stopwords = sfactory.create_stop_word_remover()
		# stop = stopwords.remove(call)
		# c = stop.split()
		
		# print("Membaca corpus.....")
		ct = CRFTagger()
		ct.set_model_file('all_indo_man_tag_corpus_model.crf.tagger')
		hasil = ct.tag_sents([corpus])
		
		this = Verba_finder()
		for x in range(len(hasil[0])):
			if hasil[0][x][1] == 'VB' and this.afiks_check(hasil[0][x][0]) == 1 and (hasil[0][x+1][1] == 'NN' or hasil[0][x+1][1] == 'JJ'):
				# print(hasil[0][x])
				verba.append(" "+hasil[0][x][0]+" ")
		
		return verba
		# print("Jumlah kata dalam corpus :",len(corpus))

	
	def afiks_check(self, a):
		factory = StemmerFactory()
		stemmer = factory.create_stemmer()

		meng = ['a','e','i','o','u','k','g','h','x']
		me = ['m','n','r','y','w','l']
		men = ['d','t']
		mem = ['b','p','f']
		meny = ['c','j','s']

		if a[:4] == "meng" and a[5] in meng:
			return 1
		elif a[:2] == "me" and a[3] in me:
			return 1
		elif a[:3] == "men" and a[4] in men:
			return 1
		elif a[:3] == "mem" and a[4] in mem:
			return 1
		elif a[:4] == "meny" and a[5] in meny:
			return 1
		elif a[:2] == "di" and len(a) > 2 and a != stemmer.stem(a):
			return 1
		else:
			return 0

# m = Verba_finder()
# m.main()