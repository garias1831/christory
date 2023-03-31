from data import Game
import pandas as pd
import numpy as np
import random as r

class TurnHandler:
    
    def on_next_turn(self):
        chance = r.uniform(0, 1)
        

    def roll_colonization(self, civ):
        civs = Game.civs
        game_map = Game.game_map

        controlled_land = game_map[['controller'] == civ]
        controlled_ids = controlled_land['id']
        #claimable_land = game_map[['controller'] == 'UNC']

    def find_adjacent_ids(self, id):
        id_map = np.arange(800)
        id_map.split(20) #FIXME -- these loops arent neccesarry! slices are nice!

class CivInitializer:
    '''Utility class for initializing individual civ locations. and other things. (l8er?)
    Methods
    -------
    generate_spawn_position():
        ''Grabs random ids from non-ocean provinces to use as civ starting locations. 
    '''

    def generate_spawn_position(self):
        '''Grabs random ids from non-ocean provinces to use as civ starting locations.
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
            df['controller'].loc[df['id'] == spawn] = civ

        print(df.to_string())
            


        return spawns


