from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button

class DowryApp(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(cols=2, spacing=10, padding=20, **kwargs)

        #Bride's Name
        self.add_widget(Label(text="Bride's Name:"))
        self.name_input = TextInput(multiline=False, size_hint=(None, None), width=250, height=40)
        self.add_widget(self.name_input)

        #Bride's Age
        self.add_widget(Label(text="Bride's Age:"))
        self.age_input = TextInput(multiline=False, input_filter="int", size_hint=(None, None), width=100, height=40)
        self.add_widget(self.age_input)

        #Asked Dowry
        self.add_widget(Label(text="Asked Dowry\n(in currency):"))
        self.dowry_input = TextInput(multiline=False, input_filter="float", size_hint=(None, None), width=300, height=40)
        self.add_widget(self.dowry_input)

        #Is She a Single Mother
        self.add_widget(Label(text="She a Single Mom?"))
        self.single_mother_checkbox = CheckBox(size_hint=(None, None), size=(40, 40))
        self.add_widget(self.single_mother_checkbox)

        #Atteded College
        self.add_widget(Label(text="Attended College?"))
        self.college_checkbox = CheckBox(size_hint=(None, None), size=(40, 40))
        self.add_widget(self.college_checkbox)

        #Boarding/Day Scholar Spinner
        self.add_widget(Label(text="Boarding/Day Scholar\n(if attended college):"))
        self.college_spinner = Spinner(
            values=["Select", "Boarding", "Day Scholar"],
            text="Select",
            size_hint=(None, None),
            width=200,
            height=40
        )
        self.college_spinner.disabled = True #Disabled until college checkbox is checked
        self.add_widget(self.college_spinner)

        #Toggle Spinner on College checkbox
        self.college_checkbox.bind(active=self.toggle_college_spinner)

        #Calculate Button (Spanning 2 Columns)
        self.calculate_button = Button(
            text="Calculate Dowry",
            size_hint=(None, None),
            width=200,
            height=50
        )
        self.add_widget(self.calculate_button)
        self.add_widget(Label()) #Add an empty widget to keep alignment

        #Result Label (spanning 2 columns)
        self.result_label = Label(
            text="Result Will Appear Here",
            size_hint=(1, None),
            height=50,
            valign="middle",
            halign="center"
        )
        self.result_label.bind(size=self.result_label.setter("text_size")) #Wrap text in the label
        self.add_widget(self.result_label)
        self.add_widget(Label()) #Add an empty widget to keep alignment
    def toggle_college_spinner(self, instance, value):
        self.college_spinner.disabled = not value

class DowryAppGUI(App):
    def build(self):
        return DowryApp()
    
if __name__ == "__main__":
    DowryAppGUI().run()