import random


class Person:
    """
    __init__ sets attributes for an object at object creation; is a constructor

    self variable - used to reference the object (instance of a class) /
    that is constructed by the init method

    We use self in order to make available all the attributes to the methods though out the class.
    However, if the method is running as a part of the class,
    rather than an instance of the class,
    then we do NOT need to use the self parameter in a method.

    """

    def __init__(self, firstname, lastname, health, status):

        # The reason we do this is to make these variables available in the init
        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
        "All ppl introduce themselves"
        print("Hola, my name is {} {}".format(self.firstname, self.lastname))

    def mood(self):
        emotion = random.randrange(1, 3)
        if emotion == 1:
            print("{} is happy".format(self.firstname))
        elif emotion == 2:
            print("{} is not happy".format(self.firstname))

    def health_status(self):
        if self.health == 100:
            print("{} is healthy!".format(self.firstname))
        elif self.health <= 74:
            print("{} is not that healthy".format(self.firstname))
        elif self.health >= 50:
            print("{} goes to the hospital".format(self.firstname))
        else:
            print("{} is unconscious".format(self.firstname))


Maria = Person("Maria", "Lopez", 95, status=True)
Shayne = Person("Shayne", "Torres", 88, status=False)
Bo = Person("Bo", "Lee", 72, status=True)

print("Is {} my friend? {}".format(Maria.firstname, Maria.status))

Shayne.introduce()

Bo.health_status()
Shayne.health_status()


class Enemy(Person):
    def __init__(self, weapon, firstname, lastname, health, status):
        super().__init__(firstname, lastname, health, status)

        self.weapon = weapon

    def hurt(self, other):
        if self.weapon == "rock":
            other.health -= 10
        elif self.weapon == "stick":
            other.health -= 5
        print(other.health)

    def insult(self, other):
        if other.health <= 75:
            print("{}, you are tired and weak".format(other.firstname))

    def steal(self, other):
        print("Ha ha ha, {}, I have your stuff!". format(other.firstname))
        if other.status == True:
            other.status = False

    # Ex. of child method overwriting the parent method
    def introduce(self):
        print("You are my mortal enemy!")


Alex = Enemy("rock", "Alex", "Wayne", 75, status=False)
# Alex.hurt(Maria)
Alex.insult(Bo)
Alex.steal(Shayne)
Alex.introduce()




