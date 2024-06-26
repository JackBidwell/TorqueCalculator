# from Functions import Circumfrance
# from Functions import GearRaitio
# from Functions import WheelTorque
# from Functions import MotorTorque
# from Functions import OutPutRPM
# from Functions import Speed





# whatToCalculate = input("What would you like to caclulate: WheelTorque(1) EngineTorque(2) Speed(3)")

# if whatToCalculate == "1":
#   engineTorque = int(input("How much torque is output by the motor?: "))
#   inputGear = int(input("What is the raidus of your input gear (the gear directly connected to the motor)?: "))
#   outputGear = int(input("What is the raidus of your output gear (the gear conncted to your wheel)?: "))
#   inputGear = Circumfrance(inputGear)
#   outputGear = Circumfrance(outputGear)
#   gearRatio = GearRaitio(inputGear, outputGear)
#   wheelTorque = WheelTorque(engineTorque, gearRatio)
#   print(wheelTorque)
# elif whatToCalculate == "2":
#   print("what")



import tkinter as tk
from tkinter import messagebox
from Functions import Circumfrance, GearRaitio, WheelTorque

def calculate_wheel_torque():
    try:
        engine_torque = int(engine_torque_entry.get())
        input_gear_radius = int(input_gear_radius_entry.get())
        output_gear_radius = int(output_gear_radius_entry.get())
        
        input_gear_circumference = Circumfrance(input_gear_radius)
        output_gear_circumference = Circumfrance(output_gear_radius)
        gear_ratio = GearRaitio(input_gear_circumference, output_gear_circumference)
        wheel_torque = WheelTorque(engine_torque, gear_ratio)
        
        messagebox.showinfo("Wheel Torque", f"The wheel torque is: {wheel_torque}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numerical values.")

def show_engine_torque_message():
    messagebox.showinfo("Info", "Engine torque calculation is not implemented yet.")

def perform_calculation():
    calculation_type = calculation_type_var.get()
    if calculation_type == 1:
        calculate_wheel_torque()
    elif calculation_type == 2:
        show_engine_torque_message()
    else:
        messagebox.showerror("Invalid Selection", "Please select a valid calculation type.")

# Create the main window
root = tk.Tk()
root.title("Torque and Speed Calculator")

# Create and place widgets
calculation_type_var = tk.IntVar()

tk.Label(root, text="What would you like to calculate:").grid(row=0, column=0, columnspan=2)
tk.Radiobutton(root, text="Wheel Torque", variable=calculation_type_var, value=1).grid(row=1, column=0)
tk.Radiobutton(root, text="Engine Torque", variable=calculation_type_var, value=2).grid(row=1, column=1)

tk.Label(root, text="Engine Torque (Nm):").grid(row=2, column=0)
engine_torque_entry = tk.Entry(root)
engine_torque_entry.grid(row=2, column=1)

tk.Label(root, text="Input Gear Radius (mm):").grid(row=3, column=0)
input_gear_radius_entry = tk.Entry(root)
input_gear_radius_entry.grid(row=3, column=1)

tk.Label(root, text="Output Gear Radius (mm):").grid(row=4, column=0)
output_gear_radius_entry = tk.Entry(root)
output_gear_radius_entry.grid(row=4, column=1)

calculate_button = tk.Button(root, text="Calculate", command=perform_calculation)
calculate_button.grid(row=5, column=0, columnspan=2)

# Start the Tkinter event loop
root.mainloop()
