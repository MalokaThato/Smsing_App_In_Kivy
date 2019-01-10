import kivy
import smstest
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import Property, ObjectProperty
from kivy.uix.listview import ListItemButton





class smsing(BoxLayout):
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
        self.ids["create_draft"].adapter.data.append("Draft")



class smsingApp(App):

    def build(self):
        return smsing()


if __name__ == "__main__":
    smsingApp().run()
