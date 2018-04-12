from random import choice
from pyknow import *

class characterstics(Fact):
    pass

class diagnosticEngine(KnowledgeEngine):
    @Rule(characterstics(service='fast-food')
          & (characterstics(food_served = 'Veg')|characterstics(food_served = 'Non-Veg'))
          & (characterstics(meal_price ='medium')|characterstics(meal_price = "expensive")))
    def Bnb_cp(self):
        print("You Should Try Bnb at CP")

    @Rule(characterstics(service='sit-down')
          & (characterstics(food_served = 'Veg')|characterstics(food_served = 'Non-Veg'))
          & (characterstics(meal_price ='medium')|characterstics(meal_price = "expensive")))
    def _Bnb_mess1(self):
        print("Bnb near mess 1 is the place you should look")

    @Rule((characterstics(service='sit-down') | characterstics(sevice = 'buffet'))
          & (characterstics(food_served='Veg'))
          & (characterstics(meal_price='cheap')))
    def _cafeteria(self):
        print("Try Cafeteria")

    @Rule(characterstics(service='fast-food')
          & (characterstics(food_served='Veg') | characterstics(food_served='Non-Veg'))
          & (characterstics(meal_price='cheap') | characterstics(meal_price="medium")))
    def _yumpy(self):
        print("Yumpy is the best place to look for")

    @Rule(characterstics(service='buffet')
          & (characterstics(food_served='Veg'))
          & (characterstics(meal_price='cheap')))
    def _mess(self):
        print("Mess 1  or Mess 2 can be a option")

    @Rule((characterstics(service='sit-down') | characterstics(service='fast-food'))
          & (characterstics(food_served='Veg') | characterstics(food_served='Non-Veg'))
          & (characterstics(meal_price='medium')))
    def _c3(self):
        print("Try C3")






if __name__ == '__main__':
    engine = diagnosticEngine()
    engine.reset()
    engine.declare(characterstics(service = 'fast-food',  #sit-down, fast-food, buffet
                                  food_served = 'Non-Veg',   #Veg and Non Veg
                                 meal_price = 'medium'))        #cheap medium expensive
    engine.run()
    #print(engine.facts)

