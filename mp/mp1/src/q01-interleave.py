from mp1 import MP, MPthread

# Q01:
# a. Run the following concurrent program. Are there any particular patterns in
#    the output? Is the interleaving of the output from the two threads
#    predictable in any way?
#
#    Worker 1 seems to be running significantly more frequently than worker 2.
#
# b. If the answer to part (a) is affirmative, run the same program while
#    browsing the web. Does the pattern you outlined in section (a) hold?
#
#    While browsing the web, worker 2 seems to run far more frequently
#
# c. In general, can one rely on a particular timing/interleaving of executions
#    of concurrent processes?
#
#    No, the concurrent processes must guarantee fairness between them, and if 
#    they just run in a particular interleave, it is not truly concurrent
#
# d. Given that there are no synchronization operations in the code below, any
#    interleaving of executions should be possible. When you run the code, do
#    you believe that you see a large fraction of the possible interleavings? If
#    so, what do you think makes this possible? If not, what does this imply
#    about the effectiveness of testing as a way to find synchronization errors?

#    I do not think I am, as I am not testing all possible other criteria while 
#    running this program. When I run it the conditions are largely the same. 
#    The fact that web browsing changes the pattern means any number of other 
#    proccesses on the side will change the behavior. Testing can work to some 
#    extent, but it will not catch every corner case involved with the system.

class Worker1(MPthread):
    def __init__(self, mp):
        MPthread.__init__(self, mp, "Worker 1")

    def run(self):
        while True:
            print("Hello from Worker 1")

class Worker2(MPthread):
    def __init__(self, mp):
        MPthread.__init__(self, mp, "Worker 2")

    def run(self):
        while True:
            print("Hello from Worker 2")
mp = MP()
w1 = Worker1(mp)
w2 = Worker2(mp)
w1.start()
w2.start()

##
## vim: ts=4 sw=4 et ai
##

