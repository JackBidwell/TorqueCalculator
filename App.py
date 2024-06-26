from Functions import Circumfrance
from Functions import GearRaitio
from Functions import WheelTorque
from Functions import MotorTorque
from Functions import OutPutRPM
from Functions import Speed


engineTorque = int(input("How much torque is output by the motor?: "))
inputGear = int(input("What is the raidus of your input gear (the gear directly connected to the motor)?: "))
outputGear = int(input("What is the raidus of your output gear (the gear conncted to your wheel)?: "))

inputGear = Circumfrance(inputGear)
outputGear = Circumfrance(outputGear)

print(inputGear)
