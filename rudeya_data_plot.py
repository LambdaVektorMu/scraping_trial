#!/home/l_vektor_m/venv3.8/bin/python
# coding: utf-8

import matplotlib.pyplot as plot
import pandas

# csvファイルをデータフレームに格納する
enc = 'utf-8-sig'
csv_title_game_price_value = 'ルデヤでの各ゲーム機の買取値段推移（値のみ）.csv'
data_frame = pandas.read_csv(csv_title_game_price_value, header=0, encoding=enc)

FIG_W = 75
plot.rcParams["figure.figsize"] = (FIG_W, 5)

fig = plot.figure()

#各ゲーム機の買取価格を1時間ごとにプロット
plot.plot(data_frame['date']+data_frame['hour'], data_frame['PlayStation5'], '.-b', label='PS5')
plot.plot(data_frame['date']+data_frame['hour'], data_frame['PlayStation5 DE'], '.-g', label='PS5DE')
#plot.plot(data_frame['date']+data_frame['hour'], data_frame['Switchグレー'], '.-k', label='Switch Gray')

# 日付（x軸）の目盛り表示を見やすくする
xlabel_list = (data_frame['date']+data_frame['hour']).to_list()
# 日本語を抜いて簡略表示
plot_xlabel_list = [l.replace('2021年', '').replace('月', '/').replace('日', ' ') for l in xlabel_list]
# 12時間毎に表示
PER = 24
print(len(plot_xlabel_list), plot_xlabel_list)
days = len(plot_xlabel_list)//PER
print(days)
days_plot = [d*PER+3 for d in range(days)]
print(days_plot)
label_list = [plot_xlabel_list[days_plot[ll]] for ll in range(days) if days_plot[ll] < len(plot_xlabel_list)]
print(label_list)
FONT_SIZE=5
plot.xticks(days_plot, label_list, fontsize=FONT_SIZE)
plot.xlim(left=-5)
plot.legend()

plot.title('ルデヤ買取価格')
plot.ylabel('価格（円）')
plot.xlabel('日時')
plot.savefig('rudeya_PS5BR-PS5DE.png', bbox_inches='tight', pad_inches=0)
plot.close()

fig = plot.figure()
plot.plot(data_frame['date']+data_frame['hour'], data_frame['PlayStation5'], '.-b', label='PS5')
plot.xticks(days_plot, label_list, fontsize=FONT_SIZE)
plot.xlim(left=-5)
plot.legend()
plot.title('ルデヤ買取価格')
plot.ylabel('価格（円）')
plot.xlabel('日時')
plot.savefig('rudeya_PS5BR.png', bbox_inches='tight', pad_inches=0)
plot.close()

fig = plot.figure()
plot.plot(data_frame['date']+data_frame['hour'], data_frame['PlayStation5 DE'], '.-g', label='PS5DE')
plot.xticks(days_plot, label_list, fontsize=FONT_SIZE)
plot.xlim(left=-5)
plot.legend()
plot.title('ルデヤ買取価格')
plot.ylabel('価格（円）')
plot.xlabel('日時')
plot.savefig('rudeya_PS5DE.png', bbox_inches='tight', pad_inches=0)
plot.close()

fig = plot.figure()
plot.plot(data_frame['date']+data_frame['hour'], data_frame['Switchグレー'], '.-k', label='Switch Gray')
plot.xticks(days_plot, label_list, fontsize=FONT_SIZE)
plot.xlim(left=-5)
plot.legend()
plot.title('ルデヤ買取価格')
plot.ylabel('価格（円）')
plot.xlabel('日時')
plot.savefig('rudeya_Switch_G.png', bbox_inches='tight', pad_inches=0)
plot.close()

fig = plot.figure()
plot.plot(data_frame['date']+data_frame['hour'], data_frame['Switchネオン'], '.-r', label='Switch Neon')
plot.xticks(days_plot, label_list, fontsize=FONT_SIZE)
plot.xlim(left=-5)
plot.legend()
plot.title('ルデヤ買取価格')
plot.ylabel('価格（円）')
plot.xlabel('日時')
plot.savefig('rudeya_Switch_N.png', bbox_inches='tight', pad_inches=0)
plot.close()

fig = plot.figure()
plot.plot(data_frame['date']+data_frame['hour'], data_frame['Switchグレー'], '.-k', label='Switch Gray')
plot.plot(data_frame['date']+data_frame['hour'], data_frame['Switchネオン'], '.-r', label='Switch Neon')
plot.xticks(days_plot, label_list, fontsize=FONT_SIZE)
plot.xlim(left=-5)
plot.legend()
plot.title('ルデヤ買取価格')
plot.ylabel('価格（円）')
plot.xlabel('日時')
plot.savefig('rudeya_Switch.png', bbox_inches='tight', pad_inches=0)
plot.close()

fig = plot.figure() #plot.figure(figsize=(FIG_W//3, 5))
plot.plot(data_frame['date']+data_frame['hour'], data_frame['Switch有機ELホワイト'], '.-c', label='SwitchOLED White')
plot.plot(data_frame['date']+data_frame['hour'], data_frame['Switch有機ELネオン'], '.-m', label='SwitchOLED Neon')
plot.xticks(days_plot, label_list, fontsize=FONT_SIZE)
plot.xlim(left=1495)
plot.legend()
plot.title('ルデヤ買取価格')
plot.ylabel('価格（円）')
plot.xlabel('日時')
plot.savefig('rudeya_SwitchOLED.png', bbox_inches='tight', pad_inches=0)
plot.close()
