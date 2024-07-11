from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from app1 import App1Screen
from app2 import App2Screen
from app3 import App3Screen
from app4 import App4Screen
from app5 import App5Screen
from app6 import App6Screen
from kivy.core.window import Window
from fuel import FuelScreen


Window.size = (330, 580)


class TestApp(MDApp):
    def build(self):
        screen_manager = ScreenManager()

        screen_manager.add_widget(App1Screen(name="app1"))
        screen_manager.add_widget(App2Screen(name="app2"))
        screen_manager.add_widget(App3Screen(name="app3"))
        screen_manager.add_widget(App4Screen(name="app4"))
        screen_manager.add_widget(App5Screen(name="app5"))
        screen_manager.add_widget(App6Screen(name="app6"))
        screen_manager.add_widget(FuelScreen(name="fuel"))

        screen_manager.current = "app1"


        return screen_manager


if __name__ == "__main__":
    TestApp().run()