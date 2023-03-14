#Misc test file using pytest (and maybe loggin' --> learn me); ignore me for game purposes

import data
import pandas as pd
import logging

#Checking to see if we're actually setting the value of the df
def test_get_base_map():
    path = r'E:\code\python\kivy\christory\data\map-base.xlsx'
    df = pd.read_excel(path)
    data.Game.game_map = df


    #This log only gets shown by pytest if the directory name is specified, b/c thats how pytest looks for the .ini file
    LOGGER = logging.getLogger(__name__)

    LOGGER.warning(f'{data.Game.game_map}')

    assert data.Game.game_map.empty == False

