class Sensor(object):
    def __init__(self):
        pass
    
    def sensorOn(self):
        print("Sensor is on")
    
    def sensorOff(self):
        print("Sensor is off")
    
    
class Smoke(object):
    def __init__(self):
        pass
    
    def smokeOn(self):
        print("Smoke is on")
    
    def smokeOff(self):
        print("Smoke is off")
        
class Lights(object):
    def __init__(self):
        pass
    
    def lightsOn(self):
        print("Lights on")
    
    def lightsOff(self):
        print("Lights off")
        
class Facade(object):
    def __init__(self):
        self._sensor = Sensor()
        self._smoke = Smoke()
        self._lights = Lights()
    
    def Emergency(self):
        self._sensor.sensorOn()
        self._smoke.smokeOn()
        self._lights.lightsOn()
    
    def NoEmergency(self):
        self._sensor.sensorOff()
        self._smoke.smokeOff()
        self._lights.lightsOff()
        
if __name__ == "__main__":
    facade = Facade()
    sensor = 28
    
    if sensor > 60:
        facade.Emergency()
    else:
        facade.NoEmergency()