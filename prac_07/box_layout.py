
from kivy.app import App
from kivy.lang import Builder


class BoxLayout(App):
    def build(self):
        self.title = "Box Layout"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_clear(self):
        self.root.ids.input_label.text = ""
        self.root.ids.output_label.text = ""

    def handle_greet(self):
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_label.text


BoxLayout().run()
