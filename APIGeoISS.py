import requests
import json
import geopy.distance





def main():
    coords_User = locateUser()
    geoResponse = locateISS()
    distance = geopy.distance.geodesic(geoResponse[0], coords_User).mi
    print(f"The ISS is above {geoResponse[1]} and {distance:.0f} miles from your location")
    if (geoResponse[2] == False):
        funFact(geoResponse[1])
        


# locate user from City, State and return cooridinates
def locateUser():
    userCity = input("Enter your City: ")
    userState = input("Enter your State: ")
    userLocationRequest = requests.get(f"https://nominatim.openstreetmap.org/search?format=json&q={userCity},{userState}")
    return [(userLocationRequest.json()[0]["lat"]),(userLocationRequest.json()[0]["lon"])]


# locate ISS and return: cooridinates, country it is above, and if it is over ocean
def locateISS():
    issResponse = requests.get("http://api.open-notify.org/iss-now.json")
    latitude = float((issResponse.json()["iss_position"]["latitude"]))
    longitude = float((issResponse.json()["iss_position"]["longitude"]))
    coordsISS = (latitude, longitude)
    
    formattedSearchGeo = requests.get(f"https://nominatim.openstreetmap.org/reverse?format=json&lat={latitude}&lon={longitude}&zoom=18&addressdetails=1")

    isOcean= False
    try:
        issLocation = (formattedSearchGeo.json()["address"]["country"])
        
    except:
        issLocation = "the ocean"
        isOcean= True


    return([coordsISS, issLocation, isOcean])


# provide fun fact based on ISS location
def funFact(country):
    #provide fun fact about country that ISS is over
    pass

# provides photo of country as seen from ISS
def photoGenerator():
    pass


main()

