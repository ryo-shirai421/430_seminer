import datetime


def get_status(current_time, past_time, past_status, sensor_values):
    """
    センサーの値と過去の情報から，現在の状態を決める関数

    引数
    ----------
    current_time       : 現在時刻
    past_time          : 前のステータスに変化した時の時刻
    past_status        : 前のステータス
    sensor_value       : センサの値 (1x8) の配列
    返り値
    -------
    current_status     : 現在時刻のステータス
    state_changed_time : ステータスが変化した時間
    """
    # Step1: 現在のステータスが変わらない事を確認しよう．
    # Step2: 温度が上がると在席，下がると離席となるようにプログラムを実装してみよう．
    # Step3: 過去の状態を利用して，一時離席を判断できるようにしよう．
    # Advance1: 在席と離席の判断を機械学習モデルにやらせてみよう．
    # Advance2: 決定木モデルで予測してみよう．
    # Advance3: 決定木がどのように判断しているかを見てみよう．(sandbox.ipynbで行う)

    # ------------------------------- ここから -----------------------------------
    current_status = 1

    # ----------------------------- ここまでに書く --------------------------------
    # 状態が変わったら，その時刻を保存しておく．
    state_changed_time = current_time if current_status != past_status else past_time

    return current_status, state_changed_time
