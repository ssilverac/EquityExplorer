"""Main file for our entire program"""
# Imports
import EquityExplorer.calculate as calc
import EquityExplorer.ExploreTicker as explore

def main():
    ls = ['ibm', 'aapl', 'tsla', 'msft', 'acb']

    dfs = explore.get_info(ls, '2019-01-01','2020-01-01')
    print(dfs.keys())

    IBM = explore.ExploreTicker('ibm', dfs['ibm'])
    print(IBM.data)





if __name__ == '__main__':
    main()
