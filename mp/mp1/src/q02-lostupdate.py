from mp1 import MP, MPthread

# Q02:
# This program simulates a postmodern game between two teams.  Each team
# presses their button as fast as they can.  There is a counter that starts at
# zero; the red team's increases a counter, while the blue team's button
# decreases the counter.  They each get to press their button 10000 times. If the
# counter ends up positive, the read team wins; a negative counter means the blue
# team wins.
#
# a. This game is boring: it should always end in a draw.  However, the provided
#    implementation is not properly synchronized.  When both threads terminate,
#    what are the largest and smallest possible scores?
#
#    The largest possible score is 10000, if the red team's process completely 
#    starves out the blue team's. In this case the blue process never runs. 
#    In the exact opposite case, the minimum score is -10000, when the blue 
#    team's process starves out the red team's.
#
#
# b. What other values can the score have when both threads have terminated?
#
#    The value of the score can be anywhere in between -10000 and 10000.
#
# c. Add appropriate synchronization such that updates to the counter
#    occur in a critical section, ensuring that the energy level is
#    always at 0 when the two threads terminate.
#
#    Your synchronization must still allow interleaving between the two threads.

################################################################################
## DO NOT WRITE OR MODIFY ANY CODE ABOVE THIS LINE #############################
################################################################################

class Contest(MP):
    def __init__(self):
        MP.__init__(self)
		#A
        self.counter = self.Shared("counter", 0)
        self.counterLock = self.Semaphore("counter lock", 1)
		
    def pushRed(self):
        self.counterLock.procure()
        self.counter.inc()
        self.counterLock.vacate()

    def pushBlue(self):
        self.counterLock.procure()
        self.counter.dec()
        self.counterLock.vacate()

class RedTeam(MPthread):
    def __init__(self, contest):
        MPthread.__init__(self, contest, "Red Team")
        self.contest = contest     

    def run(self):
        for i in range(10000):
            self.contest.pushRed()

class BlueTeam(MPthread):
    def __init__(self, contest):
        MPthread.__init__(self, contest, "Blue Team")
        self.contest = contest

    def run(self):
        for i in range(10000):
            self.contest.pushBlue()

################################################################################
## DO NOT WRITE OR MODIFY ANY CODE BELOW THIS LINE #############################
################################################################################

contest = Contest()
red  = RedTeam(contest)
blue = BlueTeam(contest)
red.start()
blue.start()
contest.Ready()

print("The counter is " + str(contest.counter.read()))

##
## vim: ts=4 sw=4 et ai
##
