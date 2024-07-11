from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
import threading
import socket


class EngineScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.connection_label = MDLabel(text="Waiting for result...")
        self.temp_label = MDLabel(text=" ")
        self.pressure_label = MDLabel(text=" ")

        self.add_widget(self.connection_label)
        self.add_widget(self.temp_label)
        self.add_widget(self.pressure_label)

    def on_start(self):
        # Start a separate thread for the OBD-II communication
        threading.Thread(target=self.obd_communication).start()

    def obd_communication(self):
        # تعيين عنوان IP ومنفذ الواجهة OBD II WiFi
        obd_interface_ip = "192.168.0.10"
        obd_interface_port = 35000

        # إعداد اتصال OBD II WiFi باستخدام مكتبة socket
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            connection.connect((obd_interface_ip, obd_interface_port))
            self.connection_label.text = "Successfully connected to OBD-II device"
        except Exception as e:
            self.connection_label.text = f"Failed to connect to OBD-II device: {str(e)}"
            return

        # Read oil temperature
        cmd_temp = b"01 5C\r"  # Command to read oil temperature
        connection.send(cmd_temp)
        response_temp = connection.recv(1024)

        # Read oil pressure
        cmd_pressure = b"01 5D\r"  # Command to read oil pressure
        connection.send(cmd_pressure)
        response_pressure = connection.recv(1024)

        # Close the OBD-II connection
        connection.close()

        # Update the UI with the received data on the main thread
        Clock.schedule_once(lambda dt: self.update_labels(response_temp, response_pressure), 0)

    def update_labels(self, response_temp, response_pressure):
        if response_temp:
            temp_str = response_temp.decode("utf-8").strip()
            temp_value = int(temp_str, 16)
            temp_celsius = temp_value - 40
            self.temp_label.text = f"Oil temperature: {temp_celsius} °C"
        else:
            self.temp_label.text = "Unable to read oil temperature"

        if response_pressure:
            pressure_str = response_pressure.decode("utf-8").strip()
            pressure_value = int(pressure_str, 16)
            self.pressure_label.text = f"Oil pressure: {pressure_value} kPa"
        else:
            self.pressure_label.text = "Unable to read oil pressure"


class OBDInterfaceApp(MDApp):
    def build(self):
        return EngineScreen()


if __name__ == "__main__":
    OBDInterfaceApp().run()
