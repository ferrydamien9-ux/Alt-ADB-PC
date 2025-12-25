import sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from ppadb.client import Client as AdbClient

# Set window size to look like a tool
Window.size = (400, 600)

class AltADB_Interface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 30
        self.spacing = 20

        self.add_widget(Label(
            text="debugHELPER: Alt-ADB",
            font_size='24sp',
            bold=True,
            size_hint_y=None,
            height=50
        ))

        self.status = Label(
            text="Status: Disconnected",
            color=(1, 0.3, 0.3, 1) # Reddish
        )
        self.add_widget(self.status)

        self.scan_btn = Button(
            text="SCAN FOR DEVICE",
            background_color=(0.2, 0.6, 1, 1),
            size_hint_y=None,
            height=60
        )
        self.scan_btn.bind(on_press=self.check_adb)
        self.add_widget(self.scan_btn)

    def check_adb(self, instance):
        try:
            # Default ADB port is 5037
            client = AdbClient(host="127.0.0.1", port=5037)
            devices = client.devices()
            
            if len(devices) == 0:
                self.status.text = "Status: No Device Found\n(Check USB Debugging)"
                self.status.color = (1, 0.5, 0, 1) # Orange
            else:
                device = devices[0]
                self.status.text = f"Status: CONNECTED\nID: {device.serial}"
                self.status.color = (0.3, 1, 0.3, 1) # Green
        except Exception:
            self.status.text = "Error: ADB Server not running\nStart ADB on your PC first."
            self.status.color = (1, 0, 0, 1) # Bright Red

class AltADBApp(App):
    def build(self):
        Window.clearcolor = (0.1, 0.1, 0.1, 1) # Dark theme
        self.title = "Alt-ADB PC"
        return AltADB_Interface()

if __name__ == '__main__':
    AltADBApp().run()
