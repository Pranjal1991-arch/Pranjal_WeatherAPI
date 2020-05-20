import requests

api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=93d0c9bdc1e5269399a4a5fccd9adf08&q='
city = input("Enter City Name :")
url = api_address + city
json_data = requests.get(url).json()
#formatted_data = json_data['weather'][0]['description']
print(json_data)
#print(formatted_data)
