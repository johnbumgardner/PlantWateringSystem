import time
from gpiozero import OutputDevice

class Relay(OutputDevice):
    def __init__(self, pin, active_high):
        super(Relay, self).__init__(pin, active_high)

    def water_plant(self, time_value):
        self.on()
        time.sleep(time_value)
        self.off()