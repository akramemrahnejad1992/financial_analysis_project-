import numpy as np
import datetime
from volume_profile import make_volume_profiles

def check_start_of_day(symbol, current_date):
    if symbol == 'CL':
        return current_date.hour == 6 and current_date.minute == 0
    elif symbol == 'GC':
        return current_date.hour == 5 and current_date.minute == 20
    return current_date.hour == 6 and current_date.minute == 30

def process_day_info(data, symbol):
    start_of_day = {}
    end_of_day = {}
    all_dates = []
    days_info = {}
    stats_list = ['inside_va', 'below_val', 'above_vah', 'below_range_low', 'above_range_high']

    for current_index in range(1, len(data)):
        current_date = data['DateTime'].iloc[current_index]
        curr_open = data['Candle_OpenPrice'].iloc[current_index]
        prev_low = data['Candle_LowPrice'].iloc[current_index - 1]
        prev_high = data['Candle_HighPrice'].iloc[current_index - 1]
        curr_high = data['Candle_HighPrice'].iloc[current_index]
        curr_low = data['Candle_LowPrice'].iloc[current_index]

        if datetime.time(5, 20, 0) <= current_date.time() < datetime.time(10, 30, 0):
            if check_start_of_day(symbol, current_date):
                ib_high = curr_high
                ib_low = curr_low
                start_of_day[str(current_date.date())] = current_index
                all_dates.append(str(current_date.date()))
                days_info[str(current_date.date())] = {key: False for key in stats_list}
                end_of_day[str(current_date.date())] = current_index

            if len(all_dates) > 1:
                prev_start = start_of_day[all_dates[-2]]
                prev_end = end_of_day[all_dates[-2]]
                val, poc, vah = make_volume_profiles(data, prev_start, prev_end)
                print(current_date, f'make prev day vp from {data.index[prev_start]} to {data.index[prev_end]}', val, vah)

    return days_info