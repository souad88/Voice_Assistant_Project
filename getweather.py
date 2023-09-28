#generate API from https://home.openweathermap.org/api_keys
import requests
def current_weather(city_name):

    API_KEY="c3fc1f5998761ff20628392b7ee3003a"
    #city_name = input("Enter city name : ")
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"
    # Making a get request to the API
    response = requests.get(weather_url)
    #json response
    res = response.json()
    if res["cod"] != "404":
         data = res["main"]
         current_temperature = data["temp"]
         current_pressure = data["pressure"]
         desc = res["weather"]
         # weather description
         weather_description = desc[0]["description"]
         #print(" Temperature " +str(round(current_temperature-273.15)) +" celsius ")
         #print("Pressure: " + str(current_pressure))
         #print("Description: " + str(weather_description))
    return str(round(current_temperature-273.15)),str(weather_description),str(current_pressure) 
#current_weather('cairo')