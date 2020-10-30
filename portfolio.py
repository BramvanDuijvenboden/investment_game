
from user import User

# We want to start by defining a class/portfolio
class Portfolio:
    def __init__(self,user):
        self.name = ("%s's portfolio" % user.name)
        print(self.name)
