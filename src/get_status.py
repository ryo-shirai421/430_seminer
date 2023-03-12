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

    # ------------------------------- ここから -----------------------------------

    if any(value >= 30 for value in sensor_values):
        current_status = 1

    else:
        if (past_status == 0):
            current_status = 0
        elif (past_status == 1):
            current_status = 2
        else:
            if (current_time - datetime.timedelta(minutes=1) >= past_time):
                current_status = 0
            else:
                current_status = 2

    # ------------------------------- ここまで -----------------------------------

    # 状態が変わったら，その時刻を保存しておく．
    state_changed_time = current_time if current_status != past_status else past_time

    return current_status, state_changed_time
