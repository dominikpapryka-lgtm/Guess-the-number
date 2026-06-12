from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager
from random import randint

name = ''
your_number = 0
random_number = 0

class FirstWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.btn = Button(text='Start', size_hint = (0.3, 0.2), pos_hint = {'center_x':0.5})
        self.btn.on_press = self.next
        text=Label(text='Welcome to the game "Guess the number"!')
        text2=Label(text='Enter name:', halign="right", outline_color='yellow')
        self.in_name = TextInput(multiline = False)
        inputline = BoxLayout(orientation= 'horizontal', size_hint=(0.8, None), height="30sp")
        inputline.add_widget(text2)
        inputline.add_widget(self.in_name)
        windowline = BoxLayout(orientation='vertical', padding = 8, spacing = 8)
        windowline.add_widget(text)
        windowline.add_widget(inputline)
        windowline.add_widget(self.btn)
        self.add_widget(windowline)
        
    def next(self):
        global name
        name = self.in_name.text
        self.manager.transition.direction = 'up'
        self.manager.current = "second"

class SecondWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.btn = Button(text='Go to next window', size_hint = (0.3, 0.2), pos_hint = {'center_x':0.5})
        self.btn.on_press = self.next
        verline = BoxLayout(orientation='vertical', padding = 8, spacing = 8)
        text3 = Label(text='Write down a number from 1-10')
        self.your_number = TextInput(multiline=False, size_hint=(1, None), height="30sp")
        verline.add_widget(text3)
        verline.add_widget(self.your_number)
        verline.add_widget(self.btn)
        self.add_widget(verline)

    def next(self):
        global your_number, random_number
        your_number = int(self.your_number.text)
        random_number = randint(1, 10)
        self.manager.transition.direction = 'left'
        self.manager.current = "third"

class ThirdWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.btn = Button(text='End game', size_hint = (0.3, 0.2), pos_hint = {'center_x':0.5})
        self.btn.on_press = self.next
        verline = BoxLayout(orientation='vertical', padding = 8, spacing = 8)
        horline1 = BoxLayout(orientation='horizontal')
        horline2 = BoxLayout(orientation='horizontal')
        self.text4 = Label(text=f'Random number: {random_number}')
        self.text5 = Label(text=f'Your number: {your_number}')
        horline1.add_widget(self.text4)
        horline2.add_widget(self.text5)
        verline.add_widget(horline1)
        verline.add_widget(horline2)
        verline.add_widget(self.btn)
        self.add_widget(verline)

    def next(self):
        global your_number, random_number
        self.manager.transition.direction = 'left'
        if your_number == random_number:
            self.manager.current = 'fourth'
        else:
            self.manager.current = 'fifth'

    def on_pre_enter(self, *args):
        global your_number, random_number
        self.text5.text = f'Your number: {your_number}'
        self.text4.text = f'Random number: {random_number}'

class FourthWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.btn = Button(text='Try again', size_hint = (0.3, 0.2), pos_hint = {'center_x':0.5})
        self.btn.on_press = self.next
        verline = BoxLayout(orientation='vertical', padding = 8, spacing = 8)
        self.text6 = Label(text=f'Congratulations {name}')
        text7 = Label(text='You have won')
        verline.add_widget(self.text6)
        verline.add_widget(text7)
        verline.add_widget(self.btn)
        self.add_widget(verline)

    def on_pre_enter(self, *args):
        global name
        self.text6.text = f'Congratulations {name}'

    def next(self):
        self.manager.current = 'first'

class FifthWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.btn = Button(text='Try again', size_hint = (0.3, 0.2), pos_hint = {'center_x':0.5})
        self.btn.on_press = self.next
        verline = BoxLayout(orientation='vertical', padding = 8, spacing = 8)
        self.text6 = Label(text=f'Congratulations {name}')
        text7 = Label(text='You have lost')
        verline.add_widget(self.text6)
        verline.add_widget(text7)
        verline.add_widget(self.btn)
        self.add_widget(verline)

    def on_pre_enter(self, *args):
        global name
        self.text6.text = f'Congratulations {name}'

    def next(self):
        self.manager.current = 'first'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstWindow(name="first"))
        sm.add_widget(SecondWindow(name="second"))
        sm.add_widget(ThirdWindow(name="third"))
        sm.add_widget(FourthWindow(name='fourth'))
        sm.add_widget(FifthWindow(name='fifth'))
        return sm

app = MyApp()
app.run()