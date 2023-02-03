import numpy as np

py_list = list(range(1000000))
np_array = np.arange(1000000)

print( %time for _ in range(100): np_array *= 2)
# CPU times: user 65.2 ms, sys: 0 ns, total: 65.2 ms Wall time: 73.7 ms


print( %time for _ in range(100): py_list = [x * 2 for x in py_list])
# CPU times: user 8.17 s, sys: 1.79 s, total: 9.96 s Wall time: 9.98 s
