from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager

class Winder(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        line = BoxLayout(orientation='horizontal')
        lin5 = BoxLayout(orientation='vertical')

        helboy = Label(text='Hi, Gitler')
        line.add_widget(helboy)

        kipish = Button(text='Германія', on_press=self.on_sec_wind)
        kipis1 = Button(text='Ещкерія')
        kipis2 = Button(text='Миж Азіей і Гетеропой, єсь регейон асобьий, хтось мала страна')
        kipis3 = Button(text='Братульньй преїдетнт')
        line.add_widget(lin5)
        lin5.add_widget(kipish)
        lin5.add_widget(kipis1)
        lin5.add_widget(kipis2)
        lin5.add_widget(kipis3)
        self.add_widget(line)
    def on_sec_wind(self, *args):
        self.manager.current = 'second'

class SecondWinder(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        line = BoxLayout(orientation='vertical')
        one = Button(text='SecondWindow', on_press=self.second)
        line.add_widget(one)
        self.add_widget(line)

    def second(self, *args):
        print(123)

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Winder(name='main'))
        sm.add_widget(SecondWinder(name='second'))
        return sm

MyApp().run()