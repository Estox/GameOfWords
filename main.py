from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class TestApp(App):
    def build(self):
        background = Background()
        return background

class Background(Widget):
    pass

class  MyButton(Button):
    pass

TestApp().run()