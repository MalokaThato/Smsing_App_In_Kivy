import kivy
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, CardTransition


class contacts_screen(Screen):
    def to_home(self):
        self.manager.transition = CardTransition(direction="right")
        self.manager.current = 'smsing_screen'
