"""
Write a program to create a dog class, create a class variable animal and inside the constructor , create another tow variables - breed and color indise the constructor. Next up, create two different objects for different breeds of dogs. Also, display the details of both breesds of dogs.
"""

class dog():

    # class variable 
    animal = 'dog'

    #constructor
    def __init__(self, breed):
        self.breed = breed
        self.color = 'brown'

    # method 
    def display(self):
        print(f'animal: {self.animal}, breed: {self.breed}, color: {self.color}')

#object creation 
firstObj = dog('blub dog')        
secondObj = dog('german shefered')     

firstObj.display()
secondObj.display()