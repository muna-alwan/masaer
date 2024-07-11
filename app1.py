

from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.uix.popup import Popup
import socket
from kivy.uix.label import Label


class App1Screen(Screen):
    def __init__(self, **kwargs):
        self.connection = None
        super(App1Screen, self).__init__(**kwargs)

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
        image2 = Image(
            pos_hint={"center_x": .5, "center_y": .6},
            source='carapp.png'
        )
        image2.size_hint = (1.2, 1.2)
        self.add_widget(image2)
        connect_button = MDRectangleFlatButton(
            pos_hint={"center_x": .1, "center_y": .2},
            on_release=self.connect_obd_interface,
            line_color=(0, 0, 0, 0)
        )
        connect_button.size_hint = (0.1, 0.1)
        image = Image(source='settings (1).png')
        connect_button.add_widget(image)
        self.add_widget(connect_button)

        check_status_button = MDRectangleFlatButton(
            pos_hint={"center_x": .1, "center_y": .3},
            on_release=self.check_obd_interface_status,
            line_color=(0, 0, 0, 0)
        )
        check_status_button.size_hint = (0.1, 0.1)
        image = Image(source='settings (1).png')
        check_status_button.add_widget(image)
        self.add_widget(check_status_button)
        check_temp_button = MDRectangleFlatButton(
            pos_hint={"center_x": .2, "center_y": 0.9},
            on_release=self.check_car_temperature,
            line_color=(0, 0, 0, 0)
        )
        check_temp_button.size_hint = (0.3, 0.3)
        image = Image(source='trep.png')
        check_temp_button.add_widget(image)
        self.add_widget(check_temp_button)
        check_errors_button = MDRectangleFlatButton(
            pos_hint={"center_x": .5, "center_y": .2},
            on_release=self.read_error_codes,
            line_color=(0, 0, 0, 0)
        )
        check_errors_button.size_hint = (0.3, 0.3)
        image = Image(source='check.png')
        check_errors_button.add_widget(image)
        self.add_widget(check_errors_button)
        check_fuel_button = MDRectangleFlatButton(
            pos_hint={"center_x": .9, "center_y": .5},
            on_release=self.check_fuel_level,
            line_color=(0, 0, 0, 0)
        )
        check_fuel_button.size_hint = (0.3, 0.3)
        image = Image(source='fuel.png')
        check_fuel_button.add_widget(image)
        self.add_widget(check_fuel_button)
        check_battery_button = MDRectangleFlatButton(
            pos_hint={"center_x": .8, "center_y": .9},
            on_release=self.check_battery_status,
            line_color=(0, 0, 0, 0)
        )
        check_battery_button.size_hint = (0.3, 0.3)
        image = Image(source='engine.png')
        check_battery_button.add_widget(image)
        self.add_widget(check_battery_button)
        check_oxygen_button = MDRectangleFlatButton(
            pos_hint={"center_x": .6, "center_y": .9},
            on_release=self.check_oxygen_level,
            line_color=(0, 0, 0, 0)
        )
        check_oxygen_button.size_hint = (0.3, 0.3)
        image = Image(source='ox.png')
        check_oxygen_button.add_widget(image)
        self.add_widget(check_oxygen_button)


    def go_to_app2(self,instance):
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