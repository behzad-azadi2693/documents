class Model():

    peyks = {
            'KamtarAz30kg'  :{'price':10000},
            '30-70kg'       :{'price':15000},
            '70-100kg'      :{'price':20000},
            'BalatarAz100kg':{'price':30000},
            }

class View():

    def list_peyks(self, peyks):
        for pek in peyks:
            print(pek, '')

    def list_price(self, peyks):
        for pek in peyks :
            print("Hazineye peyk baraye", pek, "mishavad", Model.peyks[pek]['price'])


class Controller():

    def __init__(self):
        self.model = Model()
        self.view = View()

    def get_peyks(self):
        peyks = self.model.peyks.keys()
        return(self.view.list_peyks(peyks))

    def get_price(self):
        peyks = self.model.peyks.keys()
        return(self.view.list_price(peyks))

class Client():
    controller = Controller()
    print("peyk haye mojood")
    controller.get_peyks()
    print("hazineha")
    controller.get_price()                      
