from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.clock import Clock

import time_manager as tm

alarm_file = "./timetable.txt"

class RoutineMain(BoxLayout):
    current_alarm_name = StringProperty(None)
    current_alarm_time = StringProperty(None)
    current_alarm_description = StringProperty(None)

    def update(self, dt):
        alarms = tm.get_alarm_data(alarm_file)
        self.current_alarm_name = 'Brand new'
        self.current_alarm_time = alarms[self.current_alarm_name]['time']
        self.current_alarm_description = alarms[self.current_alarm_name]['description']

class RoutineApp(App):
    def build(self):
        routine = RoutineMain()
        Clock.schedule_interval(routine.update, 1.0/60.0)
        return  routine

if __name__ == "__main__":
    routine = RoutineApp()
    routine.run()
