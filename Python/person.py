class Person:
    def __init__(self):  # def __init__(self,name,gender,ms)
        self.name = input("Enter the name: ")  # name
        self.gender = input("Enter the gender (m/f): ")  # gender
        self.ms = input("Enter the marital status (m/u): ")  # ms

    def disp_result(self):
        if(self.gender.lower() == 'm'):
            print(f"Welcome Mr. {self.name}")
        else:
            if(self.ms.lower() == 'm'):
                print(f"Welcome Mrs. {self.name}")
            elif(self.ms.lower() == 'u'):
                print(f"Welcome Ms. {self.name}")


p = Person()  # Person(name="Ram",gender="m",ms="m")
p.disp_result()
