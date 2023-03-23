from data import Game
import pandas as pd
import numpy as np
import random as r

class TurnHandler:
    pass
class Procedural_Map_Generator_v1
    def build_map(length, Height):
        Terrain = []
        #I know this is HORRRIBLE too lasy to fix TODO but it doesnt hurt anyone. Valve code, anyone?
        #Also, this might pull up an indent eeror. Havent tested it outside of repl. Pls address
        #To add or subtract terrain you have to add it here and in the places where it gets the terrain & add more to the randint and figure out how to that balances. Sorry.
        #Lets me do a spinner and not have to rewrite it everytime (:
        def Do_Le_Randoms(Chance_of_Grass, Chance_of_Forest, Chance_of_Water):
            lerandom = r.randint(0,4)
            if lerandom <= Chance_of_Grass:
                Terrain.append("Grass")
            elif lerandom > Chance_of_Grass and lerandom <= Chance_of_Forest:
                Terrain.append("Forest")
            elif lerandom > Chance_of_Forest and lerandom <= Chance_of_Water:
                Terrain.append("Water")
            Do_Le_Randoms(2,3,4)
        x+=1
        Ignore = 1
        HowManyRowsCompleted = 0
        while (HowManyRowsCompleted != Height):
            try:
                if Terrain[x-length] == "Grass":
                    Do_Le_Randoms(2,3,4)
                    x+=1
                elif Terrain[x-length] == "Water":
                    Do_Le_Randoms(1,2,4)
                    x+=1
                elif Terrain[x-length] == "Forest":
                    Do_Le_Randoms(1,3,4)
                    x+=1
                if (length * Ignore)< x:
                    HowManyRowsCompleted += 1
                    Ignore += 1
            except IndexError:
                #Todo Make it where teh uhhh procedural generation is more influenced by the one behind it. IDK, seems kinda important lol.
                if Terrain[x-1] == "Grass":
                    Do_Le_Randoms(2,3,4)
                    x+=1
                elif Terrain[x-1] == "Water":
                    Do_Le_Randoms(1,2,4)
                    x+=1
                elif Terrain[x-1] == "Forest":
                    Do_Le_Randoms(1,3,4)
                    x+=1
                if (length * Ignore)< x:
                    HowManyRowsCompleted += 1
                    Ignore += 1
        TerrainDataframe = pd.DataFrame(Terrain, columns=['Terrain'])
  
# print dataframe.
df

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


