from data import Game
import pandas as pd
import numpy as np

class TurnHandler:
    pass


class CivInitializer:
    #TODO -- create method that generates random spawn positions for each ov the civs
    #TODO -- add docs 4 me
    def generate_spawn_position(self):
        while True:
            civ_total = len(Game.civs.index)
            spawns = np.sort(np.random.randint(0, 800, size=civ_total))
            #Removing duplicates from spawns array by converting to a set. Sorting both so array_equal returns True regardless of number order.
            unique_spawns = np.sort(np.array(np.array(list(set(spawns)))))

            if np.array_equal(spawns, unique_spawns):
                break

        return spawns

