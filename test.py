import requests
import json

latitude = input("Enter the latitude: ")
longitude = input("Enter the longitude: ")
apiKey = "5qDm2kKQz8NLEjuQXQnl5AlN0BeNB4eQ"
response = requests.get("https://api.tomorrow.io/v4/weather/forecast?location=" + latitude + "," + longitude + "&apikey=" + apiKey)
if(response.status_code == 200):
    json_object = json.dumps(response.json(), indent=2)
    with open("data.json", "w") as outfile:
        outfile.write(json_object)
    temp = open('data.json')
    data = json.load(temp)
    time = data['timelines']['minutely'][0]
    minute = time['values']
    celsius = minute["temperature"]
    fahrenheit = (celsius * 9/5) + 32
    print("Temperature in fahrenheit: " + str(fahrenheit))
    print("Temperature in Celsius: " + str(celsius))
    temp.close()
else:
    print("Not a real place")
