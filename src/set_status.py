import datetime


def change_status(current_time, past_time, past_status, sensor_values):
    """
    ステータスの変化に関する関数
    
    Parameters
    ----------
    current_time    : 現在時刻
    past_time       : 前のステータスに変化した時の時刻
    past_status     : 前のステータス
    sensor_value    : センサの値 (1*8)の配列

    Returns
    -------
    current_status  : 現在時刻のステータス
    change_time     : ステータスが変化した時間
    """

    if any(value >= 30 for value in sensor_values):
        current_status = 1

    else:
        if (past_status == 0):
            current_status = 0
        elif (past_status == 1):
            current_status = 2
        else:
            if (current_time - datetime.timedelta(minutes = 1) >= past_time):
                current_status = 0
            else:
                current_status = 2

    ### ------------------------------ ここから先は編集しない -----------------------------------###
    change_time = current_time if current_status != past_status else past_time

    return current_status, change_time
