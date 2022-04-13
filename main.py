from folium import Map

latitude = 40.69
longtitude = 69.69

antipode_latitude = latitude * -1

if longtitude <= 0:
    antipode_longigtude = longtitude + 180
else :
    antipode_longigtude = longtitude - 180

location = [antipode_latitude, antipode_longigtude]
my_map = Map(location)
my_map.save('antipode.html')

print ("Antipode Latitude: " + antipode_latitude)
print ("Antipode Longtitude: " + antipode_longigtude)

print(my_map)

# You have stolen my heart oh yeah