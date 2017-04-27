from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
miles_to_km = 1.60934
class MilesToKilometres(App):
    def build(self):
        Window.size = (500, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('FromScratch.kv')
        return self.root

    def handle_increment(self, change):
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)

    def handle_calculate(self):
        value = self.get_validated_miles()
        result = value * miles_to_km
        self.root.ids.output_label.text = str(result)

    def get_validated_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

MilesToKilometres().run()