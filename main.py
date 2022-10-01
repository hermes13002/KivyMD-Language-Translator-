from deep_translator import GoogleTranslator
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.bottomsheet import MDListBottomSheet
from kivymd.uix.screen import MDScreen


class MainScreen(MDScreen):
    pass

class NavBar(MDFloatLayout):
    pass




class Exc_translator(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        



    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("splash.kv"))
        screen_manager.add_widget(Builder.load_file("main.kv"))
        return screen_manager

    def on_start(self):
        Clock.schedule_once(self.main, 8)
    
    def main(self, *args):
        screen_manager.current = "main"
    
    
    
    countries = {
    "Choose Language": "cl",
    "English": "en",
    "Dutch": "nl",
    "Greek": "el",
    "Hausa": "ha",
    "Norway": "no",
    "Spainish": "es",
    "Germany": "de",
    "French": "fr",
    "Japanese": "ja",
    "Igbo": "ig",
    "Italy": "it",
    "Korean": "ko",
    "Latin": "la",
    "Russia": "ru", 
    "Portugal": "pt",
    "Yoruba": "yo"
                 }
    direction_lang_code = StringProperty("cl")
    direction_lang = StringProperty("Choose Language")
    user_text = ""
    result=StringProperty()
    
    
    #def translate(self, user_text):
          #for key, value in self.countries.items():
                #if key == self.direction_lang:
                      #trans = GoogleTranslator(source='auto', target=value).trans.translate(self.user_text)
                      #break
          #print(trans)
          #screen_manager.get_screen('main').result.text = trans_text
    

    def translate(self, text):
        self.translated = GoogleTranslator(source='auto', target=self.direction_lang_code).translate(text)
        screen_manager.get_screen('main').result.text = self.translated
        #print(self.translated)

    def callback_for_countries_menu_items(self, *args):
        toast(args[0])
        self.direction_lang = args[0]
        self.direction_lang_code = self.countries[args[0]]

    def show_countries_list_bottom_sheet(self):
        bottom_sheet_menu = MDListBottomSheet()
        for i in range(1, 17):
            bottom_sheet_menu.add_item(
                list(self.countries.keys())[i],
                lambda x, y=i: self.callback_for_countries_menu_items(list(self.countries.keys())[y]),
            )
        bottom_sheet_menu.open()
    
    
    def win_exit(self):
          exit()


Exc_translator().run()