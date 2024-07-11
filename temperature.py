from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.uix.boxlayout import BoxLayout
import obd
from kivy.uix.screenmanager import Screen


class TemperatureScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.dgr_label = MDLabel(text="sensore:", halign="center")

        self.add_widget(self.dgr_label)

    def on_start(self):
        # تعيين عنوان IP ومنفذ الواجهة OBD II WiFi
        obd_interface_ip = "192.168.0.11"
        obd_interface_port = 35000

        try:
            # إعداد اتصال OBD II WiFi
            connection = obd.OBD(f"tcp://{obd_interface_ip}:{obd_interface_port}")

            if connection.is_connected():
                # قراءة قيمة درجة حرارة الهواء المتداخل
                cmd = obd.commands.INTAKE_TEMP
                response = connection.query(cmd)

                if response.is_null():
                    air_temp_text = "Unable to read intake air temperature"
                else:
                    air_temp = response.value.to("degC")
                    air_temp_text = f"Intake air temperature: {air_temp}"
            else:
                air_temp_text = "Failed to connect to OBD-II device"
        except:
            air_temp_text = "Failed to establish OBD connection"

        self.dgr_label.text = air_temp_text

        connection.close()