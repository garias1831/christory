from data import Game
from kivy.app import App
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.graphics import Color, Rectangle, Line
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
import numpy as np
import pandas as pd


class ChristoryApp(App):
    pass


class TitleScreen(Screen):
    '''Represents the starting window where the user will choose how to play. Users can start a new game or load a pre-existing one. 
    
    Methods
    -------
    get_base_map()
        Gets the base map and stores it as a dataframe.
    '''

    def get_base_map(self):
        '''Gets the base map and stores it as a dataframe. Called when user presses the 'New Game' button on the UI.'''

        path = r'E:\code\python\kivy\christory\data\map-base.xlsx' #TODO -- make this path more dynamic, 
        df = pd.read_excel(path)
        Game.game_map = df.copy() 



class MainGameScreen(Screen):
    '''Represents the window where the game will actually be played.'''


class GameMap(StackLayout):
    '''Visual representaion of the Game.game_map dataframe. Displays the current game state to the user.
    
    Methods
    -------
    add_provinces()
        Adds ProvinceGraphic widgets to the GameMap based on the number of entries in the game_map dataframe.
    config_province()
        Instantiates ProvinceGraphic objects. Sets their color based on terrain and the controlling civ.
    '''
    
    def add_provinces(self):
        '''Adds ProvinceGraphic widgets to the GameMap based on the number of entries in the game_map dataframe.'''
        province_total = len(Game.game_map.index)
        for i in range(province_total):
            self.config_province()
    
    def config_province(self): 
        '''Instantiates ProvinceGraphic objects. Sets their color based on terrain and the controlling civ.'''
        #TODO -- make it so that province color changes on the controlling civ (will be useful 4 later fo sho)

        #The size of these widgets are important. Here, were optimizing the game to be a 200 province affair (10 high x 20 wide)
        province = ProvinceGraphic(_size_hint=(0.05, 0.1)) #FIXME -- this violates DI, idk how okay it is though ykyk?
        province.draw_province_rect()
        province.bind(pos=province.update_rect, size=province.update_rect)

        self.add_widget(province)

       
class ProvinceGraphic(Widget):
    '''Visual representaion of an individual province.'''
    def __init__(self, _size_hint, **kwargs):
        '''Instansiates the ProvinceGraphic class and the Widget superclass. 
        
        Parameters
        ----------
        _size_hint: collection<float>
            Can be list, tuple, etc. Represents the widget's dynamic size (Kivy size_hint property).
        '''

        #Calling super() to make sure the base Widget's canvas is defined. Removing this line results in an AttributeError.
        super().__init__(**kwargs)
        self.size_hint = _size_hint

    def draw_province_rect(self):
        '''"Colors" the province by drawing a rectangle that is the same size as the widget.'''

        with self.canvas:
            Color(.119, .221, .119)
            self.rect = Rectangle(pos=self.pos, size=self.size)
    
    def update_rect(self, instance, value):
        '''Method to ensure that the drawn rectangle reacts to changes in size and position. Code stolen from https://kivy.org/doc/stable/guide/widgets.html#adding-widget-background
        
        Parameters
        ----------
        instance: Widget
            The widget that owns the drawn rectangle
        value: float
            Represents the rectangle's new size/position values. Required param acessed via Kivy behind-the-scenes magic. 
            More info here: https://kivy.org/doc/stable/api-kivy.event.html
        '''
        
        instance.rect.pos = instance.pos 
        instance.rect.size = instance.size


if __name__ == '__main__':
    ChristoryApp().run()
