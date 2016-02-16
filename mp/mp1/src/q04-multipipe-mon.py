from mp1 import MP, MPthread
import random

# Q04:
# a. Complete the implementation of the MultiPurposePipe monitor below using
#    MPlocks and MPcondition variables. Your implementation should be able
#    to make progress if there are liquids that can flow
#
# b. What fairness properties does your implementation have?  Under what
#    conditions (if any) can a thread starve?
#

################################################################################
## DO NOT WRITE OR MODIFY ANY CODE ABOVE THIS LINE #############################
################################################################################

class MultiPurposePipe(MP):
    """
    California has encountered another water crisis requiring new pipes to be
    built. The governor has decided to cut costs and introduce a new technology:
    multi-purpose pipes.  These pipes alternate carrying clean water and sewage.

    You are the lone civil engineer at the control station, and it is your job
    to make sure that people don't drink sewage. The multi-purpose pipe allows
    multiple instances of liquid to pass through in either direction but at any
    point in time, the liquid flowing through must be of the same type.

    Liquids wishing to flow should call the flow(), and once they have finished
    flowing, they should call finished()
    """

    def __init__(self):
        MP.__init__(self)
        # TODO

    def flow(self, direction):
        """wait for permission to flow through the pipe. direction should be
        either 0 or 1."""
        # TODO
        pass

    def finished(self,direction):
        # TODO
        pass

################################################################################
## DO NOT WRITE OR MODIFY ANY CODE BELOW THIS LINE #############################
################################################################################

class Sewage(MPthread):
    def __init__(self, pipe, id):
        MPthread.__init__(self, pipe, id)
        self.direction = 0
        self.wait_time = random.uniform(0.1,0.5)
        self.pipe      = pipe
        self.id        = id

    def run(self):
        # flush
        self.delay(self.wait_time)
        print "Sewage %d: trying to flow" % (self.id)
        # request permission to flow
        self.pipe.flow(self.direction)
        print "Sewage %d: Flowing" % self.id
        # flow through
        self.delay(0.01)
        print "Sewage %d: Flowed" % self.id
        # signal that we have finished flowing
        self.pipe.finished(self.direction)
        print "Sewage %d: Finished flowing" % self.id

class CleanWater(MPthread):
    def __init__(self, pipe, id):
        MPthread.__init__(self, pipe, id)
        self.direction = 1
        self.wait_time = random.uniform(0.1,0.5)
        self.pipe      = pipe
        self.id        = id

    def run(self):
        # turn on faucet
        self.delay(self.wait_time)
        print "CleanWater %d: Trying to flow" % (self.id)
        # request permission to flow
        self.pipe.flow(self.direction)
        print "CleanWater %d: Flowing" % self.id
        # flow through
        self.delay(0.01)
        print "CleanWater %d: Flowed" % self.id
        # signal that we have finished flowing
        self.pipe.finished(self.direction)
        print "CleanWater %d: Finished flowing" % self.id


if __name__ == "__main__":

    cityPipe = MultiPurposePipe()
    sid = 0
    cid = 0
    for i in range(100):
        if random.randint(0, 1) == 0:
            Sewage(cityPipe, sid).start()
            sid += 1
        else:
            CleanWater(cityPipe, cid).start()
            cid += 1


    cityPipe.Ready()
