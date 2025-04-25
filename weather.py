import requests

class City:
    def __init__(self, city, lat, lon, unit = "metric"):
        self.city = city
        self.lat = lat
        self.lon = lon
        self.unit = unit
        self.get_data()

    def get_data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.unit}&lat={self.lat}&lon={self.lon}&appid=0ba5b307163ee5003e6f0ef64a89f8bc")
        except Exception:
            print("No internet access")

        response_json = response.json()
        self.temp = response_json["main"]["temp"]
        self.temp_max = response_json["main"]["temp_max"]
        self.temp_min = response_json["main"]["temp_min"]
    
    def print_data_celsius(self):
        print(f"In {self.city}, today is {self.temp}°C")
        print(f"Highest temperature is {self.temp_max}°C")
        print(f"Lowest temperature is {self.temp_min}°C\n")
    
    def print_data_fahrenheit(self):
        self.change_unit()
        print(f"In {self.city}, today is {self.temp_fahrenheitUnit:.2f}°F")
        print(f"Highest temperature is {self.temp_max_fahrenheitUnit:.2f}F")
        print(f"Lowest temperature is {self.temp_min_fahrenheitUnit:.2f}°F\n")

    def change_unit(self):
        self.temp_fahrenheitUnit = (self.temp * 9/5) + 32
        self.temp_max_fahrenheitUnit = (self.temp_max * 9/5) + 32
        self.temp_min_fahrenheitUnit = (self.temp_min * 9/5) + 32

myCity = City("Perth", -31.954800499999997, 115.85837364402198)
myCity.print_data_celsius()
myCity.print_data_fahrenheit()


    