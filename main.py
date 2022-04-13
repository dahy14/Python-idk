from folium import Map, Marker, Popup
from geo import Geopoint

#Folium
latitude = 35.68
longitude = 139.69

#Folium Map
my_map = Map([latitude, longitude])


#Geopoint Instance
tokyo = Geopoint(latitude = latitude , longitude = longitude)
popup = Popup(str(tokyo.get_weather()))
popup.add_to(tokyo)
tokyo.add_to(my_map)

#Save the Map
my_map.save('antipode.html')


