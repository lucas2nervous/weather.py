import requests


class City:
    def __init__(self, name, lat, lon, units="metric"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()

    def get_data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=bdd89be1e9a577cc820e7d408e0090b1")



        except:
            print("No internet connection")

        self.response_json = response.json()
        self.temp = self.response_json["main"]["temp"]
        self.temp_min = self.response_json["main"]["temp_min"]
        self.temp_max = self.response_json["main"]["temp_max"]

    def temp_print(self):
        print(f"In {self.name} it is currently {self.temp} degrees")
        print(f"today high is: {self.temp_max} degrees")
        print(f"today low is: {self.temp_min} degrees")

my_city = City("Tokyo",35.6764, 139.6500 )

my_city.temp_print()
print(my_city.response_json)

vacation_city = City("Singapore", 1.3521, 103.8198)
vacation_city.temp_print()
print(vacation_city.response_json)

current_city = City("Switzerland", 46.8182, 8.2275 )
current_city.temp_print()



