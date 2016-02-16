from mp1 import MP, MPthread

# Q11:
# You are in charge of track assignemnts at Grand Central Station.
#
# The station has many tracks that a variety of trains use for loading and
# unloading passengers. For simplicity, we assume that all tracks can be used
# by any type of train: Amtrak, Metro-North, or Subway. Since both New Yorkers
# and politicians can be quite finicky, there are many regulations regarding
# how the tracks can be assigned to trains of each type. Additionally, since
# Grand Central Station is up and running almost 24/7, inpsectors must
# also be given access to the tracks. For simplicity, inspectors are
# treated as "trains" in the scheudling system.
#
# The rules are thus:
#
#   (a) There are no more than N tracks assigned to trains at any given time
#   (b) A Subway train may not begin to use a track if it would cause more than
#       80% of the tracks in use to be assigned to Subway trains
#   (c) Amtrak trains may not use a track if there are any Metro-North trains
#       currently at the station
#   (d) Likewise, Metro-North trains may not use a track if there are any Amtrak
#       trains currently at the station (The two lines compete for some of the
#       same customers, and refuse to share the station at any time, out of spite)
#   (e) Maintenance crews are always allowed priority access to the tracks
#       (subject to condition a).  No train should be allowed to use a track if
#       an inspector is waiting.
#
# The regulations make no guarantees about starvation.

# Implement the track assignement dispatcher monitor using MPlocks and
# MPcondition variables

################################################################################
## DO NOT WRITE OR MODIFY ANY CODE ABOVE THIS LINE #############################
################################################################################

class Dispatcher(MP):
    def __init__(self, n):
        MP.__init__(self)

    def subway_enter(self):
        pass

    def subway_leave(self):
        pass

    def amtrak_enter(self):
        pass

    def amtrak_leave(self):
        pass

    def metronorth_enter(self):
        pass

    def metronorth_leave(self):
        pass

    def inspector_enter(self):
        pass

    def inspector_leave(self):
        pass

################################################################################
## DO NOT WRITE OR MODIFY ANY CODE BELOW THIS LINE #############################
################################################################################

SUBWAY      = 0
AMTRACK     = 1
METRONORTH  = 2
INSPECTOR   = 3

class Train(MPthread):
    def __init__(self, train_type, dispatcher):
        MPthread.__init__(self, dispatcher, 'Train')
        self.train_type = train_type
        self.dispatcher = dispatcher

    def run(self):
        enters = [self.dispatcher.subway_enter,
                  self.dispatcher.amtrak_enter,
                  self.dispatcher.metronorth_enter,
                  self.dispatcher.inspector_enter]
        leaves = [self.dispatcher.subway_leave,
                  self.dispatcher.amtrak_leave,
                  self.dispatcher.metronorth_leave,
                  self.dispatcher.inspector_leave]
        names  = ['subway', 'amtrak', 'metro north', 'inspector']

        print("%s train trying to arrive" % names[self.train_type])
        enters[self.train_type]()
        print("%s train admitted" % names[self.train_type])
        self.delay(0.1)
        print("%s train leaving" % names[self.train_type])
        leaves[self.train_type]()
        print("%s train done" % names[self.train_type])

max_trains = 15
numbers = [10, 35, 2, 4]
dispatcher = Dispatcher(max_trains)
for t in [SUBWAY, AMTRACK, METRONORTH, INSPECTOR]:
    for i in range(numbers[t]):
        Train(t, dispatcher).start()

##
## vim: ts=4 sw=4 et ai
##
