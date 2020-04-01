import pymysql
from baseObject import baseObject

class customerList(product):
    
    def __init__(self):
        self.setupObject('mccartg_product')
        
   
    def verifyNew(self, n=0):
        self.errorList = []
        if len(self.data[n]['sku']) == 0:
            bl = str(item) + ' cannot be blank.'
        
        
        pf = None    
        try: 
            pf = float(self.data[n]['price'])
        except:
            self.errorList.append()
        if pf is not None:
            if pf <0:
                    self.errorList.append('Price is less than 0, needs to be a positive amount.')
            else:
                self.data[n]{'price'} = price
                

        if len(self.errorList) > 0:
            return False
        else:
            return True
          