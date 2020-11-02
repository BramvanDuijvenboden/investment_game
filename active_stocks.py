import pandas as pd
from search import enhanced_searchterm

class Listings:
    def __init__(self):
        self.listings = pd.read_csv('listing_status.csv')
        self.listings = self.listings.dropna(subset=['name'],inplace=True)

    def find_company(self):
        while True
            searchterm=input("Which company are you looking for?")
            enh = enhanced_searchterm(searchterm.strip())
            results = []
            number = 1
            for name in self.listings['name']:
                if re.search(enh, name):
                    results.append((number, name))
                    number += 1
            if len(results) > 0:
                return results

    def choose_company(self):
        while True:
            search_results = self.find_company()
            print("Your search had ", str(len(search_results)), 'results: \n', search_results)
            choice = int(
                input("Type the number of the company you are looking for. Type 0 if the company is not in the list"))
            if choice != 0:
                return search_results[choice - 1][1]



    def get_symbol(self,name):
        return self.listings[listings['name']==name]['symbol']]



