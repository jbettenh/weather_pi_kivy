import kivy
kivy.require("1.9.2")
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()

    def search_location(self):
        print(kivy.__version__)


class WeatherApp(App):
    pass


if __name__ == '__main__':
    WeatherApp().run()