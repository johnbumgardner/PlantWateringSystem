from hardware.water_sensor import WaterSensor
from gpiozero import Button, LED

left_sensor = WaterSensor(7)
right_sensor = WaterSensor(0)
red_dry_button = Button(2, bounce_time=1)
green_wet_button = Button(3, bounce_time=1)
set_red_dry_value = LED(21)
set_green_wet_value = LED(20)
water_the_plant_blue = LED(16)

class System:
    def __init__(self):
        self.water_sensors = [left_sensor, right_sensor]
        self.dry_val = None
        self.wet_val = None
    def sample(self):
        sampled_values = []
        for sensor in self.water_sensors: 
            sampled_values.append(sensor.sample())
        return sampled_values
    def set_dry_value(self):
        dry_vals = self.sample()
        self.dry_val = sum(dry_vals) / len(dry_vals)
        print(self.dry_val)
    def set_wet_value(self):
        wet_vals = self.sample()
        self.wet_val = sum(wet_vals) / len(wet_vals)
        print(self.wet_val)

system = System()

red_dry_button.when_pressed = system.set_dry_value
green_wet_button.when_pressed = system.set_wet_value

while True:
    if(system.dry_val):
        set_red_dry_value.off()
    else: 
        set_red_dry_value.on()
    if(system.wet_val):
        set_green_wet_value.off()
    else: 
        set_green_wet_value.on()
    
    if(system.dry_val and system.wet_val):
        mid_point = (system.dry_val + system.wet_val) / 2
        curr_val = sum(system.sample()) / 2
        if (curr_val > mid_point):
            water_the_plant_blue.on()
        else:
            water_the_plant_blue.off()
