#Play this first source env/bin/activate

from datetime import datetime
import time
import board
import datetime
import adafruit_dht
import adafruit_bh1750
import pyrebase
import random

config = {
	"apiKey": "AIzaSyClrDU_Jg7LpYZl4V0rQji5Q0-aHXEEyqg",
	"authDomain":"project-test1-f190d.firebaseapp.com",
	"databaseURL": "https://project-test1-f190d-default-rtdb.firebaseio.com",
	"storageBucket": "project-test1-f190d.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()


dhtDevice = adafruit_dht.DHT11(board.D18)
i2c = board.I2C() 
sensor = adafruit_bh1750.BH1750(i2c)
sensor = adafruit_bh1750.BH1750(i2c)

while True:
        time.sleep(5)
        t = datetime.datetime.now()
        ti = t.min
        if t.hour >= 12:
                break

while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        intensity = sensor.lux
        c_time = datetime.datetime.now()
        date = c_time.timestamp()
        print(c_time)
        
        
        print(
            "Temp: {:.1f} C    Humidity: {}% ".format(
                temperature_c, humidity
            )
        )
        
        print("%.2f Lux" % intensity)
        
        data = {
        "Temperature" : temperature_c,
        "Humidity" : humidity,
        "Light Intensity" : intensity,
        "Date" : date
        }
        
        db.child("More Data Points").push(data)
        print("Sent to firebase")
        
        
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    if t.hour >= 17:
            break
    time.sleep(599)
    
print("Done")
