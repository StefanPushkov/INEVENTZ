from SCRAPPING.scrap_text import List, markup
from os import listdir
import os
from os.path import isfile, join
from TESTS.test import get_data_from_accounts
import pandas as pd
mypath = os.getcwd()+'\\'
print(mypath)
onlyfiles = [x for x in os.listdir(mypath)]
list_of_accounts = ['wankymusic', 'testfm_radio']
# list_of_accounts = ['wankymusic', 'delodesign', 'masa.neta', 'nana_dechire', 'testfm_radio', 'tancploshadka',
#                     'mishka.bar', 'mishka.bar', 'napirelly', 'immediate_proximity', 'primitive_____',
#                     'honealomer', 'sinusoidal_music', 'vityatsoy', 'rad__machine']
new_df = pd.DataFrame(columns=['text', 'label'])
list_of_df_names = []
print(onlyfiles)
for i in list_of_accounts:

    if i in onlyfiles:
        print("Already downloaded")
        print('Preprocessing data from {0}'.format(i))
        list_of_scripts_one_acc = List(i)
        labels = markup(list_of_scripts_one_acc)
        print('Create DataFrame from {0}'.format(i))
        df = pd.DataFrame(list(zip(list_of_scripts_one_acc, labels)), columns=['text', 'label'])
        # df.to_csv("E:/INEVENTZ/DATA/data_{0}.csv".format(i), index=None, header=True)
        new_df = pd.concat([new_df, df], ignore_index=True)
        continue
    print('Start download data from {0}'.format(i))
    get_data_from_accounts(i)
    print('Preprocessing data from {0}'.format(i))
    list_of_scripts_one_acc = List(i)
    labels = markup(list_of_scripts_one_acc)
    print('Create DataFrame from {0}'.format(i))
    df = pd.DataFrame(list(zip(list_of_scripts_one_acc, labels)), columns=['text', 'label'])
    # df.to_csv("E:/INEVENTZ/DATA/data_{0}.csv".format(i), index=None, header=True)
    new_df = pd.concat([new_df, df],ignore_index=True)


new_df.to_csv("E:/INEVENTZ/DATA/All_data.csv", index=None, header=True)