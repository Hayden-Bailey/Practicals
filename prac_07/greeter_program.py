
from kivy.app import App
from kivy.lang import Builder


class BoxLayout(App):
    def build(self):
        self.title = "Greeter Program"
        self.root = Builder.load_file('greeter_program.kv')
        return self.root

    def handle_clear(self):
        self.root.ids.input_label.text = ""
        self.root.ids.output_label.text = ""

    def handle_greet(self):
        print('test')
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_label.text


BoxLayout().run()
