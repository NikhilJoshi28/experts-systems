from pyknow import *

class Symptoms(Fact):
    pass

class diagnosticEngine(KnowledgeEngine):
    # @DefFacts()
    # def _initial_action(self):
    #     yield Fact(action= "Disease")

    @Rule(Symptoms(disease=True))
    def diseaseType(self):
        self.declare(Fact(concern = True))

    @Rule(((Symptoms(diarrhea = True) | Symptoms(vomiting = True)) & (Symptoms(fever= True) | Symptoms(dizziness = True) & Symptoms(loss_of_apatite = True))))        
    def _food_poisoning(self):
        print("You Might Have Food Poisining")
        #print(Symptons.fever_temp)
        #if fever_temp > 101.5:
        #    print("Potentially Dangerous food poisoning")


if __name__ == '__main__':
    engine = diagnosticEngine()
    engine.reset()
    engine.declare(Symptoms(disease = True,
                            age = 45,
                            vomiting = True,
                            abnormal_pain = True,
                            back_pain =True,
                            cheat_pain = True,
                            cough = True,
                            dark_Urine = True,
                            diarrhea = True,
                            dizziness = True,
                            fatigue = True,
                            fever = True,
                            fever_temp = 102,
                            gas = True,
                            joint_pain =True,
                            headache = True,
                            loss_of_apatite = True,
                            rash = True,
                            ))
    engine.run()
    #print(engine.facts)

