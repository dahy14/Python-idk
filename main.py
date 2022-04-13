from folium import Map, Marker, Popup
from geo import Geopoint
from timezonefinder import TimezoneFinder

#Folium
tokyo = [35.68, 139.69]

clark = [40.7128, -74.0059]
sardinia = [36.8, 10.5]
venice = [45.4, 12.3]
seoul = [37.5, 126.9]

latitude,longitude = seoul[0], seoul[1]

#Folium Map
my_map = Map(latitude = latitude, longitude = longitude)

#Geopoint Instance
geolocation = Geopoint( latitude, longitude)

forecast = geolocation.get_weather()

popup_content = f"""
<h6>{TimezoneFinder().timezone_at(lat = latitude, lng = longitude)}</h6>
{forecast[0][0][-8:-6]}h: {round(forecast[0][1])}°F <img src="http://openweathermap.org/img/wn/{forecast[0][-1]}@2x.png" width=35> 
<hr style="margin:1px;"> 
{forecast[1][0][-8:-6]}h: {round(forecast[1][1])}°F <img src="http://openweathermap.org/img/wn/{forecast[1][-1]}@2x.png" width=35> 
<hr style="margin:1px;">
{forecast[2][0][-8:-6]}h: {round(forecast[2][1])}°F <img src="http://openweathermap.org/img/wn/{forecast[2][-1]}@2x.png" width=35> 
<hr style="margin:1px;">
{forecast[3][0][-8:-6]}h: {round(forecast[3][1])}°F <img src="http://openweathermap.org/img/wn/{forecast[3][-1]}@2x.png" width=35> 
"""

popup = Popup(popup_content, max_width=400)
popup.add_to(geolocation)
geolocation.add_to(my_map)

#Save the Map
my_map.save('antipode.html')


