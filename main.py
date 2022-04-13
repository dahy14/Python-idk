from folium import Map
from geo import Geopoint

latitude = 40.69
longitude = 69.69

antipode_latitude = latitude * -1

if longitude <= 0:
    antipode_longigtude = longitude + 180
else :
    antipode_longitude = longitude - 180

location = [antipode_latitude, antipode_longitude]
my_map = Map(location)
# my_map.save('antipode.html')

my_point = Geopoint(latitude, longitude)
print(my_point.closest_parallel())

print ("Antipode Latitude: " + str(antipode_latitude))
print ("Antipode Longitude: " + str(antipode_longitude))


# You have stolen my heart oh yeah