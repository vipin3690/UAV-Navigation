#!/usr/bin/env python
import time
from flyt_python import api

drone = api.navigation(timeout=120000)  # instance of flyt droneigation class

# at least 3sec sleep time for the drone interface to initialize properly
time.sleep(3)

print 'taking off'
drone.take_off(10.0)

print ' going along the setpoints'

#Moving a distance of 10m in an equilateral triangle, X distance travelled will be 5^(1/3) and y will be 5 in each waypoint.

drone.position_set(8.66, 5, 0, relative=True)
drone.position_set(-8.66, 5, 0, relative=True)
drone.position_set(0, -10, 0, relative=True)

print 'Landing'
drone.land(async=False)

# shutdown the instance
drone.disconnect()
