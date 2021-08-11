#!/home/l_vektor_m/venv3.8/bin/python
# coding: utf-8

import matplotlib.pyplot as plot
import pandas

# csvファイルをデータフレームに格納する
enc = 'utf-8-sig'
csv_title_game_price_value = 'ルデヤでの各ゲーム機の買取値段推移（値のみ）.csv'
data_frame = pandas.read_csv(csv_title_game_price_value, header=0, encoding=enc)

plot.figure()

#各ゲーム機の買取価格を1時間ごとにプロット
plot.plot(data_frame['date']+data_frame['hour'], data_frame['PlayStation5'], '.-b', label='PS5')
plot.plot(data_frame['date']+data_frame['hour'], data_frame['PlayStation5 DE'], '.-g', label='PS5DE')
#plot.plot(data_frame['date']+data_frame['hour'], data_frame['Switchグレー'], '.-k', label='Switch Gray')

# 日付（x軸）の目盛り表示を見やすくする
xlabel_list = (data_frame['date']+data_frame['hour']).to_list()
# 日本語を抜いて簡略表示
plot_xlabel_list = [l.replace('2021年', '').replace('月', '/').replace('日', '/').strip('時') for l in xlabel_list]
# 12時間毎に表示
days = len(plot_xlabel_list)//12 + 1
days_plot = [d*12+3 for d in range(days)]
label_list = [plot_xlabel_list[days_plot[ll]] for ll in range(days)]
plot.xticks(days_plot, label_list, fontsize=8)
plot.legend()

plot.savefig('rudeya.png')
plot.close()
