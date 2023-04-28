import datetime
import pickle


def get_status(current_time, past_time, past_status, sensor_values):
    """
    センサーの値と過去の情報から，現在の状態を決める関数

    引数
    ----------
    current_time       : 現在時刻
    past_time          : 前のステータスに変化した時の時刻
    past_status        : 前のステータス
    sensor_values       : センサの値 (1x8) の配列
    返り値
    -------
    current_status     : 現在時刻のステータス
    state_changed_time : ステータスが変化した時間
    """
    # Step1: 現在のステータスが変わらない事を確認しよう．
    current_status = 0
    # Step2: 温度が上がると在席，下がると離席となるようにプログラムを実装してみよう．
    if any(value >= 30 for value in sensor_values):
        current_status = 1
    # Step3: 機械学習を使って状態を判断してみましょう．
    model = pickle.load(open("../models/model.pkl", "rb"))
    current_status = model.predict([sensor_values])[0]
    # Step4: 過去の状態を利用して，一時離席を判断できるようにしよう．
    """
    if current_status != 1:
        if past_status == 0:
            current_status = 0
        elif past_status == 1:
            current_status = 2
        else:
            if current_time - datetime.timedelta(minutes=1) >= past_time:
                current_status = 0
            else:
                current_status = 2
                """

    # 状態が変わったら，その時刻を保存しておく．
    state_changed_time = current_time if current_status != past_status else past_time

    return current_status, state_changed_time


if __name__ == "__main__":
    # 引数の定義（具体値を入れてみる）
    past_time = datetime.datetime(year=2023, month=4, day=30, hour=12, minute=15, second=15)
    current_time = datetime.datetime(year=2023, month=4, day=30, hour=12, minute=15, second=25)
    past_status = 3
    sensor_values = [23, 24, 25, 26, 27, 28, 29, 30]
    # 関数の呼び出し
    current_status, state_changed_time = get_status(current_time, past_time, past_status, sensor_values)

    # 結果の確認
    print("過去の状態：{} --> 現在の状態：{}".format(past_status, current_status))
    print("状態が変化した時間：{}".format(state_changed_time))
