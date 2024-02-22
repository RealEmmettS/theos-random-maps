import random

lat = 0
lon = 0

#randomInt = random.randint(1,10)



def runCode(q):
	lat = round(random.uniform(-90, 90), 4)
	lon = round(random.uniform(-180, 180), 4)


	if q=="lat":
		return lat
	elif q=="lon":
		return lon

