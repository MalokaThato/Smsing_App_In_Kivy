import kivy
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, CardTransition


class sent_screen(Screen):
    def to_home(self):
        self.manager.transition = CardTransition(direction="left")
        self.manager.current = 'smsing_screen'
