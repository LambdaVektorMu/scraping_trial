#!/home/l_vektor_m/venv3.8/bin/python
# coding: utf-8

import matplotlib.pyplot as plot
import pandas

# csvファイルをデータフレームに格納する
enc = 'utf-8-sig'
csv_title_game_price = 'ebayでの各ゲーム機の売値推移.csv'
data_frame = pandas.read_csv(csv_title_game_price, header=0, encoding=enc)

FONT_SIZE=6  # グラフのフォントサイズ
FIG_W = 14  # グラフの横の大きさ
# 日付（x軸）の目盛り表示を見やすくする
xlabel_list = (data_frame['date']+data_frame['hour']).to_list()
# 日本語を抜いて簡略表示
plot_xlabel_list = [l.replace('2021年', '').replace('月', '/').replace('日', ':') for l in xlabel_list]
# 12時間毎に表示
print('横軸目盛り:', len(plot_xlabel_list), plot_xlabel_list)
days = len(plot_xlabel_list)//12
days_plot = [d*12+1 for d in range(days)]
print('横軸目盛りラベル:', days, days_plot)
label_list = [plot_xlabel_list[days_plot[ll]] for ll in range(days) if days_plot[ll] < len(plot_xlabel_list)]
print('表示されるラベル', label_list)

fig = plot.figure()
fig.set_figwidth(FIG_W)
#各ゲーム機の買取価格を1時間ごとにプロット
plot.plot(data_frame['date']+data_frame['hour'], data_frame['PS5_price_value'], '.-b', label='PS5')
plot.xticks(days_plot, label_list, fontsize=FONT_SIZE)
plot.legend()
plot.title('ebay売値価格')
plot.ylabel('価格（円）')
plot.xlabel('日時')
plot.savefig('ebay_PS5BR.png')
plot.close()

fig = plot.figure()
fig.set_figwidth(FIG_W)
plot.plot(data_frame['date']+data_frame['hour'], data_frame['PS5DE_price_value'], '.-g', label='PS5DE')
plot.xticks(days_plot, label_list, fontsize=FONT_SIZE)
plot.legend()
plot.title('ebay売値価格')
plot.ylabel('価格（円）')
plot.xlabel('日時')
plot.savefig('ebay_PS5DE.png')
plot.close()

fig = plot.figure()
fig.set_figwidth(FIG_W)
plot.plot(data_frame['date']+data_frame['hour'], data_frame['PS5_price_value'], '.-b', label='PS5')
plot.plot(data_frame['date']+data_frame['hour'], data_frame['PS5DE_price_value'], '.-g', label='PS5DE')
plot.xticks(days_plot, label_list, fontsize=FONT_SIZE)
plot.legend()
plot.title('ebay売値価格')
plot.ylabel('価格（円）')
plot.xlabel('日時')
plot.ylim(55000, 105000)
plot.savefig('ebay_PS5BR-DE.png')
plot.close()

fig = plot.figure()
fig.set_figwidth(FIG_W)
plot.scatter(data_frame['date']+data_frame['hour'], data_frame['PS5_price_value'], c='b', label='PS5')
plot.scatter(data_frame['date']+data_frame['hour'], data_frame['PS5DE_price_value'], c='g', label='PS5DE')
plot.xticks(days_plot, label_list, fontsize=FONT_SIZE)
plot.legend()
plot.title('ebay売値価格')
plot.ylabel('価格（円）')
plot.xlabel('日時')
plot.ylim(55000, 105000)
plot.savefig('ebay_scatter_PS5BR-DE.png')
plot.close()
