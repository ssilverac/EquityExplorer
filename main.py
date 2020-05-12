"""Main file for our entire program"""
# Imports
import EquityExplorer.ExploreTicker as explore
import matplotlib.pyplot as plt

START_DATE = '2019-01-01'
END_DATE = '2020-01-01'

def main():
    tesla = explore.ExploreTicker('tesla', explore.get_info('tsla', START_DATE, END_DATE))
    tesla.data['MAVG'], tesla.data['hband'], tesla.data['lband'] = tesla.calculate_bollinger_bands(window=20, stdevs=2)

    tesla.generate_plot(
    x=tesla.date,
    y=[tesla.data['MAVG'], tesla.data['hband'], tesla.data['lband'], tesla.close],
    title='Tesla-BBands',
    xlabel='Date',
    ylabel='Price',
    show=True,
    )

    tesla.data['pct_change'] = tesla.calculate_percent_change(tesla.adj_close)
    print(tesla.data)


if __name__ == '__main__':
    main()
