from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

#Import backend functions
from backend import body_count, dowry_negotiation

class DowryApp(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(cols=1, spacing=10, padding=20, **kwargs)

        self.inside = GridLayout(cols=2, spacing=10)
        #Bride's Name
        self.inside.add_widget(Label(text="Bride's Name:"))
        self.name_input = TextInput(multiline=False)
        self.inside.add_widget(self.name_input)
        # Bride's Age
        self.inside.add_widget(Label(text="Bride's Age:"))
        self.age_input = TextInput(multiline=False, input_filter="int")
        self.inside.add_widget(self.age_input)
        # Asked dowry
        self.inside.add_widget(Label(text="Asked Dowry\n(in currency):"))
        self.dowry_input = TextInput(multiline=False, input_filter="float")
        self.inside.add_widget(self.dowry_input)
        # Single Mother Checkbox
        self.inside.add_widget(Label(text="She is Single Mum?"))
        self.single_mother_checkbox = CheckBox()
        self.inside.add_widget(self.single_mother_checkbox)
        # College Checkbox
        self.inside.add_widget(Label(text="Attended College?"))
        self.college_checkbox = CheckBox()
        self.inside.add_widget(self.college_checkbox)
        # College Spinner
        self.inside.add_widget(Label(text="Boarding/Day Scholar\n(if attended college):"))
        self.college_spinner = Spinner(
            values=["Boarding", "Day Scholar"],
            text="Select",
            disabled=True
        )
        self.inside.add_widget(self.college_spinner)
        # Bind checkbox to toggle spinner
        self.college_checkbox.bind(active=self.toggle_college_spinner)
        # Add the inner grid to the main layout
        self.add_widget(self.inside)
        # Centering the Calculate button
        button_box = BoxLayout(size_hint=(1, None), height=50, padding=[0, 10, 0, 10])
        self.calculate_button = Button(
            text="Calculate Dowry",
            size_hint=(0.5, 1),
        )
        self.calculate_button.bind(on_press=self.calculate_dowry)
        button_box.add_widget(self.calculate_button)
        self.add_widget(button_box)
        # Result label
        self.result_label = Label(
            text="Result will appear here",
            size_hint=(1, None),
            halign="center",
            valign="middle"
        )
        self.result_label.bind(size=self.result_label.setter("text_size"))
        self.add_widget(self.result_label)

    def toggle_college_spinner(self, instance, value):
        """Enable or disable spinner based on college checkbox."""
        self.college_spinner.disabled = not value

    def calculate_dowry(self, instance):
        """Handle dowry calculation on button press."""
        try:
            name = self.name_input.text
            age = int(self.age_input.text)
            asked_dowry =float(self.dowry_input.text)
            single_mother = self.single_mother_checkbox.active
            college = self.college_checkbox.active

            if age <18:
                self.result_label.text ="Age must be 18 or above."
                return
            if asked_dowry <= 0:
                self.result_label.text="Asked dowry must be greater than 0."
                return
            
            body_count_result =body_count(age)
            result = dowry_negotiation(name, age, body_count_result, asked_dowry, single_mother, college)
            self.result_label.text = result
        except ValueError:
            self.result_label.text ="Please fill all fields correctly."

class DowryAppGUI(App):
    def build(self):
        return DowryApp()
if __name__ == "__main__":
    DowryAppGUI().run()