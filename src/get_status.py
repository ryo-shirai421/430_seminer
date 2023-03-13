import datetime


def get_status(now_time, past_time, past_status, values):
    '''
    time: 現在時刻
    past_time: 前のステータスに変化した時の時刻
    past_status: 前のステータス
    value: センサの値 (1*8)の配列
    '''

    if any(v >= 30 for v in values):
        new_status = 1

    else:
        if (past_status == 0):
            new_status = 0
        elif (past_status == 1):
            new_status = 2
        else:
            if (now_time - datetime.timedelta(minutes=1) >= past_time):
                new_status = 0
            else:
                new_status = 2

    if (new_status != past_status):
        change_time = now_time
    else:
        change_time = past_time

    return new_status, change_time
