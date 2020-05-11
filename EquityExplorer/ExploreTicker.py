# ------------------------ Imports ---------------------------------
import pandas as pd
import pandas_datareader as pdr
import datetime
import matplotlib.pyplot as plt
import os
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
    name: str; the name of the object. This will allow all plots saved in a specific
    folder with the name.
    data: pandas DataFrame: Dataframe obtained from get_info() function.
    '''
    def __init__(self, name, data):
        self.name = name.upper()
        self.data = data
        self.columns = data.columns
        self.open = data['Open']
        self.high = data['High']
        self.low = data['Low']
        self.Close = data['Close']
        self.adj_close = data['Adj Close']
        self.volume = data['Volume']

    def generate_plot(self, x, y, title, xlabel=None, ylabel=None, show=False, save=True):
        '''
        Generates a plot to show the historical price of a stock
        Parameters:
        -----------
            x: pandas Series; x-axis
            y: pandas Series; y-axis
            title: str; The title of the plot. If save=True, title will also be the save name
            xlabel: str Default=None; Label of the x-axis.
            ylabel: str Default=None; Label of the y-axis
            show: Bool; Default=False; If True, plot will appear in pop-up window
            save: Bool; Default=True; If True, image will save with same title title parameter

        '''
        fig, ax = plt.subplots(figsize=(10,5))
        ax.plot(x, y)
        ax.set(title=title.upper(),
               xlabel=xlabel,
               ylabel=ylabel)
        plt.grid(True)

        # Saves the plots
        if save == True:
            path = os.path.join(IMAGES_PATH, self.name )
            os.makedirs(path, exist_ok=True)
            print('\nSaving Figure as {} in {}'.format(title, path))
            plt.savefig(os.path.join(path, title))
            print('\nFigure Saved Successfully')

        if show == True:
            plt.show()

def get_info(tickers, start_date, end_date):
    '''
    Function that fetches and returns a dataframe with OHLC data for a given ticker.
    Can return one dataframe, or multiple, depending on how many objects are passed in to the stock parameter.
    Parameters:
    -----------
        tickers:
            str or list
            Should be a valid ticker, or list of tickers
        start_date:
            str or datetime object
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
