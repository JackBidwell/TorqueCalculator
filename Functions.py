import math
def Circumfrance(radius):
  circumfrance = radius*(2*(math.pi))
  return circumfrance

def GearRaitio(input, output):
  # The gear ratio is the is the ratio of number of teeth on the output gear (connected to the wheel) to the input gear (connected to the motor) the number of teeth is directly proportional to the circumfrance of these gears.
  gearRatio = output/input
  return gearRatio

def WheelTorque(MotorTorque, gearRatio):
  # Wheeltorque is calculated by the torque on the input gear (the gear connected to the motor) multiplied by the gear ratio
  wheelTorque = MotorTorque*gearRatio
  return wheelTorque

def MotorTorque(wheelTorque, input, output):
  # You can find the torque being applied to the input (motor gear) by multiplying the wheel torque by the inverse of the gear ratio
  motorTorque = wheelTorque * (input/output)

def OutPutRPM(inputRPM, gearRatio):
  outputRPM = inputRPM * gearRatio

def Speed(tireCircumfrance, outputRPM):
  # The output RPM, how many times the tire is rotating per minute * 60 will give you a speed, the unit is based on how you entered the rest of the information.
  speed = tireCircumfrance*outputRPM*60


