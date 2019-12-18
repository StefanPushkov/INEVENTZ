import json
from pprint import pprint
import codecs
# fileObj = codecs.open('E:/SNES/main/wankymusic.json', "r", "utf_8_sig")

with codecs.open('E:/SNES/main/shtephqn.json', "r", "utf_8_sig") as json_file:
    data = json.load(json_file)
    length = len(data["GraphImages"])
    for i in range(length):
        try:
            text = data["GraphImages"][i]["edge_media_to_caption"]["edges"][0]['node']["text"]
            print('NEW \n\n'+text)
        except Exception as e:
            pass