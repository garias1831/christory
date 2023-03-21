#Misc test file using pytest (and maybe loggin' --> learn me); ignore me for game purposes

from data import Game
import pandas as pd
import numpy as np
import logging

LOGGER = logging.getLogger(__name__)

#Checking to see if we're actually setting the value of the df
def test_get_base_map():
    path = r'E:\code\python\kivy\christory\data\map-base.xlsx'
    df = pd.read_excel(path)
    Game.game_map = df


    #This log only gets shown by pytest if the directory name is specified, b/c thats how pytest looks for the .ini file

    LOGGER.warning(f'{Game.game_map}')

    assert Game.game_map.empty == False

def test_add_provinces():
        '''Adds ProvinceGraphic widgets to the GameMap based on the number of entries in the game_map dataframe.'''
        province_total = len(Game.game_map.index)
        for i in range(province_total):
            controller = Game.game_map.iloc[i]['controller']
            terrrain = Game.game_map.iloc[i]['terrain']
            LOGGER.warning(f'Controller:{controller}; Terrain:{terrrain}')
            #self.config_province()




def test_generate_spawn_position():
        while True:
            civ_total = 4
            spawns = np.sort(np.random.randint(0, 800, size=civ_total))
            unique_spawns = np.sort(np.array(np.array(list(set(spawns)))))

            LOGGER.warning(spawns)
            LOGGER.error(f'Filtered spawn list:{unique_spawns}')
            
            if np.array_equal(spawns, unique_spawns):
                break
            