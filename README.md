# Trading Statistics Analysis Project

## Overview

This project analyzes trading day statistics based on price action and volume profiles. It processes historical trading data to compute various statistical measures related to significant price levels, volume activity, and trading events. The results can be used for trading strategy development and performance evaluation.

## Project Structure

```
project/
│
├── main.py                     # Main entry point for the program
├── data_loader.py              # Module for loading and preprocessing data
├── volume_profile.py            # Module for volume profile calculations
├── day_info_processor.py        # Module for processing day-specific information
└── statistics_calculator.py     # Module for calculating and printing statistics
```

## Requirements

- Python 3.x
- Pandas
- NumPy

You can install the required packages using pip:

```bash
pip install pandas numpy
```

## Usage

1. **Data Preparation**: Ensure you have a CSV file containing your trading data. The file should have the following columns:
   - `DateTime`: The timestamp of each data point.
   - `Candle_OpenPrice`: The opening price of the trading candle.
   - `Candle_HighPrice`: The highest price of the trading candle.
   - `Candle_LowPrice`: The lowest price of the trading candle.
   - `Candle_ClosePrice`: The closing price of the trading candle.
   - `VAP_Prices`: A list of prices for volume analysis.
   - `VAP_Volumes`: A list of volumes corresponding to the prices.

2. **Running the Program**: Execute the main script to start the analysis.

```bash
python main.py
```

3. **Output**: The program will print the calculated statistics for different trading events and their occurrences based on the defined ranges.

## Example Output

When you run the program, you will see output similar to the following:

```
Statistics for inside_va:
number_of_days: 20
break_on_high: 15
break_on_low: 10
break_on_high_or_break_on_low: 20%
break_on_high_and_break_on_low: 5%
neither_break_on_high_nor_break_on_low: 15%
...
```

