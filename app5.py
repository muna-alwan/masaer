

from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle


class App5Screen(Screen):
    def __init__(self, **kwargs):
        super(App5Screen, self).__init__(**kwargs)

        with self.canvas:
            Color(0.15, 0.2, 0.3, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        button1 = MDRectangleFlatButton(
            pos_hint={"center_x": .9, "center_y": .1},
            on_release=self.go_to_app2,
            line_color=(0, 0, 0, 0)
        )
        button1.size_hint = (0.1, 0.1)
        image = Image(source='car.png')
        button1.add_widget(image)
        self.add_widget(button1)

        button2 = MDRectangleFlatButton(
            pos_hint={"center_x": .7, "center_y": .1},
            on_release=self.go_to_app3,
            line_color=(0, 0, 0, 0)
        )
        button2.size_hint = (0.1, 0.1)
        image = Image(source='car-key.png')
        button2.add_widget(image)
        self.add_widget(button2)

        button3 = MDRectangleFlatButton(
            pos_hint={"center_x": .5, "center_y": .1},
            on_release=self.go_to_app4,
            line_color=(0, 0, 0, 0)
        )
        button3.size_hint = (0.1, 0.1)
        image = Image(source='location.png')
        button3.add_widget(image)
        self.add_widget(button3)

        button4 = MDRectangleFlatButton(
            pos_hint={"center_x": .3, "center_y": .1},
            on_release=self.go_to_app5,
            line_color=(0, 0, 0, 0)
        )
        button4.size_hint = (0.1, 0.1)
        image = Image(source='settings (1).png')
        button4.add_widget(image)
        self.add_widget(button4)

        button5 = MDRectangleFlatButton(
            pos_hint={"center_x": .1, "center_y": .1},
            on_release=self.go_to_app6,
            line_color=(0, 0, 0, 0)
        )
        button5.size_hint = (0.1, 0.1)
        image = Image(source='car.png')
        button5.add_widget(image)
        self.add_widget(button5)
        image1 = Image(
            pos_hint={"center_x": .5, "center_y": .2},
            source='haedcar.png'
        )
        image1.size_hint = (1.5, 1.5)
        self.add_widget(image1)
    def go_to_app2(self, instance):
        self.manager.current = "app2"

    def go_to_app3(self, instance):
        self.manager.current = "app3"

    def go_to_app4(self, instance):
        self.manager.current = "app4"

    def go_to_app5(self, instance):
        self.manager.current = "app5"

    def go_to_app6(self, instance):
        self.manager.current = "app6"

    def on_size(self, *args):
        self.rect.size = self.size

    def on_pos(self, *args):
        self.rect.pos = self.pos