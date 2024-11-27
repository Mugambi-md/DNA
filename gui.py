from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button

class DowryApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)
        #Name
        self.add_widget(Label(text="Bride's Name:"))
        self.name_input = TextInput(multiline=False)
        self.add_widget(self.name_input)

        #Age
        self.add_widget(Label(text="Bride's Age:"))
        self.age_input = TextInput(multiline=False, input_filter="int")
        self.add_widget(self.age_input)

        #Dowry Asked
        self.add_widget(Label(text="Asked Dowry (in currency):"))
        self.dowry_input = TextInput(multiline=False, input_filter="float")
        self.add_widget(self.dowry_input)

        #Single Mother
        self.add_widget(Label(text="Is Sha a Single Mother?"))
        self.single_mother_checkbox = CheckBox()
        self.add_widget(self.single_mother_checkbox)

        #Attended College
        self.add_widget(Label(text="Attended College?"))
        self.college_checkbox = CheckBox()
        self.add_widget(self.college_checkbox)

        #Boarding/Day Scholar Spinner
        self.add_widget(Label(text="Boarding/Day scholar (if attended college):)"))
        self.college_spinner = Spinner(values=["Select", "Boarding", "Day Scholar"], text="Select")
        self.college_spinner.disabled = True #Disabled until college checkbox is checked
        self.add_widget(self.college_spinner)

        #Toggle Spinner on College Checkbox
        self.college_checkbox.bind(active=self.toggle_college_spinner)

        #Calculate Button
        self.calculate_button = Button(text="Calculate Dowry")
        self.add_widget(self.calculate_button)

        #Output Label
        self.result_label = Label(text="Result will appear here")
        self.add_widget(self.result_label)

    def toggle_college_spinner(self, instance, value):
        self.college_spinner.disabled = not value

class DowryAppGUI(App):
    def build(self):
        return DowryApp()
    
if __name__ == "__main__":
    DowryAppGUI().run()