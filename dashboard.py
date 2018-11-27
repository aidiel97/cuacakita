from tkinter import *
import sys
import os
import tkinter.font as tkFont

from text_generator import Text_generator

class mengubahJudul(Frame):
	def __init__(self, parent):
		Frame.__init__(self,parent)
		
		self.tampilan =  parent
		# self.aturSplash()
		self.aturWindow()
		self.initUI()


	def aturWindow(self):
		lebar = 960
		tinggi = 540

		# ************************* penggunaan fungsi winfo_screenwidth()
		setTengahX = (self.tampilan.winfo_screenwidth()-lebar)//2
        # ************************* penggunaan fungsi winfo_screenheight()
		setTengahY = (self.tampilan.winfo_screenheight()-tinggi)//2

		self.tampilan.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY))

	def initUI(self):
		self.tampilan.title("Forecast Generator")
		self.pack(fill=BOTH, expand=1)

	def generator(self):
		tg = Text_generator()
		sample_array = tg.getData()
	
		cuaca = StringVar()
		cuaca.set(sample_array[0]['cuaca'])

		label_kota.config(text=kelembaban.get())

		teks.config(text="")
		teks.config(text=result.get())

		print("Update label : ",result.get())	

if __name__=='__main__':
	root = Tk()
	app = mengubahJudul(root)
	tg = Text_generator()
	sample_array = tg.getData()

	app.customFont = tkFont.Font(family="Varela Round", size=24)
	app.customFont2 = tkFont.Font(family="Varela Round", size=14)
	app.customFont3 = tkFont.Font(family="Varela Round", size=8, weight="bold")

	bg_image = PhotoImage(file="wallpaper\\morning-normal.png")
	bg_label = Label(root, image=bg_image).place(x=0, y=0, relwidth=1, relheight=1)

	kota = StringVar()
	kota.set(sample_array[0]['kota'][1:])
	label_kota = Label(root, text=kota.get(), font=app.customFont ,fg="#413e3b", bg="#fff1e8")
	label_kota.place(x=30.5, y=16)

	v_kelembaban = str(sample_array[0]['kelembapan']) + "% (" + sample_array[0]['k_kelembapan'] + ")"
	kelembaban = StringVar()
	kelembaban.set(v_kelembaban)
	label_kelembaban = Label(root, text=kelembaban.get(), font=app.customFont2 ,fg="#413e3b", bg="#fff1e8")
	label_kelembaban.place(x=80, y=78)
	Label(root, text="Kelembaban", font=app.customFont3 ,fg="#413e3b", bg="#fff1e8").place(x=80, y=65)

	v_angin = sample_array[0]['kec_angin'] +" "+ sample_array[0]['a_angin']
	angin = StringVar()
	angin.set(v_angin)
	label_angin = Label(root, text=angin.get(), font=app.customFont2 ,fg="#413e3b", bg="#fff1e8")
	label_angin.place(x=80, y=125)
	Label(root, text="Tiupan Angin", font=app.customFont3 ,fg="#413e3b", bg="#fff1e8").place(x=80, y=112)

	v_suhu = str(sample_array[0]['suhu']) + "°C (" + sample_array[0]['k_suhu'] +")"
	suhu = StringVar()
	suhu.set(v_suhu)
	label_suhu = Label(root, text=suhu.get(), font=app.customFont2 ,fg="#413e3b", bg="#fff1e8")
	label_suhu.place(x=80, y=170)
	Label(root, text="Suhu Udara", font=app.customFont3 ,fg="#413e3b", bg="#fff1e8").place(x=80, y=157)

	waktu = StringVar()
	waktu.set(sample_array[0]['waktu'])
	label_waktu = Label(root, text=waktu.get(), font=app.customFont2 ,fg="#413e3b", bg="#fff1e8")
	label_waktu.place(x=880, y=16)

	tgl = StringVar()
	tgl.set(sample_array[0]['tgl'])
	label_waktu = Label(root, text=tgl.get(), font=app.customFont3 ,fg="#413e3b", bg="#fff1e8")
	label_waktu.pack()

	sentence = tg.generator(sample_array)
	result = StringVar()
	result.set(sentence)
	label_result = Text(height=100, width=700, font=app.customFont2 ,fg="#fff1e8", bg="#2d112a", borderwidth=0)
	label_result.place(x=20, y=460, width=700)
	label_result.insert(END, result.get())
	Label(root, text="Kalimat Hasil Pembangkitan", font=app.customFont3 ,fg="#fff1e8", bg="#2d112a").place(x=20, y=440)

	generate_image = PhotoImage(file="wallpaper\\generate_button.png")
	Button(root, text="Generate Text", image=generate_image, fg="black", borderwidth=0, command=app.generator).place(x=762.3, y=428, height=43, width=170)

	tweet_image = PhotoImage(file="wallpaper\\tweet_button.png")
	Button(root, text="Generate Text", image=tweet_image, fg="black", borderwidth=0, command=app.generator).place(x=762.3, y=482, height=43, width=170)


	# Label(root, text="Text Generator", fg="#0984e3", font=app.customFont).pack(fill=X, padx=10)
	# teks = Label(root)
	# teks.pack()
	# Button(root, text="Exit", bg="#e17055", fg="white", borderwidth=0, command=root.quit).pack(fill=X, padx=10, pady=2)
	root.mainloop()


# #koordinat :
# kota = 30.5 , 26
# kelembaban = 80, 76
# angin = 80, 120
# suhu = 80, 167
# tbl puti = 762.3, 428.6
# tbl biru = 762.3, 482.2
# generate = 80, 430
