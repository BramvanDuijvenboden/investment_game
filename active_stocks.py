import pandas as pd
from search import enhanced_searchterm, search_results

class Listings:
    def __init__(self):
        self.listings = pd.read_csv('listing_status.csv').dropna(subset=['name'])

    def find_company(self):
        while True:
            searchterm=enhanced_searchterm(input("Which company are you looking for?").strip())
            results = search_results(searchterm,self.listings['name'])
            if len(results) > 0:
                return results

    def choose_company(self):
        while True:
            search_results = self.find_company()
            print("Your search had ", str(len(search_results)), 'results: \n', search_results)
            choice = int(
                input("Type the number of the company you are looking for. Type 0 if the company is not in the list"))
            if choice > 0:
                try:
                    return search_results[choice - 1][1]
                except:
                    print("Your choice is not in the list")


    def get_symbol(self):
        company = self.choose_company()
        symbol = self.listings[self.listings['name']==company]['symbol']
        symbol = symbol.to_string(index=False)
        print(symbol)
        return symbol



