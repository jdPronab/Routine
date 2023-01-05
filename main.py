from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout

class RoutineMain(BoxLayout):
    pass

class RoutineApp(App):
    def build(self):
        routine = RoutineMain()
        return  routine

if __name__ == "__main__":
    routine = RoutineApp()
    routine.run()
