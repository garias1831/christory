from data import Game
import pandas as pd
import numpy as np
import random as r

class TurnHandler:
    
    def on_next_turn(self):
        chance = r.uniform(0, 1)
        

    def roll_colonization(self, civ): #TODO this function should probably have an event/callback to manipulate the UI, rather than a direcy call
        civs = Game.civs
        game_map = Game.game_map

        controlled_ids = game_map.loc[game_map.controller == civ]['id']

        #controlled_land = game_map[['controller'] == civ]
        #controlled_ids = controlled_land['id']
        #claimable_land = game_map[['controller'] == 'UNC']

    def find_adjacent_ids(self, target_id): #TODO -- document me
        ids = range(800)
        step = 40
        target = target_id

        id_map = [ids[x:x+step] for x in range(0, 800, step)]

        for i, row in enumerate(id_map):
            if target in row:
                rownum = i
        
        #Handling edge cases where the id is either on the top or bottom of the map.
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
                
        adjacent_ids = [x[start:end] for x in adjacent_rows]
        #Flattening adjacent_ids into a 1-D set containing all ids
        adjacent_ids = {x for ids in adjacent_ids for x in ids}

class CivInitializer:
    '''Utility class for initializing individual civ locations. and other things. (l8er?)
    Methods
    -------
    generate_spawn_position():
        ''Grabs random ids from non-ocean provinces to use as civ starting locations. 
    '''

    def generate_spawn_position(self):
        '''Grabs random ids from non-ocean provinces to use as civ starting locations. Modifies the map dataframe based on the generated spawns.
        Returns
        -------
        spawns: list<int>
            list of civ starting locations'''
        
        df = Game.game_map
        civs = Game.civs

        land = df[df['terrain'] != 'ocean']
        id_list =  land['id'].tolist()
        #Generating 4 civs
        spawns = r.sample(id_list, 4)

        #Setting the province controller in the df based on the spawns
        for i, spawn in enumerate(spawns): #There is probably a more elegant way to do this. Might want to look up some dataframe tips online
            civ = civs.iloc[i]['civ']   #Also there might b incentive to export this into another meth-od
            df.loc[df['id'] == spawn, 'controller'] = civ

        return spawns