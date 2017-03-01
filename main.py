from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest
import ConfigParser
import json
#kivy.require("1.9.2")


class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()
    search_results = ObjectProperty()

    def search_location(self):
        config = ConfigParser.SafeConfigParser()
        config.read('config.ini')
        my_api_key = config.get('my_weather_id', 'weather_api_key')
       # print my_api_key
        search_template = "http://api.openweathermap.org/data/2.5/forecast/daily?APPID=" + my_api_key + "&q={}"
        print search_template
        search_url = search_template.format(self.search_input.text)
        request = UrlRequest(search_url, self.found_location)

    def found_location(self, request, data):
        data = json.loads(data.decode()) if not isinstance(data, dict) else data
        cities = ["{} ({})".format(data["city"]["name"], data["city"]["country"])]
        self.search_results.item_strings = cities

class WeatherApp(App):
    pass

if __name__ == '__main__':
    WeatherApp().run()
