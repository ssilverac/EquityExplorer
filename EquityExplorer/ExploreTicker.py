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
            xlabel: str; Label of the x-axis. Usually Date
            ylabel: str; Label of the y-axis
            show: Bool; Default=False. If set to True, plot will appear in pop-up window
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
            print('\nSaving Figure as {} in {}'.format(self.name, path))
            plt.savefig(os.path.join(path, title))
            print('\nFigure Saved Successfully')

        if show == True:
            plt.show()

    def calculate_percent_change(self, column):
        'Calculates percent change of series'

        percent_change = (column.pct_change()) * 100
        return percent_change


    def calculate_momentum(self):
        pass

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

def main():
    '''
    Main Program
    '''

    ls = TICKERS


    dfs = get_info(ls)

 # This doesnt work. It does not give back seperate dataframes.
 # Need to use something like a dictionary or something to store these objects?



    # cls_ls = []
    # for  i in dfs:
    #     print(i)
    #     cls_ls.append(ExploreTicker(i, dfs[i]))
    #
    # for i in cls_ls:
    #     print(i.name)

    spy = ExploreTicker('spy', dfs)
    spy.generate_plot(spy.data.index, spy.adj_close, 'spy_close', 'Date', 'Price', show=True, save=True)
     #spy.pcnt_change = spy.adj_close.pct_change() * 100
     #print(spy.pcnt_change)
     #spy_percent_change = spy.calculate_percent_change(spy.adj_close)





if __name__ == '__main__':

    main()
