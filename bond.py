from main import tda_auth
import re
from datetime import date

c = tda_auth()


class Bond:
    asset_type = 'bond'
    def __init__(self,cusip):
        self.bond = c.get_instrument(cusip)
        self.cusip=cusip
        self.face_value = 100

    def get_price(self):
        return self.bond.json()[0]['bondPrice'].__round__(5)

    def get_coupon(self):
        return re.findall(r'\d+\.\d+|\d+',self.bond.json()[0]['description'])

    def get_description(self):
        return self.bond.json()[0]['description']

    def get_dtm(self):
        return (date(int(self.get_coupon()[1]),int(self.get_coupon()[2]),int(self.get_coupon()[3]))-date.today()).days

    def get_fv(self):
        return 100

    def get_raw_return(self):
        if Bond.get_coupon(self)==0:
            return (((Bond.get_fv(self)-Bond.get_price(self))/100)*100).__round__(4)
        else:
            return (((Bond.get_fv(self)-Bond.get_price(self))/100)+((float(Bond.get_coupon(self)[0])/100)*(Bond.get_dtm(self)/365)))*100

    def get_ann_return(self):
        if Bond.get_coupon(self)==0:
            return (((1 + (Bond.get_raw_return(self) / 100)) ** (365 / Bond.get_dtm(self)))-1)*100
        else:
            return (((1 + (Bond.get_raw_return(self) / 100)) ** (365 / Bond.get_dtm(self)))-1).__round__(5)*100