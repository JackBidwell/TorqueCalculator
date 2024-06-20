import math
def circumfrance(radius):
  circumfrance = radius(math.pi)
  return circumfrance

def GearRaitio(input, output):
  gearRatio = output/input
  return gearRatio

def WheelTorque(MotorTorque, gearRatio):
  wheelTorque = MotorTorque*gearRatio
  return wheelTorque
