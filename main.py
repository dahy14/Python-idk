from folium import Map, Marker, Popup
from geo import Geopoint
from timezonefinder import TimezoneFinder

#Folium
tokyo = [35.68, 139.69]

clark = [40.7128, -74.0059]
sardinia = [36.8, 10.5]
venice = [45.4, 12.3]
seoul = [37.5, 126.9]
shen_zen = [30.6, 114.4]
taipei = [25.0, 121.5]
manila = [14.5, 121.0]

locations = [['seoul', 37.5, 126.9], ['shanghai', 30.6, 114.4], ['taipei', 25.0, 121.5], ['manila', 14.5, 121.0], ['tokyo', 35.68, 139.69], ['venice', 45.4, 12.3], ['sardinia', 36.8, 10.5], ['clark', 40.7128, -74.0059], ['melbourne', -37.8136, 144.9631], ['texas', 31.9686, -99.9018]]

latitude,longitude = tokyo[0], tokyo[1]

#Folium Map
my_map = Map(latitude = latitude, longitude = longitude)

for loc in locations:
    #Geopoint Instance
    geolocation = Geopoint(latitude = loc[1], longitude = loc[2])
    forecast = geolocation.get_weather()
    #Create Popup instances for markers
    popup_content = f"""
     
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


