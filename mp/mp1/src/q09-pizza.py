from mp1 import MP, MPthread
import random

# Q09:
# This program simulates the creation of pepperoni pizzas.
#
# Implement the PepperoniPizza monitor below using MPlocks and
# MPcondition variables.

################################################################################
## DO NOT WRITE OR MODIFY ANY CODE ABOVE THIS LINE #############################
################################################################################

class PepperoniPizzaMonitor(MP):
    """
    A pepperoni pizza is made from one pepperoni and three cheeses (each
    pepperoni and cheese can be used in only one pizza).  A thread offers an
    ingredient by calling the appropriate method; the thread will block until
    the ingredient can be used in the pizza.
    """

    def __init__(self):
        MP.__init__(self)
        # TODO
        pass


    def pepperoni_ready(self):
        """Offer a pepperoni and block until this pepperoni can be used to make
        a pizza."""
        # TODO
        pass

    def cheese_ready(self):
        """Offer a cheese and block until this cheese can be used to make a
        pizza."""
        # TODO
        pass

################################################################################
## DO NOT WRITE OR MODIFY ANY CODE BELOW THIS LINE #############################
################################################################################

class Pepperoni(MPthread):
    def __init__(self, pizza, id):
        MPthread.__init__(self, pizza, id)
        self.pizza = pizza
        self.id = id

    def run(self):
        while True:
            print "Pepperoni %d ready" % self.id
            self.pizza.pepperoni_ready()
            print "Pepperoni %d is in the oven" % self.id
            self.delay()
            print "Pepperoni %d finished baking" % self.id

class Cheese(MPthread):
    def __init__(self, pizza, id):
        MPthread.__init__(self, pizza, id)
        self.pizza = pizza
        self.id = id

    def run(self):
        while True:
            print "Cheese %d ready" % self.id
            self.pizza.cheese_ready()
            print "Cheese %d is in the oven" % self.id
            self.delay(0.5)
            print "Cheese %d finished baking" % self.id

if __name__ == '__main__':
    NUM_PEPPERONI = 5
    NUM_CHEESE = 6

    pizza = PepperoniPizzaMonitor()

    for i in range(NUM_PEPPERONI):
        Pepperoni(pizza, i).start()

    for j in range(NUM_CHEESE):
        Cheese(pizza, j).start()

    pizza.Ready()
