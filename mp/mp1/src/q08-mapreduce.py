from mp1 import MP, MPthread
import time, random

# Q08:
# This problem simulates a simplified map/reduce controller.  A map/reduce
# controller performs a computation in two steps.  In the first step (the "map
# phase"), each input value is transformed (by a separate worker thread) into
# an intermediate value.  In the second step (the "reduce phase"), all of the
# intermediate values are combined (by the worker threads) to form an output.
#
# Thus all of the worker threads start the map phase simultaneously, but none
# can proceed to the reduce phase until they have all completed the map phase.
# they will then all start the reduce phase, but cannot start another map/reduce
# computation until they have all completed the reduce phase.
#
# Implement the controller monitor using python MPlock and MPcondition variables

################################################################################
## DO NOT WRITE OR MODIFY ANY CODE ABOVE THIS LINE #############################
################################################################################

class Controller(MP):

    def __init__(self, num_workers):
        MP.__init__(self)
        self.lock = self.Lock("Monitor lock")
        self.done = self.lock.Condition("is done")

    def start_next_phase(self):
        """Called by a thread to indicate that it has completed the current
        phase.  Function blocks until all threads have completed the current
        phase."""
        self.done.broadcast()
        pass

################################################################################
## DO NOT WRITE OR MODIFY ANY CODE BELOW THIS LINE #############################
################################################################################

class Worker(MPthread):

    def __init__(self, controller, id):
        MPthread.__init__(self, controller, id)
        self.controller = controller
        self.id         = id

    def run(self):
        while True:
            # wait for start of map phase:
            print("worker #%d: waiting for input" % self.id)
            self.controller.start_next_phase()
            # perform map phase
            print("worker #%d: starting map phase" % self.id)
            self.delay(random.randint(0, 2))
            print("worker #%d: finished map phase" % self.id)
            # wait for start of reduce phase
            self.controller.start_next_phase()
            # perform reduce phase
            print("worker #%d: starting reduce phase" % self.id)
            self.delay(random.randint(0, 2))
            print("worker #%d: finished reduce phase" % self.id)
            self.controller.start_next_phase()
            print("worker #%d: computation done" % self.id)


if __name__ == '__main__':
    num_threads = 10
    controller  = Controller(num_threads)
    for i in range(num_threads):
        Worker(controller,i).start()

##
## vim: ts=4 sw=4 et ai
##
