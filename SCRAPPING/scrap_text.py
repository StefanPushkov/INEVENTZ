import json
from pprint import pprint
import codecs
import pandas as pd
# fileObj = codecs.open('E:/SNES/main/wankymusic.json', "r", "utf_8_sig")
list_of_accounts = ['wankymusic', 'testfm_radio']
def List(acc):
    list_of_scripts_one_acc = []
    with codecs.open('E:/INEVENTZ/TESTS/{0}/{0}.json'.format(acc), "r", "utf_8_sig") as json_file:
        data = json.load(json_file)
        length = len(data["GraphImages"])
        for i in range(length):
            try:
                text = data["GraphImages"][i]["edge_media_to_caption"]["edges"][0]['node']["text"]
                list_of_scripts_one_acc.append(text)
                # if any(symbol.isdigit()for symbol in text):
                #    print('NEW \n\n'+text)
            except Exception as e:
                pass
        return list_of_scripts_one_acc


def markup(list_of_scripts_one_acc: list):
    labels = []
    for i in list_of_scripts_one_acc:
        if any(symbol.isdigit()for symbol in i) or "этот" in i or 'эту' in i:
            labels.append(1)
        else:
            labels.append(0)
    return labels


if __name__ == '__main__':
    for i in list_of_accounts:
        list_of_scripts = List(acc=i)
        labels = markup(list_of_scripts)
        df = pd.DataFrame(list(zip(list_of_scripts, labels)), columns=['text', 'label'])
        df.to_csv("E:/INEVENTZ/DATA/data.csv", index=None, header=True)
        print(df[df.label == 0])