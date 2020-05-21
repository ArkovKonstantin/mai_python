import csv
import os
import datetime
import itertools
import pandas as pd

LOGS_PATH = "./train/other_user_logs/"


def get_time(s: str) -> int:
    args = list(itertools.chain(map(int, s[:s.find(' ')].split('-')),
                                map(int, s[s.find(' ') + 1:].split(':'))))
    return datetime.datetime(*args)


def create_df_row(w: list, user_id: str, session_length):
    row = [None] * (session_length*2 + 1)
    for i, v in enumerate(w):
        row[i] = v[1]
        row[i + 1] = v[0]
    row[-1] = user_id
    return row


def prepare_train_set(logs_path: str, session_length: int, window_size: int, max_duration: int):
    def gen():
        if os.path.isdir(logs_path):
            files = os.listdir(LOGS_PATH)
        else:
            files = [""]

        for j, filename in enumerate(files):
            idx = filename.find('.csv')
            user_id = filename[idx - 4:idx]
            # sessions = []
            with open(logs_path + filename) as csv_file:
                reader = csv.reader(csv_file)
                is_head = True
                fast, slow = None, None
                window = []
                slow_idx = 0
                for curr_idx, row in enumerate(reader, -1):
                    # skip header
                    if is_head:
                        is_head = False
                        continue
                    # skip values than not in window
                    if not window and slow_idx % window_size != 0:
                        slow = row
                        slow_idx = curr_idx
                        continue
                    # assign fast pointer
                    fast = row
                    d2 = get_time(fast[0])
                    # init slow pointer
                    if slow is None:
                        slow = fast
                        d1 = get_time(slow[0])

                    # tree of conditions
                    if len(window) == session_length:
                        # window closed
                        yield create_df_row(window, user_id, session_length)
                        if (d2 - d1).total_seconds() / 60 <= max_duration:
                            # session continues
                            if window_size < len(window):
                                window = window[window_size:]
                                slow = window[0]
                                slow_idx += window_size
                                d1 = get_time(slow[0])
                                window.append(fast)
                            elif window_size > len(window):
                                window = []
                                slow = fast
                                slow_idx = curr_idx
                                d1 = get_time(slow[0])
                            elif window_size == len(window):
                                slow = fast
                                slow_idx = curr_idx
                                d1 = get_time(slow[0])
                                window = [fast]

                        elif (d2 - d1).total_seconds() / 60 > max_duration:
                            # session closed
                            slow = fast
                            slow_idx = curr_idx
                            window = [slow]
                            d1 = get_time(slow[0])

                    elif len(window) != session_length:
                        # window continues
                        if (d2 - d1).total_seconds() / 60 <= max_duration:
                            # session continues
                            window.append(fast)
                            if not window:
                                slow = fast
                                slow_idx = curr_idx
                                d1 = get_time(slow[0])

                        elif (d2 - d1).total_seconds() / 60 > max_duration:
                            # session closed
                            if window:
                                yield create_df_row(window, user_id, session_length)

                                if window_size < len(window):
                                    while len(window) >= window_size:
                                        window = window[window_size:]
                                        yield create_df_row(window, user_id, session_length)

                                elif window_size >= len(window):
                                    yield create_df_row(window, user_id, session_length)

                                slow = fast
                                window = [slow]
                                slow_idx = curr_idx
                                d1 = get_time(slow[0])

                yield create_df_row(window, user_id, session_length)

    columns = []
    for i in range(1, session_length + 1):
        columns.append(f'site{i}')
        columns.append(f'time{i}')
    columns.append('user_id')
    g = gen()
    return pd.DataFrame.from_records(g, columns=columns)


if __name__ == '__main__':
    start = datetime.datetime.now()
    df = prepare_train_set(LOGS_PATH, 10, 10, 30)
    # print(df)
    # df = prepare_train_set('./user_logs_example.csv', 4, 2, 30)
    # print(df)
    print((datetime.datetime.now() - start).seconds, "s")

    # import pstats
    # p = pstats.Stats("out.txt")
    # p.strip_dirs().sort_stats('time').print_stats()
