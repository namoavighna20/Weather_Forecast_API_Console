import requests
import os
from datetime import datetime

user_api=os.environ['Weather_api']
location=input("Enter the city name:")
#posted from website:         api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
location_link= "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api

api_link=requests.get(location_link)
api_data=api_link.json()
#print(api_data)

if api_data['cod']=='404':
    print("Invalid City: {}, Please check your city name".format(location))
else:
    temp_city=((api_data['main']['temp'])-273.15)
    weather_desc=api_data['weather'][0]['description']
    hmdt=api_data['main']['humidity']
    wind_spd=api_data['wind']['speed']
    date_time=datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    print("----------------------------------------------------------------------------")
    print("Weather Stats for-{} || {}".format(location.upper(),date_time))
    print("---------------------------------------------------------------------------------")

    print("Current temperature is: {:.2f} deg C".format(temp_city))
    print("Current Weather desc :",weather_desc)
    print("Current humidity        :",hmdt,'%')
    print("Current wind speed     :",wind_spd,'kmph')

#REQ_DATE=input("Enter the date to get status(Date Format:DD-MM-YYYY)=>")
