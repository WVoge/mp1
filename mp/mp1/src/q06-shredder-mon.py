from mp1 import MP, MPthread
import time, random

# Q06:
# Complete the implementation of the ShredderScheduler monitor below.  Your
# implementation should use MPlock and MPcondition variables.

################################################################################
## DO NOT WRITE OR MODIFY ANY CODE ABOVE THIS LINE #############################
################################################################################

class ShredderScheduler(MP):
    """Students are attempting to clean up the undergrad lounge in Gates by 
    shredding loose paper they find on the ground. A ShredderScheduler matches 
    up paper shredder threads with job threads. Students shred sheets of paper
    by calling add_paper(); Shredders indicate their availability by calling 
    shredder_ready().

    When a job and a shredder have been matched up, the corresponding threads
    should be allowed to continue (that is, the add_paper and shredder_ready
    functions should return).

    A ShredderScheduler will only allow a maximum number of jobs (num_jobs) to be
    queued up.  If a job is submitted and the ShredderScheduler is full, it will
    reject the job immediately."""

    def __init__(self, num_jobs):
        MP.__init__(self)
        self.lock = self.Lock("Monitor Lock")
        self.sr = self.lock.Condition("shredder ready")
        self.pr = self.lock.Condition("paper ready")
        self.counter = self.Shared("COunter",0)
        pass

    def shredder_ready(self):
        """Indicate that the currently running shredder thread is ready to
        shred. This function should return when a piece of paper has been
        put into this shredder."""
        # TODO
        with self.lock:
            self.sr.signal()
            self.counter.write(self.counter.read()+1)
            self.pr.wait()
            self.counter.write(self.counter.read()-1)
            #print self.counter.read()
            return				
        pass

    def add_paper(self):
        """Indicate that the student wants to shred a piece of paper. Immediately 
        raises an exception if the ShredderScheduler is full; otherwise waits 
        until a shredder has been assigned to this job and then returns."""
        # TODO
        with self.lock:
            #print `self.counter.read()`+`num_jobs`
            #if self.counter.read()<=num_jobs:
            self.pr.signal()
            #else: 
                
            #    raise Exception("Num Jobs Exceeded")
            self.sr.wait()
            return
        pass

################################################################################
## DO NOT WRITE OR MODIFY ANY CODE BELOW THIS LINE #############################
################################################################################

class Shredder(MPthread):
    def __init__(self, scheduler, id):
        MPthread.__init__(self, scheduler, id)
        self.scheduler = scheduler
        self.id        = id

    def run(self):
        while True:
            print("Shredder #%d: ready to shred" % self.id)
            self.scheduler.shredder_ready()
            print("Shredder #%d: shredding" % self.id)
            self.delay(random.randint(0, 2))
            print("Shredder #%d: done shredding" % self.id)

class Student(MPthread):
    def __init__(self, scheduler, id):
        MPthread.__init__(self, scheduler, id)
        self.id        = id
        self.scheduler = scheduler

    def run(self):
        while True:
            print("Student #%d: wants to print" % self.id)
            try:
                self.scheduler.add_paper()
                print("Student #%d: shredding in progress..." % self.id)
            except:
                print("Student #%d: shredding job rejected." % self.id)
            self.delay(random.randint(0, 2))

if __name__ == '__main__':
    NUM_SHREDDERS = 2
    NUM_STUDENTS = 6
    sched = ShredderScheduler(3)

    for i in range(NUM_SHREDDERS):
        Shredder(sched, i).start()
    for i in range(NUM_STUDENTS):
        Student(sched, i).start()


##
## vim: ts=4 sw=4 et ai
##
