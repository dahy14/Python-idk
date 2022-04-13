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

locations = [['seoul', 37.5, 126.9], ['shanghai', 30.6, 114.4], ['taipei', 25.0, 121.5], ['manila', 14.5, 121.0], ['tokyo', 35.68, 139.69], ['venice', 45.4, 12.3], ['sardinia', 36.8, 10.5], ['clark', 40.7128, -74.0059], ['melbourne', -37.8136, 144.9631], ['texas', 31.9686, -99.9018], ['london', 51.5074, -0.1278], ['new york', 40.7128, -74.0059], ['paris', 48.8566, 2.3522], ['berlin', 52.5200, 13.4050], ['dubai', 25.2048, 55.2708], ['sydney', -33.8688, 151.2093], ['cape town', -33.9249, 18.4241], ['dublin', 53.3498, -6.2603], ['cairo', 30.0444, 31.2357], ['rome', 41.9028, 12.4964], ['new delhi', 28.7041, 77.1025], ['moscow', 55.7558, 37.6173], ['johannesburg', -26.2041, 28.0473], ['istanbul', 41.0186, 28.9647], ['lhasa', 29.6575, 90.2088], ['dushanbe', 38.5737, 68.7738], ['tashkent', 41.3193, 69.2988], ['tehran', 35.6892, 51.3890], ['baghdad', 33.3386, 44.3922], ['kabul', 34.5155, 69.1957], ['karachi', 24.8615, 67.0099], ['mumbai', 19.0760, 72.8777], ['kathmandu', 27.7172, 85.3240], ['kolkata', 22.5726, 88.3639], ['chennai', 13.0827, 80.2707], ['bangkok', 13.7563, 100.5018], ['jakarta', -6.1751, 106.8296], ['hanoi', 21.0341, 105.8372], ['ho chi minh city', 10.8142, 106.6297], ['osaka', 34.6937, 135.5022]]

latitude,longitude = tokyo[0], tokyo[1]

#Folium Map
my_map = Map(latitude = latitude, longitude = longitude)

for loc in locations:
    #Geopoint Instance
    geolocation = Geopoint(latitude = loc[1], longitude = loc[2])
    forecast = geolocation.get_weather()
    #Create Popup instances for markers
    popup_content = f"""
    <h6 style="text-align:center;">{loc[0].title()}</h6>
    
    {forecast[0][0][-8:-6]}h: {round(forecast[0][1])}°F <img src="http://openweathermap.org/img/wn/{forecast[0][-1]}@2x.png" width=35> 
    <hr style="margin:1px;"> 
    {forecast[1][0][-8:-6]}h: {round(forecast[1][1])}°F <img src="http://openweathermap.org/img/wn/{forecast[1][-1]}@2x.png" width=35> 
    <hr style="margin:1px;">
    {forecast[2][0][-8:-6]}h: {round(forecast[2][1])}°F <img src="http://openweathermap.org/img/wn/{forecast[2][-1]}@2x.png" width=35> 
    <hr style="margin:1px;">
    {forecast[3][0][-8:-6]}h: {round(forecast[3][1])}°F <img src="http://openweathermap.org/img/wn/{forecast[3][-1]}@2x.png" width=35> 
    <hr style="margin:1px;">
    """
    popup = Popup(popup_content, max_width=400)
    popup.add_to(geolocation)
    geolocation.add_to(my_map)

#Save the Map
my_map.save('antipode.html')
