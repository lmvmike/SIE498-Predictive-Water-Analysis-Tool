# <<<<<<< HEAD
# cropType = ["lettuce", "broccoli", "cantaloupe", "cabbage", "dates"]
# cropPhase = ["seed", "sprout", "adolescence", "adult"]
# soilType = ["sandy", "peaty", "silty", "chalky", "clay", "loamy"]


# #croptype
# cropType = input("Enter the crop type: ")
# if (cropType == "lettuce"):
#         croptypeWeight = 1
# elif (cropType == "broccoli"):
#     croptypeWeight = 4/5
# elif (cropType == "cantoloupe"):
#         croptypeWeight = 3/5
# elif (cropType == "cabbage"):
#         croptypeWeight = 2/5
# elif (cropType == "dates"):
#         croptypeWeight = 1/5
# else:
#     print('Invalid crop type. Try again')
    

# #print ('Crop Weight = ', croptypeWeight)

# cropPhase = input("Enter the crop phase: ")
# if (cropPhase == 'seed'):
#     cropphaseWeight = 1
# elif (cropPhase == "sprout"):
#     cropphaseWeight = 3/4
# elif (cropPhase == "adolescence"):
#     cropphaseWeight = 2/4
# elif (cropPhase == "adult"):
#     cropphaseWeight = 1/4

# #print ('Phase Weight = ', cropphaseWeight)

# soilType = input("Enter the soil type: ")
# if (soilType == "sandy"):
#     soilTypeWeight = 1
# elif (soilType == "peaty"):
#     soilTypeWeight = 5/6
# elif (soilType == "silty"):
#     soilTypeWeight = 4/6
# elif (soilType == "chalky"):
#     soilTypeWeight = 3/6
# elif (soilType == "clay"):
#     soilTypeWeight = 2/6 
# elif (soilType == "loamy"):
#     soilTypeWeight = 1/6
# #     # print('Soil Weight = ',soilTypeWeight)

# acres = float(input("Enter the acres to be watered: "))
# # print(' Acres watered: ', acres)

# forecastTempHigh = float(input("Enter the high temp for the day: "))
# # print('forecastTempHigh: ', forecastTempHigh)

# forecastTempLow = float(input("Enter the low temp for the day: "))
# # print('forecastTempLow: ', forecastTempLow)

# averageTemp = (forecastTempHigh + forecastTempLow) / 2
# if (averageTemp > 90):
#     averageTempWeight = 1
# elif (averageTemp > 70):
#     averageTempWeight = 3/4
# elif (averageTemp > 0):
#     averageTempWeight = 1/2
# # print('Average Temp: ', averageTemp)

# forecastWindSpeed = float(input("Enter the average wind speed for the day: "))
# if (forecastWindSpeed > 20):
#     windSpeedWeight = 1
# elif (forecastWindSpeed > 10):
#     windSpeedWeight = 3/4
# elif (forecastWindSpeed > 0
# ):
#     windSpeedWeight = 1/2
# # print('Average Wind Speed: ', forecastWindSpeed)

# forecastHumidity = float(input("Enter the average humidity for the day: "))
# if (forecastHumidity > 50):
#     humidityWeight = 1/4
# elif(forecastHumidity > 25):
#     humidityWeight = 1/2
# elif (forecastHumidity > 10):
#     humidityWeight = 3/4
# elif (forecastHumidity > 0):
#     humidityWeight = 1
# # print('Average Humidity: ', forecastHumidity)


# waterOrdered = float(input("Enter the water needed: "))
# # print('Water ordered: ', waterOrdered)

# cfsNeeded = ((croptypeWeight + cropphaseWeight + soilTypeWeight
# + averageTempWeight + humidityWeight + windSpeedWeight)) + waterOrdered

# print('You should order this much water: ', cfsNeeded, 'CFS')
# =======
# def calculateWaterNeeded(orderedWater, precipitation, temperature):
#     waterNeeded = orderedWater

#     if precipitation > 0:
#         waterNeeded -= precipitation
#         waterNeeded = max(0,waterNeeded)

#     temperatureAdjusted = temperatureCoefficient(temperature)
#     waterNeeded *= temperatureAdjusted

#     return waterNeeded

# def temperatureCoefficient(temperature):
#     if temperature <=50:
#         coefficient = 0.9
#     elif temperature <=60:
#         coefficient = 0.95
#     elif temperature <=70:
#         coefficient = 1.0
#     elif temperature <=80:
#         coefficient = 1.05
#     elif temperature <=90:
#         coefficient = 1.1
#     elif temperature <= 100:
#         coefficient = 1.15
#     else:
#         coefficient = 1.2

#     return coefficient


# # cropType = ["lettuce", "broccoli", "cantaloupe", "cabbage", "dates"]
# # cropPhase = ["seed", "sprout", "adolescence", "adult"]
# # soiltype = ["sandy", "peaty", "silty", "chalky", "clay", "loamy"]
# # averageTempWeight = 1
# # humidityWeight = 2/3
# # windSpeedWeight = 1/3


# # #croptype
# # cropType = input("Enter the crop type: ")
# # if (cropType[0]):
# #     croptypeWeight = 1
# # elif (cropType[1]):
# #     croptypeWeight = 4/5
# # elif (cropType[2]):
# #     croptypeWeight = 3/5
# # elif (cropType[3]):
# #     croptypeWeight = 2/5
# # elif (cropType[4]):
# #     croptypeWeight = 1/5   

# # print ('Crop Weight = ', croptypeWeight)

# # cropPhase = input("Enter the crop phase: ")
# # if (cropPhase[0]):
# #     cropphaseWeight = 1
# # elif (cropPhase[1]):
# #     cropphaseWeight = 3/4
# # elif (cropPhase[2]):
# #     cropphaseWeight = 2/4
# # elif (cropPhase[3]):
# #     cropphaseWeight = 1/4
# #     print ('Phase Weight = ', cropphaseWeight)

# # soilType = input("Enter the soil type: ")
# # if (soilType[0]):
# #     soilTypeWeight = 1
# # elif (soilType[1]):
# #     soilTypeWeight = 5/6
# # elif (soilType[2]):
# #     soilTypeWeight = 4/6
# # elif (soilType[3]):
# #     soilTypeWeight = 3/6
# # elif (soilType[4]):
# #     soilTypeWeight = 2/6 
# # elif (soilType[5]):
# #     soilTypeWeight = 1/6

# # acres = int(input("Enter the acres to be watered: "))
# # print(' Acres watered: ', acres)

# temperature = int(input("Enter the temperature for the day: "))
# print('Temperature: ', temperature)

# precipitation = int(input("Enter the precipitation: "))
# print('Precipitation: ', precipitation)

# orderedWater = int(input("Enter the water needed: "))
# print('Water ordered: ', orderedWater)

# calculateWaterNeeded(orderedWater, precipitation, temperature)
# temperatureCoefficient(temperature)

# print('Order this much CFS: ', orderedWater)

# >>>>>>> 0ac3d6c (Added Machine Learning)
