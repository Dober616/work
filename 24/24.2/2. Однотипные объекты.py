class Monitor:
    monitor_name = 'Samsung'
    monitor_matrix = 'VA'
    monitor_res = 'WQHD'
    monitor_freq = 0

class Headphones:
    heads_name = 'Sony'
    heads_sensitivity = 108
    heads_micro = True

all_monitors = [Monitor() for _ in range(4)]
all_headphones = [Headphones() for _ in range(3)]

for index, number in enumerate([60, 144, 70, 60]):
    all_monitors[index].monitor_freq = number

all_headphones[0].heads_micro = False