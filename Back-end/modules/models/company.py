from modules.models.companyStock import CompanyStock

class Company:
    def __init__(self, name : str = "", symbol : str = "", 
                 region : str = "", rank : int = 0, sector : str = "", stock : CompanyStock = CompanyStock()):
        self.__name = name
        self.__symbol = symbol
        self.__region = region
        self.__rank = rank
        self.__sector = sector
        self.__stock = stock
    
    def getName(self):
        return self.__name

    def setName(self, name : str):
        self.__name = name
    
    def getSymbol(self):
        return self.__symbol

    def setSymbol(self, symbol : str):
        self.__symbol = symbol
    
    def getRegion(self):
        return self.__region
    
    def setRegion(self, region : str):
        self.__region = region
    
    def getRank():
        return self.__rank
    
    def setRank(self, rank : int):
        self.__rank = rank
    
    def getSector():
        return self.__sector
    
    def setSector(self, sector : str):
        self.__sector = sector
    
    def getStock():
        return self.__stock
    
    def setStock(self, stock : CompanyStock):
        self.__stock = stock
    
    def toJSON(self):
        data = {
            "name"  : self.__name,
            "symbol"   : self.__symbol,
            "region" : self.__region,
            "rank": self.__rank,
            "sector": self.__sector,
            "stock" : self.__stock.toJSON()
        }
        return data