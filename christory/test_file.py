'''Misc test file using pytest (and maybe loggin' --> learn me); ignore me for game purposes'''
from config.definitions import ROOT_DIR
from data import Game
import pandas as pd
import pytest
import random as r
import numpy as np
import logging
import os

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

@pytest.fixture
def df_setup():
    '''Test fixture to read the map-base and civs-base xlsx files'''
    path = os.path.join(ROOT_DIR, 'data', 'map-base.xlsx')
    map_df = pd.read_excel(path)

    path = os.path.join(ROOT_DIR, 'data', 'civs-base.xlsx')
    civs_df = pd.read_excel(path)

    return map_df, civs_df

@pytest.fixture
def random_spawn_setup(df_setup):
    '''Grabs random ids from non-ocean provinces to use as civ starting locations. Modifies the map dataframe based on the generated spawns.
        Returns
        -------
        spawns: list<int>
            list of civ starting locations'''
    
    df, civs = df_setup

    land = df[df['terrain'] != 'ocean']
    id_list =  land['id'].tolist()
    #Generating 4 civs
    spawns = r.sample(id_list, 4)

    #Setting the province controller in the df based on the spawns
    for i, spawn in enumerate(spawns): #There is probably a more elegant way to do this. Might want to look up some dataframe tips online
        civ = civs.iloc[i]['civ']   #Also there might b incentive to export this into another meth-od
        #df['controller'].loc[df['id'] == spawn] = civ
        df.loc[df['id'] == spawn, 'controller'] = civ

    return df, civs



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



@pytest.mark.parametrize('civ', [('FRA')]) 
def test_roll_colonization(random_spawn_setup, civ):
    map_df, civs_df = random_spawn_setup

    controlled_land = map_df.loc[map_df.controller == civ]
    LOGGER.info(controlled_land)
    ''' Set of ids outlining the civ's owned provinces.
        If the civ looks like so: (empty space denoted by #, civ at position X)
        # # # #
        # # X #
        # # # #

        The set will contain these province ids: (O denotes outline)
        # O O O
        # O X O
        # O O O
    '''
    all_ids = set()
    for target in controlled_land['id']: #This is very inefficient. The call to get adjacent ids should not occur if all the adjacent ids
        adjacent_ids = get_adjacent_ids(target)
        all_ids.update(adjacent_ids)
        #TODO -- put an if here to grab only the adjacent uncolonized provinces
        LOGGER.debug(f'Target province: {target}; Adjacent ids: {adjacent_ids}')

    uncolonized_df = map_df.loc[map_df['controller'] == 'UNC']
    #If the given id is uncolonized, add it to the list of colonizable ids.
    colonizable_ids = uncolonized_df[uncolonized_df['id'].isin(all_ids)].id # pd.Series of all the province ids
    LOGGER.info(f'Colonizable ids: {colonizable_ids}')

    #LOGGER.info(f'uncolonized df\n: {uncolonized_df.to_string()}')



    #adjacent_ids = {adjacent_ids.union(test_get_adjacent_ids()) for x in map_df['id']}
    #LOGGER.debug(f'Adjacent ID set: {colonizable_ids}')



    


@pytest.mark.parametrize('target_id', [(50), (79), (39), (799)])
def test_get_adjacent_ids(target_id):
    ids = range(800)
    step = 40
    target = target_id

    id_map = [ids[x:x+step] for x in range(0, 800, step)]

    for i, row in enumerate(id_map):
         if target in row:
              rownum = i
              
    if target <= 39: #This ain't to hot in terms of DRY, but it works? #FIXME: there are better ways to do this, maybe more pandas-centric
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

    #Flattening adjacent_ids into a 1-D set
    adjacent_ids = {x for ids in adjacent_ids for x in ids}

    LOGGER.debug(f'Target ID: {target}')
    LOGGER.debug(f'Adjacent ids: {adjacent_ids}')

    #return adjacent_ids

def get_adjacent_ids(target_id):
    ids = range(800)
    step = 40
    target = target_id

    id_map = [ids[x:x+step] for x in range(0, 800, step)]

    for i, row in enumerate(id_map):
         if target in row:
              rownum = i
              
    if target <= 39: #This ain't to hot in terms of DRY, but it works? #FIXME: there are better ways to do this, maybe more pandas-centric
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

    #Flattening adjacent_ids into a 1-D set
    adjacent_ids = {x for ids in adjacent_ids for x in ids}

    return adjacent_ids
