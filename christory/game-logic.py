from data import Game
import pandas as pd
import numpy as np

class TurnHandler:
    pass


class CivInitializer:
    def give_pos_to_civs():
        spawns_x = list((np.random.randint(0, 800, size=100)))
        spawns_y = list(np.random.randint(0, 400, size=100))
        #TEst this plsss my uhh whats it called umm VS didnt work for some reason have 2 reinstall LOL!
        SpawnHolder = {
            "X": spawns_x,
            "Y": spawns_y
        }
        spawns = pd.DataFrame(SpawnHolder)
        with pd.ExcelWriter('Christory.xlsx',mode='a') as writer:  
            spawns.to_excel(writer, sheet_name='Spawns')
