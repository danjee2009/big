class amazon:
    
    strength=20
    dextability=25
    vitability=15
    energy=5
    
    def attack():
        return "jab!"
    def exercise(self):
        self.strength+=2
        self.energy -= 1
    
jane=amazon
mary=amazon
print(jane.strength)
jane.exercise
print(jane.energy)
