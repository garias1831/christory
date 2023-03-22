from data import Game
import pandas as pd
import numpy as np
import random as r

class TurnHandler:
    pass


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
        land = df[df['terrain'] != 'ocean']
        id_list =  land['id'].tolist()
        #Generating 4 civs
        #this input is a placeholder. TODO!!! Add slider or smthn that can do this 
        civ_total = input("how many civs")
        spawns = r.sample(id_list, civ_total) 

        return spawns


