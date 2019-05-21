# quotes = []
# filepath = 'quotes.txt'  
# with open(filepath, encoding="utf8") as fp:  
#    line = fp.readline()
#    cnt = 1
#    while line:
#    	# if "galau" in line :
#    		# print("Line {}: {}".format(cnt, line.strip()))
#    		quotes.append(format(line.strip()))
#    		line = fp.readline()
#    		cnt += 1
   		
# for qt in quotes:
# 	if "galau" in qt:
# 		print(qt)

qt = open("quotes.txt", "r", encoding="utf8")
qt_call = qt.read()
qt_corps = qt_call.split()
qt.close()

if "galau" in qt_corps:
	print("ya")
else:
	print("tidak")



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

elif ans == "quotes":
        	qt = translate.quotes(city)
        	api.update_status('Hai! @' + mention.user.screen_name + "\n"+ qt, mention.id)