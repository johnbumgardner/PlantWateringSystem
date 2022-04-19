import time, sched
from hardware.relay import Relay
from hardware.water_sensor import WaterSensor

scheduler = sched.scheduler(time.time, time.sleep)
PRIORITY = 1
TIME_DELAY = 1
def sample(scheduler, water_sensor, power_relay):
    sampled_value = water_sensor.sample()
    scheduler.enter(TIME_DELAY, PRIORITY, sample, (scheduler, water_sensor, power_relay))

water_sensor = WaterSensor(7)
power_relay = Relay(21, False)

scheduler.enter(TIME_DELAY, PRIORITY, sample, (scheduler, water_sensor, power_relay))
scheduler.run()

print(water_sensor.sample())

