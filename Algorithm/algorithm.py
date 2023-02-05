cropType = ["lettuce", "broccoli", "cantaloupe", "cabbage", "dates"]
cropPhase = ["seed", "sprout", "adolescence", "adult"]
soiltype = ["sandy", "peaty", "silty", "chalky", "clay", "loamy"]
averageTempWeight = 1
humidityWeight = 2/3
windSpeedWeight = 1/3


#croptype
cropType = input("Enter the crop type: ")
if (cropType[0]):
    croptypeWeight = 1
elif (cropType[1]):
    croptypeWeight = 4/5
elif (cropType[2]):
    croptypeWeight = 3/5
elif (cropType[3]):
    croptypeWeight = 2/5
elif (cropType[4]):
    croptypeWeight = 1/5   

print ('Crop Weight = ', croptypeWeight)

cropPhase = input("Enter the crop phase: ")
if (cropPhase[0]):
    cropphaseWeight = 1
elif (cropPhase[1]):
    cropphaseWeight = 3/4
elif (cropPhase[2]):
    cropphaseWeight = 2/4
elif (cropPhase[3]):
    cropphaseWeight = 1/4
    print ('Phase Weight = ', cropphaseWeight)

soilType = input("Enter the soil type: ")
if (soilType[0]):
    soilTypeWeight = 1
elif (soilType[1]):
    soilTypeWeight = 5/6
elif (soilType[2]):
    soilTypeWeight = 4/6
elif (soilType[3]):
    soilTypeWeight = 3/6
elif (soilType[4]):
    soilTypeWeight = 2/6 
elif (soilType[5]):
    soilTypeWeight = 1/6

acres = float(input("Enter the acres to be watered: "))
print(' Acres watered: ', acres)

forecastTempHigh = float(input("Enter the high temp for the day: "))
print('forecastTempHigh: ', forecastTempHigh)

forecastTempLow = float(input("Enter the low temp for the day: "))
print('forecastTempLow: ', forecastTempLow)

averageTemp = (forecastTempHigh + forecastTempLow) / 2
print('Average Temp: ', averageTemp)

forecastWindSpeed = float(input("Enter the average wind speed for the day: "))
print('Average Wind Speed: ', forecastWindSpeed)

forecastHumidity = float(input("Enter the average humidity for the day: "))
print('Average Humidity: ', forecastHumidity)

waterOrdered = float(input("Enter the water needed: "))
print('Water ordered: ', waterOrdered)

cfsNeeded = (((croptypeWeight + cropphaseWeight + soilTypeWeight) * acres)
+ (averageTemp*averageTempWeight) 
+ (forecastHumidity * humidityWeight)
+ (forecastWindSpeed * windSpeedWeight))
+ waterOrdered

print('Order this much CFS: ', cfsNeeded)