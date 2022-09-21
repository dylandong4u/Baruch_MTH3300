#******************************************************************************
# weler.py
#******************************************************************************
# Name: Kun Dong
#******************************************************************************
# Remarks (optional):
# Used math.radians() to convert degrees to radians...
# The print results are the challenge problem 
# The logic of selecting stations bothered me a lot... I wonder if professor you could kindly provide an example code later?

import math

# head office latitude and longtitude
hlat = 40.740230
hlong = -73.983766


# Input numbers for station 1 and station 2 and their bike number
station_lat_1 = float(input("Enter latitude of station 1: "))
station_long_1 = float(input("Enter longtitude of station 1: "))
bikes_1 = int(input("Bikes at station 1: "))

station_lat_2 = float(input("Enter latitude of station 2: "))
station_long_2 = float(input("Enter longtitude of station 2: "))
bikes_2 = int(input("Bikes at station 2: "))


# Calculate difference between head office and stations
delta_lat_1 = (station_lat_1 - hlat)
delta_long_1 = (station_long_1 - hlong)

delta_lat_2 = (station_lat_2 - hlat)
delta_long_2 = (station_long_2 - hlong)


# FLat Earth: convert degrees to kilometers
delta_x_1 = delta_lat_1 * 111.048       # kilometer difference between latitudes station 1
delta_y_1 = delta_long_1 * 84.515       # kilometer difference between longtitudes station 1 

delta_x_2 = delta_lat_2 * 111.048       # kilometer difference between latitudes station 2
delta_y_2 = delta_long_2 * 84.515       # kilometer difference between longtitudes station 2

'''
# Flat distance between the locations
distance_1 = math.sqrt((delta_x_1 ** 2) + (delta_y_1 ** 2))
distance_2 = math.sqrt((delta_x_2 ** 2) + (delta_y_2 ** 2))
'''

# Apprximation for the Earth radius 6371 km
R = 6371

# Convert degrees to radians to use in math.sin()/cos() functions in the formula below
delta_lat_1_rad = math.radians(delta_lat_1)
delta_lat_2_rad = math.radians(delta_lat_2)

delta_long_1_rad = math.radians(delta_long_1)
delta_long_2_rad = math.radians(delta_long_2)

hlat_rad = math.radians(hlat)

station_lat_1_rad = math.radians(station_lat_1)
station_lat_2_rad = math.radians(station_lat_2)


# Geo distance between the locations
# Used haversine distance formula to find the distance
geo_distance_1 = 2 * R * math.asin(math.sqrt( ( (math.sin( delta_lat_1_rad / 2) ) ** 2) + (math.cos(hlat_rad) * math.cos(station_lat_1_rad) * ( (math.sin( delta_long_1_rad /2 ) ) ** 2) ) ) )
geo_distance_2 = 2 * R * math.asin(math.sqrt( ( (math.sin( delta_lat_2_rad / 2) ) ** 2) + (math.cos(hlat_rad) * math.cos(station_lat_2_rad) * ( (math.sin( delta_long_2_rad /2 ) ) ** 2) ) ) )


'''
#print('*********FLAT DISTANCE***********')
print(f'Distance to station 1 = {distance_1}')
print(f'Distance to station 2 = {distance_2}')
'''

#print('*********GEOMETRY DISTANCE*********')
print(f'Distance to station 1 = {geo_distance_1}')
print(f'Distance to station 2 = {geo_distance_2}')


# Selection for stations
if (geo_distance_1 > 0 and geo_distance_1 <= 3) and (geo_distance_2 > 0 and geo_distance_2 <= 3) and (bikes_1 != 0 and bikes_2 != 0): # when both in range and have bikes
    
    if geo_distance_1 > geo_distance_2: # compare distance and print the closer one
        print("Station 2")
    elif geo_distance_1 < geo_distance_2: # compare distance and print the closer one
        print("Station 1")

elif (geo_distance_1 > 3 and geo_distance_2 > 3) or (bikes_1 == 0 and bikes_2 == 0): # when neither A and B is in range nor has bikes
    print("Neither")

elif geo_distance_1 > 3 and bikes_2 == 0: # when A not in range, and B not have bikes
    print("Neither")

elif geo_distance_2 > 3 and bikes_1 == 0: # when B not in range, and A not have bikes
    print("Neither")

elif (geo_distance_1 > 0 and geo_distance_1 <= 3) and bikes_1 != 0: # when only A in range and has bikes
    print("Station 1")

elif (geo_distance_2 > 0 and geo_distance_2 <= 3) and bikes_2 != 0: # when only B in range and has bikes
    print("Station 2")
