import kivy
import smstest
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import Property, ObjectProperty
from kivy.uix.listview import ListItemButton
from time import gmtime, strftime
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, CardTransition


#importing screen classes

from contacts import contacts_screen
from sent_msg import sent_screen
from received_msg import received_screen
import received_msg

# import the smsing # DEBUG:
import sms_db



class smsing(Screen):
    msg = ObjectProperty()
    number = ObjectProperty()
    contacts_list = ObjectProperty()
    #draft_list_view = ObjectProperty()

    def load_contacts(self):

        cont_list = ["Mathapelo: 0817769744", "Thato: 0739548248", "Chipo: 0789652354"]
        self.contacts_list.values= cont_list

        if self.contacts_list.text != "Contacts":
            cont_num = self.contacts_list.text.split(":")
            self.number.text = cont_num[1]


    def send_sms(self):
        smstest.password = str(input("Please enter your winsms password: "))
        smstest.msg = self.msg.text
        smstest.num = (self.number.text).replace(" ","")
        smstest.send_sms()

    def add_draft(self):
        self.ids["create_draft"].adapter.data.append(str(strftime("%Y-%m-%d %H:%M:%S", gmtime())) + "\n" + self.msg.text[:10] + "...")


    #Functions for selecting screens

    def to_contacts(self):
        self.manager.transition = CardTransition(direction="left")
        self.manager.current = 'contacts_screen'

    def to_sent(self):
        self.manager.transition = CardTransition(direction="right")
        self.manager.current = 'sent_msg_screen'

    def to_received(self):
        self.manager.transition = CardTransition(direction="up")
        self.manager.current = 'received_msg_screen'





class smsingApp(App):

    def build(self):

        manager = ScreenManager()

        manager.add_widget(smsing(name="smsing_screen"))
        manager.add_widget(contacts_screen(name='contacts_screen'))
        manager.add_widget(sent_screen(name='sent_msg_screen'))
        manager.add_widget(received_screen(name='received_msg_screen'))


        return manager


if __name__ == "__main__":
    smsingApp().run()
