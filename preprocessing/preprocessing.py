count = 0

for i in range(100):
	count = 0
	with open("AddisSimulationResult.xml") as f:
	    for num, line in enumerate(f, 1):
	        if '<vehicle id="'+ str(i) +'"' in line:
	        	count = count + 1
            

	print ("vehicle " + str(i) + ": reported its location information " + str(count) + " times")
