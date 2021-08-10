#!/home/l_vektor_m/venv3.8/bin/python
# coding: utf-8

# ebay（https://www.ebay.com）のHPから
# 家庭用ゲーム機の売値を取得し
# csvファイルに保存する

import warnings
import datetime
from time import sleep
import requests
from bs4 import BeautifulSoup
import pandas

# warningが出ないようにする
warnings.filterwarnings('ignore')

# 現在日時
dt_now = datetime.datetime.now()
today = dt_now.strftime('%Y年%m月%d日')
now_hour = dt_now.strftime('%H時')

# ebayの各ゲームハードのURL
ebay_PS5BR_url = 'https://www.ebay.com/b/Sony-PlayStation-5-Blu-Ray-Edition-Video-Game-Consoles/139971/bn_7117588355?rt=nc&_sop=1'
ebay_PS5DE_url = 'https://www.ebay.com/b/Sony-PlayStation-5-Digital-Edition-Video-Game-Consoles/139971/bn_7117625199?rt=nc&_sop=1'
ebay_Switch_url = 'https://www.ebay.com/b/Video-Game-Home-Consoles/139971/bn_27305094?Model=Nintendo%2520Switch&rt=nc&_sop=1&mag=1'
ebay_XboxSX_url = 'https://www.ebay.com/b/Microsoft-Xbox-Series-X-Video-Game-Consoles/139971/bn_7117574288?rt=nc&_sop=1'
ebay_XboxSS_url = 'https://www.ebay.com/b/Microsoft-Xbox-Series-S-Video-Game-Consoles/139971/bn_7117578289?rt=nc&_sop=1'
# 調査対象のゲームハード
game_consoles = ['PS5BR', 'PS5DE', 'Switch', 'XboxSX', 'XboxSS']
# ゲームハードとURLの紐付け
url_dict = {game_consoles[0]: ebay_PS5BR_url,
            game_consoles[1]: ebay_PS5DE_url,
            game_consoles[2]: ebay_Switch_url,
            game_consoles[3]: ebay_XboxSX_url,
            game_consoles[4]: ebay_XboxSS_url
}

title_item = {}
price = {}
bids = {}

for gc in game_consoles:
    response = requests.get(url_dict[gc])
    sleep(1)
    soup = BeautifulSoup(response.text)

    buy_table = soup.find('ul', {'class': 'b-list__items_nofooter srp-results srp-grid'})
    buy_items = buy_table.find_all('li', {'class': 's-item s-item--large s-item--bgcolored'})

    for it in buy_items:
        bids_item = it.find('span', {'class': 's-item__bids s-item__bidCount'}).text
        bids[gc] = int(bids_item.rstrip(' bids'))
        if bids[gc] < 1: continue
        else:
            title_item[gc] = it.find('h3', {'class': 's-item__title'}).text
            price[gc] = it.find('span', {'class': 's-item__price'}).text
            break

game_price_dict = {
    'date': today,
    'hour': now_hour,
    # PS5BRの情報
    'PS5_title': title_item[game_consoles[0]],
    'PS5_price': price[game_consoles[0]],
    'PS5_price_value': price[game_consoles[0]].replace(',', '').replace(' 円', ''),
    'PS5_bids': bids[game_consoles[0]],
    # PS5DEの情報
    'PS5DE_title': title_item[game_consoles[1]],
    'PS5DE_price': price[game_consoles[1]],
    'PS5DE_price_value': price[game_consoles[1]].replace(',', '').replace(' 円', ''),
    'PS5DE_bids': bids[game_consoles[1]],
    # Nintendo Switchの情報
    'Switch_title': title_item[game_consoles[2]],
    'Switch_price': price[game_consoles[2]],
    'Switch_price_value': price[game_consoles[2]].replace(',', '').replace(' 円', ''),
    'Switch_bids': bids[game_consoles[2]],
    # XboxSX/Sの情報
    'XboxSX_title': title_item[game_consoles[3]],
    'XboxSX_price': price[game_consoles[3]],
    'XboxSX_price_value': price[game_consoles[3]].replace(',', '').replace(' 円', ''),
    'XboxSX_bids': bids[game_consoles[3]],
    'XboxSS_title': title_item[game_consoles[4]],
    'XboxSS_price': price[game_consoles[4]],
    'XboxSS_price_value': price[game_consoles[4]].replace(',', '').replace(' 円', ''),
    'XboxSS_bids': bids[game_consoles[4]],
}

# csv情報を更新する
enc = 'utf-8-sig'
csv_title_game_price = 'ebayでの各ゲーム機の売値推移.csv'
columns_sort = [
    'date',
    'hour',
    'PS5_title',
    'PS5_price',
    'PS5_price_value',
    'PS5_bids',
    'PS5DE_title',
    'PS5DE_price',
    'PS5DE_price_value',
    'PS5DE_bids',
    'Switch_title',
    'Switch_price',
    'Switch_price_value',
    'Switch_bids',
    'XboxSX_title',
    'XboxSX_price',
    'XboxSX_price_value',
    'XboxSX_bids',
    'XboxSS_title',
    'XboxSS_price',
    'XboxSS_price_value',
    'XboxSS_bids',
]

#dataframe = pandas.DataFrame([game_price_dict])
#dataframe.reindex(columns=columns_sort)
#dataframe.to_csv(csv_title_game_price, index=None, encoding=enc)

# 更新前のcsvファイルを読み込む
data_frame = pandas.read_csv(csv_title_game_price, header=0, encoding=enc)
# 読み込んだデータフレームに今回取得したデータを入れる
add_data_frame = data_frame.append(game_price_dict, ignore_index=True)
# 新規にデータフレームを作るので、項目でソートする
add_data_frame.reindex(columns=columns_sort)
# ファイルに書き込む
add_data_frame.to_csv(csv_title_game_price, index=None, encoding=enc)
