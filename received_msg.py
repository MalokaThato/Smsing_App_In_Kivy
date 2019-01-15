import kivy
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, CardTransition


class received_screen(Screen):
    def to_home(self):
        self.manager.transition = CardTransition(direction="down")
        self.manager.current = 'smsing_screen'
