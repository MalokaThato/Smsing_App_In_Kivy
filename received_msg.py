import kivy
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, CardTransition

from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton
import sqlite3 as db



class ReceivedListButton(ListItemButton):
    pass

class received_screen(Screen):

    received_list = ObjectProperty()
    con = db.connect("sms_db.db")
    cur = con.cursor()

    def submit_Rlist(self):


        db_list = []


        try:
            #with con:
            # cur.execute("INSERT INTO Users(name, password, email_address) VALUES('Timothy', 'paswword123', 'admin@admin.com')")

            self.cur.execute("SELECT * FROM received_sms")
            result = self.cur.fetchall()

            print("printing results: \n" + str(result))

            for item in result:
                print (item)
                rev_sms_text = str(str(item[1]) +":  "+ str(item[3]) +"\n" + str(item[2]))
                print(type(rev_sms_text))

                db_list.append(rev_sms_text)

                self.received_list.adapter.data.extend(list(db_list))
            self.received_list._trigger_reset_populate()

        except Exception as e:
            print (e)

        finally:
            self.cur.close()





    # This part of the code will be used for deleting items

    def delete_Rlist(self):
        if self.received_list.adapter.selection:
            self.received_list.adapter.selection[0].text
            self.received_list._trigger_reset_populate()


    def to_home(self):
        self.manager.transition = CardTransition(direction="down")
        self.manager.current = 'smsing_screen'
