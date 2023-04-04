#Misc test file using pytest (and maybe loggin' --> learn me); ignore me for game purposes

from data import Game
import pandas as pd
import pytest
import random as r
import numpy as np
import logging

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)


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


#Test for generate_spawn_potision method
def test_gsp():
    #setup data
    path = r'E:\code\python\kivy\christory\data\map-base.xlsx'
    df = pd.read_excel(path)

    land = df[df['terrain'] != 'ocean']
    LOGGER.warning(land.to_string())

    id_list =  land['id'].tolist()
    LOGGER.warning(f'List of ids: {[id_list]}')

    spawns = r.sample(id_list, 4)
    LOGGER.critical(f'Sample spawn: {spawns}')


def test_roll_colonization():
    pass


@pytest.mark.parametrize('target_id', [(50), (79), (39), (799)])
def test_get_adjacent_ids(target_id):
    ids = range(800)
    step = 40
    target = target_id

    id_map = [ids[x:x+step] for x in range(0, 800, step)]

    for i, row in enumerate(id_map):
         if target in row:
              rownum = i
              
    if target <= 39: #This ain't to hot in terms of DRY, but it works? #FIXME: there are better ways to do this
        adjacent_rows = id_map[rownum:rownum+2]
        start = adjacent_rows[0].index(target) - 1
        end = adjacent_rows[0].index(target) + 2
    elif target >= 760:
        adjacent_rows = id_map[rownum-1:rownum+1]
        start = adjacent_rows[1].index(target) - 1
        end = adjacent_rows[1].index(target) + 2
    else:
        adjacent_rows = id_map[rownum-1:rownum+2]
        start = adjacent_rows[1].index(target) - 1
        end = adjacent_rows[1].index(target) + 2
    
    #LOGGER.warning(f'adj row: {adjacent_rows}')
    
    adjacent_ids = [x[start:end] for x in adjacent_rows]

    LOGGER.debug(f'Target ID: {target}')
    LOGGER.debug(f'Adjacent ids: {adjacent_ids}')








'''
def test_generate_spawn_position():
        
        
        while True:
            civ_total = 4
            spawns = np.sort(np.random.randint(0, 800, size=civ_total))
            unique_spawns = np.sort(np.array(np.array(list(set(spawns)))))
            LOGGER.warning(spawns)
            LOGGER.error(f'Filtered spawn list:{unique_spawns}')
            
            if np.array_equal(spawns, unique_spawns):
                break
        '''