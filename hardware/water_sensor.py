from gpiozero import MCP3008

class WaterSensor:
    def __init__(self, pin) -> None:
        self.adc = MCP3008(pin)
    def sample(self): 
        return self.adc.value