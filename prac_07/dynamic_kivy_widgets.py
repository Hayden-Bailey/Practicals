
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label
from kivy.properties import StringProperty


class DynamicWidgets(App):

    name_text = StringProperty()

    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        self.names = ['James', 'Jackson', 'Jeremy']

    def build(self):

        self.title = "Dynamic Kivy Widgets"
        self.root = Builder.load_file('dynamic_kivy_widgets.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):

        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.labels_box.add_widget(temp_label)


DynamicWidgets().run()
