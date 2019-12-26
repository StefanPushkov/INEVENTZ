import json
from pprint import pprint
import codecs
import pandas as pd
# fileObj = codecs.open('E:/SNES/main/wankymusic.json', "r", "utf_8_sig")

def List():
    with codecs.open('E:/INEVENTZ/main/wankymusic.json', "r", "utf_8_sig") as json_file:
        list_of_scripts = []
        data = json.load(json_file)
        length = len(data["GraphImages"])
        for i in range(length):
            try:
                text = data["GraphImages"][i]["edge_media_to_caption"]["edges"][0]['node']["text"]
                list_of_scripts.append(text)
                # if any(symbol.isdigit()for symbol in text):
                #    print('NEW \n\n'+text)
            except Exception as e:
                pass
        return list_of_scripts

list_of_scripts = List()

def markup():
    labels = []
    for i in list_of_scripts:
        if any(symbol.isdigit()for symbol in i) or "этот" in i or 'эту' in i:
            labels.append(1)
        else:
            labels.append(0)
    return labels

labels = markup()
df = pd.DataFrame(list(zip(list_of_scripts, labels)), columns=['text', 'label'])
df.to_csv("E:/INEVENTZ/DATA/data.csv", index=None, header=True)
print(df[df.label == 0])