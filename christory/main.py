import data
from kivy.app import App
from kivy.uix.screenmanager import Screen
import numpy as np
import pandas as pd


class ChristoryApp(App):
    pass

class TitleScreen(Screen):
    #Gets the base map and stores it as a dataframe
    def get_base_map():
        path = r'E:\code\python\kivy\christory\data\map-base.xlsx'
        df = pd.read_excel(path)
        data.Game.game_map = df



class MainGameScreen(Screen):
    pass



if __name__ == '__main__':
    ChristoryApp().run()
