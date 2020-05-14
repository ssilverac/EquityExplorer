# ------------------------ Imports ---------------------------------
import pandas as pd
import numpy as np
import pandas_datareader as pdr
import datetime
import matplotlib.pyplot as plt
import os
import ta
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# --------------------------------------------------------------------
# ---------------------- Global Vars ---------------------------------

PROJECT_ROOT_DIR = '.'
IMAGES_PATH = os.path.join(PROJECT_ROOT_DIR, 'images')

# -----------------------------------------------------------------
class ExploreTicker:
    '''
    Parameters
    ----------
    name: str;
        The name of the object. This will allow all plots saved in a specific
        folder with the name.
    data: pd.Dataframe:
        Dataframe obtained from get_info() function.
    '''
    def __init__(self, name, data):
        self.name = name.upper()
        self.data = data
        self.date = data.index
        self.columns = data.columns
        self.open = data['Open']
        self.high = data['High']
        self.low = data['Low']
        self.close = data['Close']
        self.adj_close = data['Adj Close']
        self.volume = data['Volume']

    def calculate_bollinger_bands(self, window, stdevs):
        indicator_bb = ta.volatility.BollingerBands(self.close, window, stdevs)

        mavg = indicator_bb.bollinger_mavg()
        high = indicator_bb.bollinger_hband()
        low = indicator_bb.bollinger_lband()

        return mavg, high, low

    def calculate_percent_change(self, data, periods=1):
        '''
        Calculates the percent change of a series.
        Parameters:
        -----------
            data: pd.Series, pd.DataFrame
                The data which you wish to calculate percent change for
            periods: int; Default=1
                Periods over which to shift for forming percent change
        Returns:
        --------
        percent_change: pd.Series or pd.Dataframe
            Will be the same type as the calling object
        '''

        return data.pct_change(periods) * 100

    def generate_plot(self, x, y, title, xlabel=None, ylabel=None, show=False, save_name=None):
        '''
        Generates a plot to show the historical price of a stock
        Parameters:
        -----------
            x: pd.Series
                Data which will be used as x-axis
            y: pd.Series or list containing pd.Series objects
                Data which will be used as y-axis. If list passed in, everything
                will be plotted on the same axis.
            title: str
                The title of the plot. If save=True, title will also be the save name
            xlabel: str; Default=None
                Label of the x-axis.
            ylabel: str; Default=None
                Label of the y-axis
            show: Bool; Default=False
                If True, plot will appear in pop-up window
            save_name: str; Default=None
                If save_name specified, image will save as save_name, otherwise
                it will not save
        '''
        fig, ax = plt.subplots(figsize=(10,5))
        #for i in y:
        ax.plot(x, y)

        ax.set(title=title.upper(),
               xlabel=xlabel,
               ylabel=ylabel)
        plt.grid(True)

        # Saves the plots
        if save_name != None:
            path = os.path.join(IMAGES_PATH, self.name)
            os.makedirs(path, exist_ok=True)
            print('\nSaving Figure as {} in {}'.format(save_name, path))
            plt.savefig(os.path.join(path, save_name))
            print('\nFigure Saved Successfully')


        if show == True:
            plt.show()


def get_info(tickers, start_date, end_date):
    '''
    Function that fetches and returns a dataframe with OHLC data for a given ticker.
    Can return one dataframe, or multiple, depending on how many objects are passed in to the stock parameter.
    Parameters:
    -----------
        tickers: str or list
            Should be a valid ticker, or list of tickers
        start_date: str or datetime object
            Should be in the form of yyyy-mm-dd
        end_date: str or datetime object
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
    if type(tickers) == str: #check if function was called with a list or a single ticker
        df = pd.DataFrame(pdr.DataReader(tickers.upper(), 'yahoo', start_date, end_date))
        return df

    elif type(tickers) == list:
        result = {}
        for i in range (len(tickers)):
            result[tickers[i]] = pd.DataFrame(pdr.DataReader(tickers[i].upper(), 'yahoo', start_date, end_date))
        return result
    else:
        raise TypeError("tickers must be <class 'str'> or <class 'list'>; {} passed instead".format(type(tickers)))

def test():
    '''Test function when developing'''
    pass

if __name__ == '__main__':

    test()
