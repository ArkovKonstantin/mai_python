import csv
import os
import datetime
from time import time
import functools
import pandas as pd

LOGS_PATH = "./train/other_user_logs/"


def get_time(s: str) -> int:
    print(s)
    arr = s[s.find(' ') + 1:].split(':')
    return int(arr[0]) * 60 * 60 + int(arr[1]) * 60 + int(arr[2])


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
                for curr_idx, row in enumerate(reader):
                    # skip header
                    if is_head:
                        is_head = False
                        continue
                    # skip values than not in window
                    if slow_idx % window_size != 0:
                        slow = row
                        slow_idx = curr_idx
                        continue
                    # assign fast pointer
                    fast = row
                    # init slow pointer
                    if slow is None:
                        slow = fast
                        d1 = get_time(slow[0])

                    d2 = get_time(fast[0])
                    # check if window is reached
                    if (d2 - d1) / 60 > max_duration or len(window) == session_length:
                        # sessions.append(window)
                        window.append(user_id)
                        yield window
                        if window_size < len(window):
                            window = window[window_size:]
                            slow = window[0]
                            slow_idx += window_size
                            print(slow)
                            d1 = get_time(slow[0])
                        else:
                            slow = fast
                            slow_idx = curr_idx
                            d1 = get_time(slow[0])
                            window = []
                            continue

                    # processing edge case
                    if (d2 - d1) / 60 > max_duration:
                        # sessions.append(window)
                        window.append(user_id)
                        yield window
                        slow = fast
                        slow_idx = curr_idx
                        d1 = get_time(slow[0])
                        window = []

                    window.append(fast[1])
                    window.append(fast[0])

                # sessions.append(window)
                window.append(user_id)
                yield window

    columns = []
    for i in range(1, session_length + 1):
        columns.append(f'site{i}')
        columns.append(f'time{i}')
    columns.append('user_id')
    g = gen()
    return pd.DataFrame.from_records(g, columns=columns)


if __name__ == '__main__':
    start = time()
    # print(prepare_train_set(LOGS_PATH, 10, 10, 30))
    df = prepare_train_set('./user_logs_example.csv', 4, 2, 30)
    # df = prepare_train_set(LOGS_PATH, 10, 10, 30)
    print((time() - start) / 10 ** 9, "s")
    # import pstats
    # p = pstats.Stats("out.txt")
    # p.strip_dirs().sort_stats('time').print_stats()
