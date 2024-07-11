from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.uix.boxlayout import BoxLayout
import obd
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock


class WheelScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.toolbar = MDLabel(text="Tire Pressure Reader")

        self.pressure_label = MDLabel(id='pressure_label', halign='center')
        self.add_widget(self.toolbar)
        self.add_widget(self.pressure_label)

    def on_start(self):
        Clock.schedule_once(self.connect_obd)

        commands = [
            obd.commands.PRESSURE_CONTROL_MODULE_D,
            obd.commands.PRESSURE_CONTROL_MODULE_E,
            obd.commands.PRESSURE_CONTROL_MODULE_F,
            obd.commands.PRESSURE_CONTROL_MODULE_10,
        ]
        pressures = []
        for command in commands:
            response = self.connection.query(command)
            if response.is_null():
                pressures.append("N/A")
            else:
                pressures.append(str(response.value.magnitude) + response.value.units)
        self.pressure_text = "\n".join(pressures)