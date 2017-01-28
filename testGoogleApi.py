import requests

url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=%D0%B3.%D0%BA%D0%B0%D0%B7%D0%B0%D0%BD%D1%8C,%20%D1%83%D0%BB%20%D0%B3%D0%B2%D0%B0%D1%80%D0%B4%D0%B5%D0%B9%D1%81%D0%BA%D0%B0%D1%8F%2036&destinations=%D0%BD%D0%B0%D0%B1%D0%B5%D1%80%D0%B6%D0%BD%D1%8B%D0%B5%20%D1%87%D0%B5%D0%BB%D0%BD%D1%8B&mode=walking&language=EN&key=AIzaSyBSJywKPIK1ONXOByLvjPHeqvNhIFd6Cu4"

response = requests.get(url)
json = response.json()
print(json['rows'][0]['elements'][0]['distance']['value'])

