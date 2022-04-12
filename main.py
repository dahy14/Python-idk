latitude = float("40.09")
longtitude = float("72.64")

antipode_latitude = latitude.__mul__(int("-1"))

if longtitude < 0:
    antipode_longigtude = longtitude.__add__(float("180"))
else :
    antipode_longigtude = longtitude.__sub__(float("180"))


print ("Latitude: " + str(latitude))
print ("Longtitude: " + str(longtitude))
print ("Antipode Latitude: " + str(antipode_latitude))
print ("Antipode Longtitude: " + str(antipode_longigtude))