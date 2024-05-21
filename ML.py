# %%
import numpy as np
import pandas as pd
from sklearn import preprocessing, svm

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

def calculate_temp(temperature, humidity, light_intensity, hour, delta_type):
    data = pd.read_csv(f"hour{hour}.txt", delimiter=",", low_memory=False)
    x = np.array(data[["Humid", "Light Intensity", "Temperature"]])
    y = np.array(data[[delta_type]])
 
    model = LinearRegression().fit(x,y)

    r_sq = model.score(x, y)

    arr = np.array([[humidity, light_intensity, temperature]], dtype=object)

    delta = model.predict(arr)
    delta = delta[0][0]   
    

    if delta_type == "T_Delta":
        temperature = temperature + delta
        return temperature
    elif delta_type == "H_Delta":
        humidity = humidity + delta
        return humidity
    else:
        light_intensity = light_intensity + delta
        return light_intensity

# %%
hours = []
hour = 2
#Input goes here
input_temperature = 16
light_intensity = 760
time = 13
wanted_hour = 17
input_humidity = 50
input_l = light_intensity
input_hour = (time - 12) + hour
utcOffset = 10
temp = []
humid = []
light = []

for i in range(6):
    if input_hour != hour:
        temperature = calculate_temp(input_temperature, input_humidity, input_l, hour, "T_Delta")
        humidity = calculate_temp(input_temperature, input_humidity, input_l, hour, "H_Delta")
        light_intensity = calculate_temp(input_temperature, input_humidity, input_l, hour, "L_Delta")
    else:
        temperature = input_temperature
        humidity = input_humidity 
        light_intensity = input_l

    temp.append(temperature)
    humid.append(humidity)
    light.append(light_intensity)
    if (hour > 24): hour -= 24
    
    hour_str = str(hour+utcOffset) if hour+utcOffset < 24 else str(hour + utcOffset - 24)
    hours.append(hour_str)
    hour += 1

# print(hours)
j = 0
final_hour = wanted_hour - 12
final_temp = temp[final_hour]
print(temp)
print(light)
print(humid)

# %%
