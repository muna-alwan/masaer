from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.uix.boxlayout import BoxLayout
import obd
from kivy.uix.screenmanager import Screen

class FuelScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.fuel_level_label = MDLabel(text="Fuel level:", pos_hint={"center_x": 0.9, "center_y": 0.5})
        self.add_widget(self.fuel_level_label)
        self.fuel_consumption_label = MDLabel(text="Fuel consumption:", pos_hint={"center_x": 0.7, "center_y": 0.3})
        self.add_widget(self.fuel_consumption_label)
        self.other_fuel_info_label = MDLabel(text="Other fuel information:",
                                             pos_hint={"center_x": 0.7, "center_y": 0.1})
        self.add_widget(self.other_fuel_info_label)

    def on_start(self):
        # تعيين عنوان IP ومنفذ الواجهة OBD II WiFi
        obd_interface_ip = "192.168.0.11"
        obd_interface_port = 35000

        # إعداد اتصال OBD II WiFi
        connection = obd.OBD(f"tcp://{obd_interface_ip}:{obd_interface_port}")

        fuel_level_command = obd.commands.FUEL_LEVEL
        fuel_level_response = connection.query(fuel_level_command)
        if fuel_level_response.is_null():
            self.fuel_level_label.text = "Unable to read fuel level"
        else:
            self.fuel_level_label.text = f"Fuel level: {fuel_level_response.value}"

        fuel_consumption_command = obd.commands.FUEL_CONSUMPTION
        fuel_consumption_response = connection.query(fuel_consumption_command)
        if fuel_consumption_response.is_null():
            self.fuel_consumption_label.text = "Unable to read fuel consumption"
        else:
            self.fuel_consumption_label.text = f"Fuel consumption: {fuel_consumption_response.value}"

        other_fuel_info_command = obd.commands.OTHER_FUEL_INFO
        other_fuel_info_response = connection.query(other_fuel_info_command)
        if other_fuel_info_response.is_null():
            self.other_fuel_info_label.text = "Unable to read other fuel information"
        else:
            self.other_fuel_info_label.text = f"Other fuel information: {other_fuel_info_response.value}"

        connection.close()