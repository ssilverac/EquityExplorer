import pandas as pd
import pandas_datareader as pdr
import datetime
import matplotlib.pyplot as plt
import os
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
TODAY = datetime.date.today()

# ------------------- ADJUST THESE VARIABLES -------------------

#TICKERS = ['aapl','msft','ibm','tsla', 'spy']
TICKERS = 'spy'
START_DATE = '2019-01-01'
END_DATE = TODAY


# ------------------- Do Not Edit Below this line -------------------

PROJECT_ROOT_DIR = '.'
IMAGES_PATH = os.path.join(PROJECT_ROOT_DIR, 'images')

class ExploreTicker:
    '''This class will hold all functions to plot data as well as calculating
    various values which can be used to further analyze the stock and its price
    action.
    '''
    def __init__(self, name, ticker):
        self.name = name
        self.ticker = ticker
        self.columns = ticker.columns
        self.high = ticker['High']
        self.low = ticker['Low']
        self.open = ticker['Open']
        self.Close = ticker['Close']
        self.volume = ticker['Volume']
        self.adj_close = ticker['Adj Close']

    def generate_plot(self, xlabel, ylabel, show=False):
        '''
        Generates a plot to show the historical price of a stock
        Parameters:
        -----------
            xlabel: str; Label of the x-axis. Usually Date
            ylabel: str; Label of the y-axis
            show: Bool; Default=False. If set to True, plot will appear in pop-up window
        '''
        fig, ax = plt.subplots(figsize=(10,5))
        ax.plot(self.ticker.index, self.adj_close)
        ax.set(title=self.name,
                xlabel=xlabel,
                ylabel=ylabel)
        plt.grid(True)

        # Saves the plots
        path = os.path.join(IMAGES_PATH, self.name)
        os.makedirs(path, exist_ok=True)
        print('\nSaving Figure as {} in {}'.format(self.name, path))
        plt.savefig(os.path.join(path, self.name + '_price'))
        print('\nFigure Saved Successfully')

        if show == True:
            plt.show()

def get_info(tickers, start_date=START_DATE, end_date=END_DATE):
    '''
    Function that fetches and returns a dataframe with OHLC data for a given ticker.
    Can return one dataframe, or multiple, depending on how many objects are passed in to the stock parameter.
    Parameters:
    -----------
        tickers:
            str or list
            Should be a valid ticker, or list of tickers
        start_date:
            str
            Should be in the form of yyyy-mm-dd
        end_date:
            str
            Should be in the form of yyyy-mm-dd
    Returns:
    --------
        A dataframe indexed by date, containing OHLC info for the tickers.
        If more than one ticker is passed
        in, it will return a dictionary, which can be accessed by the keys
        Dictionary:
            Keys
                the ticker for the company
            values
                dataframe
    '''
    def build_df(stock, start_date, end_date):
        df = pd.DataFrame(pdr.DataReader(stock.upper(), 'yahoo', start_date, end_date))
        return df

    if type(tickers) == str: #check if function was called with a list or a single ticker
        df = build_df(tickers, start_date, end_date)
        return df

    else:
        result = {}
        for i in range (len(tickers)):
            result[tickers[i]] = build_df(tickers[i], start_date, end_date)
        return result

def main():
    '''
    Main Program
    '''
    ls = TICKERS
    data = get_info(ls)
    print(data.keys())
    #i.generate_plot('Date', 'Adj Close', show=True)

if __name__ == '__main__':

    main()
