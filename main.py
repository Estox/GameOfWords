from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from  kivy.uix.vkeyboard import VKeyboard

Builder.load_string("""
<Background>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'Start'
            on_press: root.manager.current = 'select'
        Button:
            text: 'Settings'
            on_press: root.manager.current = 'settings'
        Button:
            text: 'Quit'
            on_press: app.stop()

<SettingsScreen>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'My settings button'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
<Select>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'Local mode'
            on_press: root.manager.current = 'local'
        Button:
            text: 'Mode 2'
        Button:
            text: 'Mode 3'
        Button:
            text: 'Mode 4'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
<Local>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'images/background.jpg'
    GameButton:
        text: 'E'
        pos: root.width - self.size[0], root.height - self.size[1]
    GameButton:
        text: 'C'
        pos: 0, root.height - self.size[1]
<GameButton>:
    size_hint: 0.1, 0.1
<KeyboardButton>:
    size_hint: 0.05, 0.05
""")

class Background(Screen):
    pass

class SettingsScreen(Screen):
    pass

class Select(Screen):
    pass

class Local(Screen):
    pass

class GameButton(Button):
    def on_press(self):
        vk = VKeyboard()
        vk.layout = 'keyboards/keyboard.json'
        self.parent.add_widget(vk)

class KeyboardButton(Button):
    pass

sm = ScreenManager()
sm.add_widget(Background(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))
sm.add_widget(Select(name='select'))
sm.add_widget(Local(name='local'))

class TestApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()