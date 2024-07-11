from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.uix.boxlayout import BoxLayout
import obd
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

class CheckUpScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.title = "OBD Reader"
        self.obd_connected = False

        self.obd_status_label = MDLabel(text="OBD Status: Connecting...", pos_hint={"center_x": 0.9, "center_y": 0.5})
        self.dtc_label = MDLabel(text="DTCs: None",  pos_hint={"center_x": 0.7, "center_y": 0.3})
        self.add_widget(self.obd_status_label)
        self.add_widget(self.dtc_label)

    def on_start(self):
        # تعيين عنوان IP ومنفذ الواجهة OBD II WiFi
        obd_interface_ip = "192.168.0.11"
        obd_interface_port = 35000

        
        try:
            # إعداد اتصال OBD II WiFi
            self.connection = obd.OBD(f"tcp://{obd_interface_ip}:{obd_interface_port}")
            if self.connection.is_connected():
                self.obd_connected = True
        except:
            self.obd_connected = False

        if self.obd_connected:
            self.obd_status_label.text = "OBD Status: Connected"
        else:
            self.obd_status_label.text = "OBD Status: Not Connected"
            self.show_obd_not_connected_dialog()

        if self.obd_connected:
            response = self.connection.query(obd.commands.GET_DTC)
            if response.is_null():
                self.dtc_label.text = "DTCs: None"
            else:
                dtc_list = response.value
                dtc_text = "\n".join(dtc_list)
                self.dtc_label.text = f"DTCs:\n{dtc_text}"

    def show_obd_not_connected_dialog(self):
        dialog = MDDialog(
            title="OBD Not Connected",
            text="OBD device is not connected. Please check the connection.",
            buttons=[
                MDFlatButton(text="Close", on_release=self.close_app)
            ]
        )
        dialog.open()

    def close_app(self, *args):
        MDApp.get_running_app().stop()