from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty

CONVERSION_FACTOR = 1.60934


class ConvertMilesToKms(App):
    kilometers = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kms"
        self.root = Builder.load_file('convert_miles_to_kms.kv')
        return self.root

    def handle_increment(self, increment_value):
        input_value = self.check_input()
        result = input_value + increment_value
        self.root.ids.input_value.text = str(result)
        self.handle_calculation()

    def handle_calculation(self):
        input_value = self.check_input()
        self.kilometers = str(input_value * CONVERSION_FACTOR)

    def check_input(self):
        try:
            input_check = int(self.root.ids.input_value.text)
            return input_check
        except ValueError:
            return 0


ConvertMilesToKms().run()
