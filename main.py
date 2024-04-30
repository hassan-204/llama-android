import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout  # Add this line
from random import randint

class RandomNumberApp(App):

    def generate_random_number(self, instance):
        self.label.text = str(randint(1, 100))

    def build(self):
        # Create a button
        self.button = Button(text="Generate Random Number",
                             size_hint=(0.5, 0.2),
                             pos_hint={'center_x': 0.5, 'center_y': 0.7})
        self.button.bind(on_press=self.generate_random_number)

        # Create a label to display the random number
        self.label = Label(text="Press the button to generate a random number",
                           size_hint=(0.5, 0.2),
                           pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # Create a layout to hold the button and label
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.button)
        layout.add_widget(self.label)

        return layout

if __name__ == '__main__':
    RandomNumberApp().run()
