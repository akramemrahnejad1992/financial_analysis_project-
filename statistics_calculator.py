from collections import defaultdict

def days_in_range(days_info, target_range):
    return len([date for date in days_info.keys() if days_info[date][target_range]])

def days_break_event(days_info, target_range, event):
    return len([date for date in days_info.keys() if days_info[date][target_range] and days_info[date][event]])

def days_break_any_events(days_info, target_range, event_1, event_2):
    return len([date for date in days_info.keys() if days_info[date][target_range] and (days_info[date][event_1] or days_info[date][event_2])])

def days_break_all_events(days_info, target_range, event_1, event_2):
    return len([date for date in days_info.keys() if days_info[date][target_range] and (days_info[date][event_1] and days_info[date][event_2])])

def days_break_no_events(days_info, target_range, event_1, event_2):
    return len([date for date in days_info.keys() if days_info[date][target_range] and (not days_info[date][event_1] and not days_info[date][event_2])])

def calculate_event_statistics(days_info, target_ranges, events):
    event_info = defaultdict(lambda: {event: 0 for event in events})

    for target_range in target_ranges:
        event_info[target_range]['number_of_days'] = days_in_range(days_info, target_range)

        for event in events[1:]:
            event_info[target_range][event] = days_break_event(days_info, target_range, event)

        for event_1, event_2 in [('break_on_high', 'break_on_low'), ('retest_on_vah', 'retest_on_val'), ('break_ib_high', 'break_ib_low')]:
            event_info[target_range][f'{event_1}_or_{event_2}'] = days_break_any_events(days_info, target_range, event_1, event_2)
            event_info[target_range][f'{event_1}_and_{event_2}'] = days_break_all_events(days_info, target_range, event_1, event_2)
            event_info[target_range][f'neither_{event_1}_nor_{event_2}'] = days_break_no_events(days_info, target_range, event_1, event_2)

    return event_info

def print_event_statistics(event_info, target_ranges):
    for target_range in target_ranges:
        print(f"Statistics for {target_range}:")
        for event, count in event_info[target_range].items():
            print(f"{event}: {count}")