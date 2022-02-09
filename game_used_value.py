#!/home/l_vektor_m/venv3.8/bin/python
# coding: utf-8

# ルデヤ（https://kaitori-rudeya.com）のHPから
# 家庭用ゲーム機の買取価格を取得し
# csvファイルに保存する

import warnings
import datetime
from time import sleep
import requests
from bs4 import BeautifulSoup
import pandas

# warningが出ないようにする
warnings.filterwarnings('ignore')

# ゲームハードのカテゴリー
# 1:Nintendo Switch
# 2:PlayStation
# 3:Xbox
game_category = [1, 2, 3]
# 対象のid
# Switchグレー Switchネオン SwitchLiteターコイズ
Switch_category = ['focused2', 'focused3', 'focused7', 'focused1088', 'focused1087']
# PS5 PS5-DE
PlayStation_category = ['focused386', 'focused387']
# XboxSX XboxSS
Xbox_category = ['focused550', 'focused551']
id_sets = [Switch_category, PlayStation_category, Xbox_category]

# 現在日時
dt_now = datetime.datetime.now()
today = dt_now.strftime('%Y年%m月%d日')
now_hour = dt_now.strftime('%H時')

buy_price = {}
buy_price_value = {}

# ルデヤの買取ページのURL
rudeya_url = 'https://kaitori-rudeya.com/category/detail/{}'
for c in game_category:
    target_url = rudeya_url.format(c)
    response = requests.get(target_url, verify=False)
    sleep(1)
    soup = BeautifulSoup(response.text)

    buy_table = soup.find('table', {'class': 'kai_list_table mt30'})
    for id in id_sets[c-1]:
        focused_item = buy_table.find('tr', {'id': id})
        buy_price[id] = focused_item.find_all('td')[3].text.strip()
        buy_price_value[id] = buy_price[id].replace(',', '').replace('円', '')

game_price_dic = {
    'date': today,
    'hour': now_hour,
    'PlayStation5': buy_price[PlayStation_category[0]],
    'PlayStation5 DE': buy_price[PlayStation_category[1]],
    'XboxSX': buy_price[Xbox_category[0]],
    'XboxSS': buy_price[Xbox_category[1]],
    'Switchグレー': buy_price[Switch_category[0]],
    'Switchネオン': buy_price[Switch_category[1]],
    'SwitchLiteターコイズ': buy_price[Switch_category[2]],
    'Switch有機ELネオン': buy_price[Switch_category[3]],
    'Switch有機ELホワイト': buy_price[Switch_category[4]],
}

game_price_value_dic = {
    'date': today,
    'hour': now_hour,
    'PlayStation5': buy_price_value[PlayStation_category[0]],
    'PlayStation5 DE': buy_price_value[PlayStation_category[1]],
    'XboxSX': buy_price_value[Xbox_category[0]],
    'XboxSS': buy_price_value[Xbox_category[1]],
    'Switchグレー': buy_price_value[Switch_category[0]],
    'Switchネオン': buy_price_value[Switch_category[1]],
    'SwitchLiteターコイズ': buy_price_value[Switch_category[2]],
    'Switch有機ELネオン': buy_price_value[Switch_category[3]],
    'Switch有機ELホワイト': buy_price_value[Switch_category[4]],
}

# from pprint import pprint
# pprint(game_price_dic)
# pprint(game_price_value_dic)

enc = 'utf-8-sig'
csv_title_game_price = 'ルデヤでの各ゲーム機の買取値段推移.csv'
csv_title_game_price_value = 'ルデヤでの各ゲーム機の買取値段推移（値のみ）.csv'
columns_sort = ['date',
                'hour',
                'PlayStation5',
                'PlayStation5 DE',
                'Switch有機ELホワイト',
                'Switch有機ELネオン',
                'Switchネオン',
                'Switchグレー',
                'SwitchLiteターコイズ',
                'XboxSX',
                'XboxSS']

# 更新前のcsvファイルを読み込む
data_frame = pandas.read_csv(csv_title_game_price, header=0, encoding=enc)
last_column = data_frame.iloc[-1]

if last_column['date'] != today or last_column['hour'] != now_hour:
    # 読み込んだデータフレームに今回取得したデータを入れる
    add_data_frame = data_frame.append(game_price_dic, ignore_index=True)
    # 新規にデータフレームを作るので、項目でソートする
    add_data_frame.reindex(columns=columns_sort)
    # ファイルに書き込む
    add_data_frame.to_csv(csv_title_game_price, index=None, encoding=enc)

# 更新前のcsvファイルを読み込む
data_frame_value = pandas.read_csv(csv_title_game_price_value, header=0, encoding=enc)
last_column = data_frame_value.iloc[-1]

if last_column['date'] != today or last_column['hour'] != now_hour: 
    # 読み込んだデータフレームに今回取得したデータを入れる
    add_value_df = data_frame_value.append(game_price_value_dic, ignore_index=True)
    # 新規にデータフレームを作るので、項目でソートする
    add_value_df.reindex(columns=columns_sort)
    # ファイルに書き込む
    add_value_df.to_csv(csv_title_game_price_value, index=None, encoding=enc)