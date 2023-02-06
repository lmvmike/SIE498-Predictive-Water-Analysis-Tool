cropType = ["lettuce", "broccoli", "cantaloupe", "cabbage", "dates"]
cropPhase = ["seed", "sprout", "adolescence", "adult"]
soilType = ["sandy", "peaty", "silty", "chalky", "clay", "loamy"]


#croptype
cropType = input("Enter the crop type: ")
if (cropType == "lettuce"):
        croptypeWeight = 1
elif (cropType == "broccoli"):
    croptypeWeight = 4/5
elif (cropType == "cantoloupe"):
        croptypeWeight = 3/5
elif (cropType == "cabbage"):
        croptypeWeight = 2/5
elif (cropType == "dates"):
        croptypeWeight = 1/5
else:
    print('Invalid crop type. Try again')
    

#print ('Crop Weight = ', croptypeWeight)

cropPhase = input("Enter the crop phase: ")
if (cropPhase == 'seed'):
    cropphaseWeight = 1
elif (cropPhase == "sprout"):
    cropphaseWeight = 3/4
elif (cropPhase == "adolescence"):
    cropphaseWeight = 2/4
elif (cropPhase == "adult"):
    cropphaseWeight = 1/4

#print ('Phase Weight = ', cropphaseWeight)

soilType = input("Enter the soil type: ")
if (soilType == "sandy"):
    soilTypeWeight = 1
elif (soilType == "peaty"):
    soilTypeWeight = 5/6
elif (soilType == "silty"):
    soilTypeWeight = 4/6
elif (soilType == "chalky"):
    soilTypeWeight = 3/6
elif (soilType == "clay"):
    soilTypeWeight = 2/6 
elif (soilType == "loamy"):
    soilTypeWeight = 1/6
#     # print('Soil Weight = ',soilTypeWeight)

acres = float(input("Enter the acres to be watered: "))
# print(' Acres watered: ', acres)

forecastTempHigh = float(input("Enter the high temp for the day: "))
# print('forecastTempHigh: ', forecastTempHigh)

forecastTempLow = float(input("Enter the low temp for the day: "))
# print('forecastTempLow: ', forecastTempLow)

averageTemp = (forecastTempHigh + forecastTempLow) / 2
if (averageTemp > 90):
    averageTempWeight = 1
elif (averageTemp > 70):
    averageTempWeight = 3/4
elif (averageTemp > 0):
    averageTempWeight = 1/2
# print('Average Temp: ', averageTemp)

forecastWindSpeed = float(input("Enter the average wind speed for the day: "))
if (forecastWindSpeed > 20):
    windSpeedWeight = 1
elif (forecastWindSpeed > 10):
    windSpeedWeight = 3/4
elif (forecastWindSpeed > 0
):
    windSpeedWeight = 1/2
# print('Average Wind Speed: ', forecastWindSpeed)

forecastHumidity = float(input("Enter the average humidity for the day: "))
if (forecastHumidity > 50):
    humidityWeight = 1/4
elif(forecastHumidity > 25):
    humidityWeight = 1/2
elif (forecastHumidity > 10):
    humidityWeight = 3/4
elif (forecastHumidity > 0):
    humidityWeight = 1
# print('Average Humidity: ', forecastHumidity)


waterOrdered = float(input("Enter the water needed: "))
# print('Water ordered: ', waterOrdered)

cfsNeeded = ((croptypeWeight + cropphaseWeight + soilTypeWeight
+ averageTempWeight + humidityWeight + windSpeedWeight)) + waterOrdered

print('You should order this much water: ', cfsNeeded, 'CFS')