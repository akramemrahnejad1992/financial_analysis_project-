def main():
    symbol = 'GC'
    data = load_data('../data/Korbs/LOB1_GCG24-COMEX_1min_0PercentSum_0PercentOrders_Overlapped.csv')
    days_info = process_day_info(data, symbol)

    # Define ranges and events for analysis
    target_ranges = ['inside_va', 'below_val', 'above_vah', 'below_range_low', 'above_range_high']
    events = ['number_of_days', 'break_on_high', 'break_on_mid', 'break_on_low', 
              'retest_on_vah', 'retest_on_val', 'retest_on_poc', 
              'break_ib_high', 'break_ib_low']

    # Calculate statistics
    event_info = calculate_event_statistics(days_info, target_ranges, events)
    print_event_statistics(event_info, target_ranges)

if __name__ == "__main__":
    main()