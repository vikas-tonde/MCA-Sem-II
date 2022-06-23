class Bmi:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def getName(self):
        return self.name

    def getHeight(self):
        return self.name

    def getAge(self):
        return self.name

    def getWeight(self):
        return self.name

    def calculate(self):
        self.bmi = {}
        self.bmi["BMI"] = (self.weight/(self.height**2))
        self.bmi["Status"] = self.getStatus()

        return self.bmi

    def getStatus(self):
        if(self.bmi["BMI"] < 16):
            return "Severe thinness"
        elif(16 < self.bmi["BMI"] < 17):
            return "moderate thinness"
        elif(17 < self.bmi["BMI"] < 18.5):
            return "Mild thinness"
        elif(18.5 < self.bmi["BMI"] < 25):
            return "Normal"
        elif(25 < self.bmi["BMI"] < 30):
            return "Overweight"
        elif(30 < self.bmi["BMI"] < 35):
            return "Obese class I"
        elif(35 < self.bmi["BMI"] < 40):
            return "Obese class II"
        elif(self.bmi["BMI"] > 40):
            return "Obese class III"


name = input("Enter your name: ")
age = int(input("Enter the age: "))
height = float(input("Enter the height(in meters): "))
weight = float(input("Enter the weight (in kg): "))
b = Bmi(name, age, height, weight)
print(b.calculate())
