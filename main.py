from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty
from kivy.clock import Clock

import time_manager as tm

alarm_file = "./timetable.txt"

class RoutineMain(BoxLayout):
    current_alarm_name = StringProperty(None)
    current_alarm_time = StringProperty(None)
    current_alarm_description = StringProperty(None)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.adding = 'added'

    def update(self, dt):
        print("Start update")
        alarms = tm.get_alarm_data(alarm_file)
        if alarms != False:
            print("I will be not seen if it fails")
            self.current_alarm_name = 'Brand new'
            self.current_alarm_time = alarms[self.current_alarm_name]['time']
            self.current_alarm_description = alarms[self.current_alarm_name]['description']

    def add_new_alarm(self):
        print("Adding new alarm...")
        if  self.adding == 'added':
            self.adding  = 'adding'
            add_alarm_widget = BoxLayout(
                orientation='vertical')

            label = Label(text='New Alarm')
            name_input = TextInput(text="Name", multiline=False)
            time_input = TextInput(text="Time", multiline=False)
            desc_input = TextInput(text="Description")
            add_btn = Button(text="Add", on_press=self.save_alarm)

            add_alarm_widget.add_widget(label)
            add_alarm_widget.add_widget(name_input)
            add_alarm_widget.add_widget(time_input)
            add_alarm_widget.add_widget(desc_input)
            add_alarm_widget.add_widget(add_btn)

            self.add_widget(add_alarm_widget, 1)

    def save_alarm(self, instance):
        self.remove_widget(self.children[-2])
        self.adding = 'added'
        print("Removed")

class RoutineApp(App):
    def build(self):
        routine = RoutineMain()
        Clock.schedule_interval(routine.update, 1.0/60.0)
        return  routine

if __name__ == "__main__":
    routine = RoutineApp()
    routine.run()
