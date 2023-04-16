from config.definitions import ROOT_DIR
from data import Game
from logic import CivInitializer, TurnHandler
from kivy.app import App
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.graphics import Color, Rectangle, Line
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window
import os
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

    def get_base_data(self):
        '''Gets the base map and civ sheets and stores them as dataframes. Called when user presses the 'New Game' button on the UI.'''

        path = os.path.join(ROOT_DIR, 'data', 'map-base.xlsx')
        map_df = pd.read_excel(path)
        Game.game_map = map_df.copy() #idk if copy is neccesary but like sure

        path = os.path.join(ROOT_DIR, 'data', 'civs-base.xlsx')
        civs_df = pd.read_excel(path)
        Game.civs = civs_df.copy() 


class MainGameScreen(Screen):
    '''Represents the window where the game will actually be played.'''
    
    def on_next_turn(self):
        TurnHandler().on_next_turn()


class GameMap(StackLayout):
    '''Visual representaion of the Game.game_map dataframe. Displays the current game state to the user.
    
    Methods
    -------
    add_provinces()
        Adds ProvinceGraphic widgets to the GameMap based on the number of entries in the game_map dataframe.
    add civs()
        Colors in existing provinces to represent randomized civ spawns.
    config_province()
        Instantiates ProvinceGraphic objects. Sets their color based on terrain and the controlling civ.
    '''
    
    #TODO use self.children to access the individual provinces


    def add_provinces(self): #TODO -- it probably makes sense to do a setup typa method just to be a little more clear (if complex)... just a method w calls to add province and add civ
        '''Adds ProvinceGraphic widgets to the GameMap based on the number of entries in the game_map dataframe. Called by entering the MainGameScreen.'''
        province_total = len(Game.game_map.index)
        for i in range(province_total):
            #Grabbing the respective values from the map-base excel sheet. 
            terrain = Game.game_map.iloc[i]['terrain']
            self.config_province(terrain) #TODO - remove unused params 
        #self.children.sort(key=lambda x: x.id, reverse=True) #maybe sorting this works? but not really?
        self.add_civs()
    
    def config_province(self, terrain): 
        '''Instantiates ProvinceGraphic objects. Sets their color based on terrain and the controlling civ.'''
        #TODO -- make it so that province color changes on the controlling civ (will be useful 4 later fo sho)

        #The size of these widgets are important. Here, were optimizing the game to be a 800 province affair (20 high x 40 wide)
        province = ProvinceGraphic(_size_hint=(0.025, 0.05)) #FIXME -- this violates DI, idk how okay it is though ykyk?
        color = province.get_terrain_color(terrain)
        province.draw_province_rect(color)
        province.bind(pos=province.update_rect, size=province.update_rect)

        self.add_widget(province)
    
    def add_civs(self):
        '''Colors in existing provinces to represent randomized civ spawns.''' 
        spawns = CivInitializer().generate_spawn_position()
        for i, spawn in enumerate(spawns):
            civ = Game.civs.iloc[i]['civ']
            province = self.get_province(spawn)
            province.set_civ_color(civ)

    def get_province(self, _id):
        '''Selects a province from the children list.
        Parameters
        ----------
        _id: int
            id of the province to select
        Returns
        -------
        province: ProvinceGraphic
            See ProvinceGraphic class for more info
        '''
        
        #Widgets in self.children are stored front-to-back even though we insert them back-to-front.
        #See this: https://github.com/kivy/kivy/issues/2895
        children = self.children[:]
        children.reverse()
        #The province's id and index in the list are equal
        province = children[_id]
        
        return province


   
        
       
class ProvinceGraphic(Widget):
    '''Visual representaion of an individual province.
    Methods
    -------
    draw_province_rect(color)
        "Colors" the province by drawing a rectangle that is the same size as the widget.
    set_civ_color(civ) 
        Sets the province's color based on the controlling civ.
    get_terrain_color(controller, terrain)
        Returns an RGB color depending on the terrain and controlling civ.
    update_rect(instance, value)
        Method to ensure that the drawn rectangle reacts to changes in size and position.
    '''

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

    def draw_province_rect(self, color):
        '''"Colors" the province by drawing a rectangle that is the same size as the widget.
        Parameters
        ----------
        color: tuple/list<float>
            Tuple or list representing an RGB color code.
        '''

        r, g, b = color
        with self.canvas:
            self.canvas.clear()
            Color(r, g, b)
            self.rect = Rectangle(pos=self.pos, size=self.size)

    def set_civ_color(self, civ): #TODO -- probably want province param for modifying province; also change name to set_civ color maybe?
        '''Sets the province's color based on the controlling civ.
        Parameters
        ----------
        civ: str
            Three-letter string identifier for the civ controlling the province. 
        '''

        df = Game.civs
        #Thank you https://towardsdatascience.com/dealing-with-list-values-in-pandas-dataframes-a177e534f173
        color = df.loc[df['civ'] == civ]['color'].apply(eval).to_list()[0] 
        color = list(map(eval, color))
        self.draw_province_rect(color)

    def get_terrain_color(self, terrain): #FIXME -- controller isn't needed here, can probably remove
        '''Returns an RGB color depending on the province terrain.
            
        Parameters
        ----------
        terrain: str
            The terrain of the province being drawn.
        Returns
        ---------
        tuple<float>
            Tuple representing an RGB color code.
        '''

        if terrain == 'ocean':
            return (58/255, 179/255, 218/255) #TODO -- this color is kinda bright and annoying, but i'll see how i feel abt it
        elif terrain == 'desert':
            return (227/255, 167/255, 36/255)
        elif terrain == 'grasslands':
            return (128/255, 199/255, 31/255)
        elif terrain == 'forest':
            return (103/255, 117/255, 53/255)
        elif terrain == 'hills':
            return (62/255, 92/255, 32/255)
        elif terrain == 'mountains':
            return (156/255, 157/255, 151/255)

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
    #Window.fullscreen = 'auto' #FIXME -- makes the window fullscreen , but can't windows button out of it. Add a button in .kv to kill the application / exit
    ChristoryApp().run()