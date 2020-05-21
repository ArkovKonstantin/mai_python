import pandas as pd


def get_time(s: str) -> int:
    arr = s[s.find(' ') + 1:].split(':')
    print(arr)
    return int(arr[0]) * 60 * 60 + int(arr[1]) * 60 + int(arr[2])


# print((get_time('2013-11-15 11:37:26') - get_time('2013-11-15 09:28:17')) / 60)
import timeit
a = timeit.default_timer()
arr = [["a", 1, 1], ["b", 2], ["c", 3]]
df = pd.DataFrame.from_records(arr, columns=['user', 'id', 'age'])
print(df)
print(timeit.default_timer()-a)
