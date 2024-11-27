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
        self.add_widget(Label(text="Bride's Name:", size_hint=(1, 0.1)))
        name_layout = BoxLayout(size_hint=(None, None), width=300, height=40, pos_hint={'center_x': 0.5})
        self.name_input = TextInput(multiline=False, size_hint=(None, None), width=250, height=40)
        name_layout.add_widget(self.name_input)
        self.add_widget(name_layout)

        #Age
        self.add_widget(Label(text="Bride's Age:", size_hint=(1, 0.1)))
        age_layout = BoxLayout(size_hint=(None, None), width=200, height=40, pos_hint={'center_x': 0.5})
        self.age_input = TextInput(multiline=False, input_filter="int", size_hint=(None, None), width=100, height=40)
        age_layout.add_widget(self.age_input)
        self.add_widget(age_layout)

        #Dowry Asked
        self.add_widget(Label(text="Asked Dowry (in currency):", size_hint=(1, 0.1)))
        dowry_layout = BoxLayout(size_hint=(None, None), width=350, height=40, pos_hint={'center_x': 0.5})
        self.dowry_input = TextInput(multiline=False, input_filter="float", size_hint=(None, None), width=300,height=40)
        dowry_layout.add_widget(self.dowry_input)
        self.add_widget(dowry_layout)

        #Single Mother
        single_mother_layout = BoxLayout(orientation="horizontal", size_hint=(1, None), height=50)
        self.add_widget(Label(text="Is Sha a Single Mother?", size_hint=(1, 0.1)))
        self.single_mother_checkbox = CheckBox(size_hint=(None, None), size=(40, 40))
        single_mother_layout.add_widget(self.single_mother_checkbox)
        self.add_widget(single_mother_layout)

        #Attended College
        self.add_widget(Label(text="Attended College?", size_hint=(1, 0.1)))
        college_layout = BoxLayout(size_hint=(None, None), width=200, height=50, pos_hint={"center_x": 0.5})
        self.college_checkbox = CheckBox(size_hint=(None, None), size=(40, 40))
        college_layout.add_widget(self.college_checkbox)
        self.add_widget(college_layout)

        #Boarding/Day Scholar Spinner
        self.add_widget(Label(text="Boarding/Day scholar (if attended college):", size_hint=(1, 0.1)))
        scholar_layout = BoxLayout(size_hint=(None, None), width=300, height=40, pos_hint={'center_x': 0.5})
        self.college_spinner = Spinner(
            values=["Select", "Boarding", "Day Scholar"],
            text="Select",
            size_hint=(None, None),
            width=200,
            height=40,
            )
        self.college_spinner.disabled = True #Disabled until college checkbox is checked
        scholar_layout.add_widget(self.college_spinner)
        self.add_widget(scholar_layout)

        #Toggle Spinner on College Checkbox
        self.college_checkbox.bind(active=self.toggle_college_spinner)

        #Calculate Button
        self.calculate_button = Button(
            text="Calculate Dowry",
            size_hint=(None, None),
            width=200,
            height=50,
            pos_hint={'center_x': 0.5}
            )
        self.add_widget(self.calculate_button)

        #Output Label
        self.result_label = Label(
            text="Result will appear here",
            size_hint=(1, None),
            height=50,
            valign="middle",
            halign="center",
            )
        self.result_label.bind(size=self.result_label.setter("text_size")) #Make text wrap in label
        self.add_widget(self.result_label)

    def toggle_college_spinner(self, instance, value):
        self.college_spinner.disabled = not value

class DowryAppGUI(App):
    def build(self):
        return DowryApp()
    
if __name__ == "__main__":
    DowryAppGUI().run()