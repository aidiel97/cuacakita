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