from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.popup import Popup
import socket


class OBDInterfaceApp(MDApp):
    def __init__(self, **kwargs):
        self.connection = None
        super().__init__(**kwargs)

    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20)

        title_label = Label(
            text="OBD-II Interface Application",
            font_size=30,
            size_hint=(None, None),
            size=(400, 50)
        )

        connect_button = MDRectangleFlatButton(
            text="Connect to OBD-II Interface",
            font_size=20,
            size_hint=(None, None),
            size=(300, 50),
            on_release=self.connect_obd_interface
        )

        check_status_button = MDRectangleFlatButton(
            text="Check OBD-II Interface Status",
            font_size=20,
            size_hint=(None, None),
            size=(300, 50),
            on_release=self.check_obd_interface_status
        )

        check_temp_button = MDRectangleFlatButton(
            text="Check Car Temperature",
            font_size=20,
            size_hint=(None, None),
            size=(300, 50),
            on_release=self.check_car_temperature
        )

        check_errors_button = MDRectangleFlatButton(
            text="Read Error Codes",
            font_size=20,
            size_hint=(None, None),
            size=(300, 50),
            on_release=self.read_error_codes
        )

        check_fuel_button = MDRectangleFlatButton(
            text="Check Fuel Level",
            font_size=20,
            size_hint=(None, None),
            size=(300, 50),
            on_release=self.check_fuel_level
        )

        check_battery_button = MDRectangleFlatButton(
            text="Check Battery Status",
            font_size=20,
            size_hint=(None, None),
            size=(300, 50),
            on_release=self.check_battery_status
        )
        check_oxygen_button = MDRectangleFlatButton(
            text="Check Oxygen Level",
            font_size=20,
            size_hint=(None, None),
            size=(300, 50),
            on_release=self.check_oxygen_level
        )

        layout.add_widget(title_label)
        layout.add_widget(connect_button)
        layout.add_widget(check_status_button)
        layout.add_widget(check_temp_button)
        layout.add_widget(check_errors_button)
        layout.add_widget(check_fuel_button)
        layout.add_widget(check_battery_button)
        layout.add_widget(check_oxygen_button)

        return layout

    def connect_obd_interface(self, instance):
        try:
            host = "192.168.0.10"  # OBD-II WiFi Interface IP address
            port = 35000  # OBD-II WiFi Interface port number
            self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.connection.connect((host, port))
            self.show_popup("Successfully connected to OBD-II Interface!")
        except Exception as e:
            self.show_popup(f"Failed to connect to OBD-II Interface: {str(e)}")

    def check_obd_interface_status(self, instance):
        if self.connection:
            self.show_popup("OBD-II Interface is connected!")
        else:
            self.show_popup("OBD-II Interface is not connected!")

    def check_car_temperature(self, instance):
        if self.connection:
            command = b'0105\r'  # OBD-II command to read coolant temperature
            self.connection.send(command)
            response = self.connection.recv(1024)
            temperature = self.parse_temperature(response)
            if temperature is not None:
                self.show_popup(f"Car temperature: {temperature} °C")
            else:
                self.show_popup("Unable to read car temperature")
        else:
            self.show_popup("OBD-II Interface is not connected!")

    def read_error_codes(self, instance):
        if self.connection:
            command = b'03\r'  # OBD-II command to read error codes
            self.connection.send(command)
            response = self.connection.recv(1024)
            error_codes = self.parse_error_codes(response)
            if error_codes:
                self.show_popup("Error Codes:\n" + "\n".join(error_codes))
            else:
                self.show_popup("No error codes found")
        else:
            self.show_popup("OBD-II Interface is not connected!")

    def check_fuel_level(self, instance):
        if self.connection:
            command = b'012F\r'  # OBD-II command to read fuel level
            self.connection.send(command)
            response = self.connection.recv(1024)
            fuel_level = self.parse_fuel_level(response)
            if fuel_level is not None:
                self.show_popup(f"Fuel level: {fuel_level}%")
            else:
                self.show_popup("Unable to read fuel level")
        else:
            self.show_popup("OBD-II Interface is not connected!")

    def check_battery_status(self, instance):
        if self.connection:
            self.show_popup("Reading battery status...")
            command = b'0101\r'  # OBD-II command to read battery status
            self.connection.send(command)
            response = self.connection.recv(1024)
            battery_voltage = self.parse_battery_voltage(response)
            if battery_voltage is not None:
                self.show_popup(f"Battery voltage: {battery_voltage} V")
            else:
                self.show_popup("Unable to read battery status")
        else:
            self.show_popup("OBD-II Interface is not connected!")

    def check_oxygen_level(self, instance):
        if self.connection:
            command = b'0115\r'  # OBD-II command to read oxygen level
            self.connection.send(command)
            response = self.connection.recv(1024)
            oxygen_level = self.parse_oxygen_level(response)
            if oxygen_level is not None:
                self.show_popup(f"Oxygen level: {oxygen_level}%")
            else:
                self.show_popup("Unable to read oxygen level")
        else:
            self.show_popup("OBD-II Interface is not connected!")

    def parse_temperature(self, response):
        try:
            response = response.decode().strip()
            if response.startswith("41 05"):
                temperature_hex = response[6:8]
                temperature_celsius = int(temperature_hex, 16) - 40
                return temperature_celsius
            return None
        except Exception:
            return None

    def parse_error_codes(self, response):
        try:
            response = response.decode().strip()
            if response.startswith("43"):
                codes = response.split("\r")
                error_codes = [code[2:] for code in codes if code[2:] != "0000"]
                return error_codes
            return []
        except Exception:
            return []

    def parse_fuel_level(self, response):
        try:
            response = response.decode().strip()
            if response.startswith("41 2F"):
                fuel_hex = response[6:8]
                fuel_level = int(fuel_hex, 16) * 100 / 255
                return round(fuel_level, 2)
            return None
        except Exception:
            return None

    def parse_battery_voltage(self, response):
        try:
            response = response.decode().strip()
            if response.startswith("41 01"):
                voltage_hex = response[6:8]
                voltage = int(voltage_hex, 16) / 10
                return voltage
            return None
        except Exception:
            return None

    def parse_oxygen_level(self, response):
        try:
            response = response.decode().strip()
            if response.startswith("41 15"):
                oxygen_level_hex = response[6:8]
                oxygen_level_percentage = int(oxygen_level_hex, 16) * 100 / 255
                return round(oxygen_level_percentage, 2)
            return None
        except Exception:
            return None


    def show_popup(self, text):
        popup = Popup(title='OBD-II Interface', content=Label(text=text), size_hint=(None, None), size=(400, 200))
        popup.open()


if __name__ == "__main__":
    OBDInterfaceApp().run()

