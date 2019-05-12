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
	if "galau" in qt:
		print(qt)