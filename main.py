import theosCode
from flask import Flask, redirect
from time import sleep
import random

app = Flask(__name__)


@app.route('/')
def index():
  return "Welcome to the GeoLocator!"




@app.route('/navigate')
def navigate():
  lat = theosCode.runCode("lat")
  lon = theosCode.runCode("lon")

  url = f"https://www.google.com/maps?q={str(lat)},{str(lon)}"
	
  return redirect(url, code=302)






@app.route('/navigate/land')
def navigate_land():
	lat1 = round(random.uniform(15, 70), 4)
	lon1 = round(random.uniform(55, 165), 4)

	lat2 = round(random.uniform(36, 71), 4)
	lon2 = round(random.uniform(-10, 60), 4)
	
	if random.uniform(1,2) == 1:
		lat = lat1
		lon = lon1
	else:
		lat = lat2
		lon = lon2

	url = f"https://www.google.com/maps?q={str(lat)},{str(lon)}"

	return redirect(url, code=302)






if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=False)