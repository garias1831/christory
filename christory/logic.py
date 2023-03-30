from data import Game
import pandas as pd
import numpy as np
import random as r

class TurnHandler:
    def on_next_turn(self):
      chance = r.uniform(0, 1)
    def roll_colonization(self):
      df = Game.game_map
      claimable_land = df[df['controller'] == 'UNC']

class Akhil_Generator_Map:
    @staticmethod
    def Map_Generator_v2(length, How_Many_Rows):
        #NOTE: To add/ Chance terrain simply text me and ill add / subtract lickity split
        Terrain = []
#Lets me do a spinner and not have to rewrite it everytime (:
        def Do_Le_Randoms(Chance_of_Grass, Chance_of_Forest, Chance_of_Water):
            lerandom = r.randint(0,8)
            if lerandom <= Chance_of_Grass:
                Terrain.append("Grass")
            elif lerandom > Chance_of_Grass and lerandom <= Chance_of_Forest:
                Terrain.append("Forest")
            elif lerandom > Chance_of_Forest and lerandom <= Chance_of_Water:
                Terrain.append("Water")
        Do_Le_Randoms(4,6,8)
        x+=1
        Ignore = 1
        HowManyRowsCompleted = 0
        while (HowManyRowsCompleted != How_Many_Rows):
            try:
                if Terrain[x-length] == "Grass":
                    if Terrain[x-1] == "Grass":
                        Do_Le_Randoms(6,7,8)
                    elif Terrain[x-1] == "Forest":
                        Do_Le_Randoms(4,7,8)
                    elif Terrain[x-1] == "Water":
                        Do_Le_Randoms(4,5,8)
                    x+=1
                elif Terrain[x-length] == "Water":
                    if Terrain[x-1] == "Grass":
                        Do_Le_Randoms(3,4,8)
                    elif Terrain[x-1] == "Forest":
                        Do_Le_Randoms(1,4,8)
                    elif Terrain[x-1] == "Water":
                        Do_Le_Randoms(1,2,8)
                    x+=1
                elif Terrain[x-length] == "Forest":
                    if Terrain[x-1] == "Grass":
                        Do_Le_Randoms(3,7,8)
                    elif Terrain[x-1] == "Forest":
                        Do_Le_Randoms(1,7,8)
                    elif Terrain[x-1] == "Water":
                        Do_Le_Randoms(1,5,8)
                    x+=1
                if (length * Ignore) <= x:
                    HowManyRowsCompleted += 1
                    Ignore += 1
            except IndexError:
                if Terrain[x-1] == "Grass":
                    Do_Le_Randoms(4,6,8)
                elif Terrain[x-1] == "Water":
                    Do_Le_Randoms(2,4,8)
                elif Terrain[x-1] == "Forest":
                    Do_Le_Randoms(2,6,8)
                x+=1
                if (length * Ignore) <= x:
                    HowManyRowsCompleted += 1
                    Ignore += 1
        return Terrain
   
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
        spawns = r.sample(id_list, 4) 

        return spawns


