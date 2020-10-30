class Exchange:
    def __init__(self):
        self.name = "KOBEX"
        print("Welcome at %s" %self.name)

    def available_stocks(self):
        stocks = {'ABN AMRO Group':'ABN', 'Ahold Delhaize':'AD', 'Adyen':'ADYEN', 'Aegon':'AGN', 'AkzoNobel':'AKZA',
                  'ASM International':'ASM', 'ASML Holding':'ASML', 'ASR Nederland':'ASRNL', 'DSM':'DSM',
                  'Galapagos':'GLPG', 'Heineken':'HEIA', 'IMCD':'IMCD', 'ING Group':'INGA', 'KPN':'KPN',
                  'ArcelorMittal':'MT',	'NN Group':'NN', 'Philips':'PHIA', 'Prosus':'PRX', 'Randstad':'RAND',
                  'Royal Dutch Shell':'RDSA', 'RELX':'REN', 'Just Eat Takeaway':'TKWY', 'Unilever':'UNA',
                  'Unibail-Rodamco-Westfield':'URW', 'Wolters Kluwer':'WKL'}
        print(stocks.keys())
        #choice = input("Choose a company:")
        #try:
        #    choice in stock.keys()
        #except:
        #    print("Stock not available")


    #def stock_price(stock):