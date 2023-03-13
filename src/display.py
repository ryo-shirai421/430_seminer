import itertools
import math
import datetime

import seaborn as sns
import csv

import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as patches
from matplotlib import animation
import japanize_matplotlib
from get_status import get_status


status_arr = [0]
dt_past = []
dt_past.append(datetime.datetime.now())


def tail(fn):
    # ファイルを開いてすべての行をリストで取得する
    with open(fn, 'r') as f:
        # 一行読む. 一行目はヘッダーだから結果は捨てる
        f.readline()

        # 全行読む
        lines = f.readlines()

    # 最後の１行だけ
    return lines[-1:]


# 描画の設定
fig, (ax1, ax2, ax3, ax4) = plt.subplots(
    4, 1, gridspec_kw={'height_ratios': [1, 1, 2, 1]})
plt.subplots_adjust(hspace=1.0)

# カラーバーの描画
tempbar = np.arange(10, 40.1, 0.1).reshape((1, 301))
sns.heatmap(tempbar, cmap='YlOrRd', vmin=10, vmax=40, ax=ax2,
            cbar=False, yticklabels=False, xticklabels=100)
ax2.set_xticks([0, 100, 200, 300], [10, 20, 30, 40])
ax2.set_title('センサの値に対応するカラーマップ', fontsize=24, fontweight="bold")


def _update(frame):
    """グラフを更新するための関数"""
    # 現在のグラフを消去する
    ax1.clear()
    ax1.set_title('センサの値(８列)', fontsize=24, fontweight="bold")
    ax3.clear()
    ax3.set_title('座席の状態（ステータス）', fontsize=24, fontweight="bold")
    ax3.axis("off")
    ax3.set_xlim([0, 10])
    ax3.set_ylim([0, 5])
    ax4.clear()
    ax4.axis('off')
    ax4.set_title('現在時刻', fontsize=24, fontweight="bold")

    # データを更新 (追加) する
    last_row = tail('Z:/test.csv')[0].split(',')
    values = np.array(last_row).reshape((1, 8))
    temp = values.astype(float)

    # ヒートマップ描画
    sns.heatmap(temp, cmap='YlOrRd', vmin=10, vmax=40, ax=ax1,
                cbar=False, annot=True, fmt='1.1f', yticklabels=False)

    # 座席の状態
    dt_now = datetime.datetime.now()

    new_status, changed_time = get_status(
        dt_now, dt_past[-1], status_arr[-1], temp[0])
    status_arr.append(new_status)
    dt_past.append(changed_time)
    status_arr.pop(0)
    dt_past.pop(0)

    status = status_arr[-1]

    boxdic_abs = {
        "facecolor": "skyblue",
        "edgecolor": "blue",
        "boxstyle": "Round,pad=0.5",
        "linewidth": 2,
    }

    boxdic_exist = {
        "facecolor": "lightsalmon",
        "edgecolor": "orangered",
        "boxstyle": "Round,pad=0.5",
        "linewidth": 2,
    }

    boxdic_leaving = {
        "facecolor": "lightgreen",
        "edgecolor": "green",
        "boxstyle": "Round,pad=0.5",
        "linewidth": 2,
    }

    boxdic_other = {
        "facecolor": "#CCCCCC",
        "edgecolor": "#999999",
        "boxstyle": "Round,pad=0.5",
        "linewidth": 2,
    }

    # 四角形描画
    if status == 0:
        ax3.text(1.5, 2, '不在', color='blue', fontweight="heavy",
                 fontsize="36", bbox=boxdic_abs)
        ax3.text(4.5, 2, '在席', color='#999999',
                 fontsize="36", bbox=boxdic_other)
        ax3.text(7.5, 2, '一時離席', color='#999999',
                 fontsize="36", bbox=boxdic_other)

    if status == 1:
        ax3.text(1.5, 2, '不在', color='#999999',
                 fontsize="36", bbox=boxdic_other)
        ax3.text(4.5, 2, '在席', color='orangered', fontweight="heavy",
                 fontsize="36", bbox=boxdic_exist)
        ax3.text(7.5, 2, '一時離席', color='#999999',
                 fontsize="36", bbox=boxdic_other)

    if status == 2:
        ax3.text(1.5, 2, '不在', color='#999999',
                 fontsize="36", bbox=boxdic_other)
        ax3.text(4.5, 2, '在席', color='#999999', fontweight="heavy",
                 fontsize="36", bbox=boxdic_other)
        ax3.text(7.5, 2, '一時離席', color='green',
                 fontsize="36", bbox=boxdic_leaving)

    dt_now_txt = dt_now.strftime('%Y-%m-%d %H:%M:%S')

    ax4.text(0.25, 0, dt_now_txt, fontweight="heavy", fontsize="36")


# アニメーション設定
anime = animation.FuncAnimation(fig, _update, interval=1000)

# グラフを表示する
plt.show()
