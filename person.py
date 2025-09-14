class Person():
    def __init__(self, name, age, height, weight, sex):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.sex = sex


    def checks(self):
        if (self.age <= 0):
            raise ValueError("Age must be greater than zero.")
        if (self.height <= 0 or self.height > 250):
            raise ValueError("Height must be between 0 and 250 cm.")
        if (self.weight <= 0 or self.weight > 500):
            raise ValueError("Weight must be between 0 and 500 kg.")

    def evaluate(self):
        return self.__basal_metabolic_rate()
    
    def diet(self, goal):   
        if (goal == "maintain"):
            kcal = self.__basal_metabolic_rate() * 1.55
            phrase = f"To maintain your weight, you should consume around {round(kcal)} kcal per day."
            return phrase
        
        elif (goal == "lose"):
            kcal = self.__basal_metabolic_rate() * 1.55 - 500
            phrase = f"To lose weight, you should consume around {round(kcal)} kcal per day."
            return phrase
        
        elif (goal == "gain"):
            kcal = self.__basal_metabolic_rate() * 1.55 + 500
            phrase = f"To gain weight, you should consume around {round(kcal)} kcal per day."
            return phrase
        
    

    def __basal_metabolic_rate(self):
        if (self.sex == "F"):
            tmb = 655.1 + (9.563 * self.weight) + (1.850 * self.height) - (4.676 * self.age) 
            return tmb 
        
        else:
            tmb = 66.47 + (13.75 * self.weight) + (5.003 * self.height) - (6.755 * self.age)
            return tmb
        