import json
from datetime import datetime
from GoogleApi.access_to_gs import append_data_to_gsheets


def json_to_gsheets(acc: str):
    with open('E:/INEVENTZ/TESTS/{0}/{0}.json'.format(acc), encoding='utf-8', newline='') as json_file:
        json_obj = json.load(json_file)
        json_file.close()
    for i in json_obj['GraphImages']:
        if len(i['edge_media_to_caption']['edges']):
            username = i['username']
            text = i['edge_media_to_caption']['edges'][0]['node']['text']
            link = "https://www.instagram.com/p/" + i['shortcode'] + "?utm_source=ig_web_copy_link"
            time_stamp_normal = datetime.utcfromtimestamp(int(i['taken_at_timestamp'])).strftime('%Y-%m-%d %H:%M:%S')
            time_stamp = int(i['taken_at_timestamp'])
            append_data_to_gsheets(time_stamp, time_stamp_normal, username, text, link)

list_of_accounts = ['wankymusic', 'delodesign', 'masa.neta', 'nana_dechire', 'testfm_radio', 'tancploshadka',
                   'mishka.bar', 'mishka.bar', 'napirelly', 'immediate_proximity', 'primitive_____',
                    'honealomer', 'sinusoidal_music', 'vityatsoy', 'rad__machine', 'luminous_bar']

for i in list_of_accounts:
    json_to_gsheets(i)

