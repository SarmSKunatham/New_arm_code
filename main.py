# Import all dependencies
import time
from conveyor import Conveyor
from gripper import Gripper
from arm import Arm
from camera import Camera
import math

# Initialize all classes
conveyor = Conveyor()
arm = Arm()
gripper = Gripper()
camera = Camera()

# Move arm to start position and open gripper
start_position = [0.116,-0.3,0.2,0,-3.143,0]
arm.movel_to_position(start_position)
gripper.gripper_open()

# Start conveyor
conveyor.run_conveyor()

# Detect object
while True:
    # Get the information from the camera
    camera.get_camera_info()
    # If object is detected break the loop and start to grab the box
    if camera.numberObj == '1':
        print(f'Latest Angle: {camera.angle}, X: {camera.x}, Y: {camera.y}, numberObj: {camera.numberObj}')
        break
print(f'Final Angle: {camera.angle}, X: {camera.x}, Y: {camera.y}, numberObj: {camera.numberObj}')
        

# Calculate position of the box
# Calculate the real distance from pixel into m of x and y
x_obj = (float(camera.x) - 540) * (0.4 / 1823)
y_obj = (float(camera.y) - 550) * (0.4 / 2477)
# length from gripper to camera
L = 0.18
# speed of the conveyor is 1 cm/s
v = 0.01
# time use to move the arm (4 sec) and close the gripper (1 sec)
time_interval = 2 + 1
# calculate new x and y position
new_x = start_position[0] + x_obj + L - (v * time_interval)
new_y = start_position[1] + y_obj
# add all values into a position list
new_pos = start_position.copy()
new_pos[0] = new_x
new_pos[1] = new_y
# our define z in order to go down
new_pos[2] = 0.04
# because the gripper can rotate only one side this checking for possible angle to rotate
if not(float(camera.angle) >= 270.0 and float(camera.angle)<= 360.0):
    # if the box tilts from 0 to 90 degree
    # then rx will be added from angle recieved from the camera
    new_rx = start_position[3] + math.radians(float(camera.angle))
    new_pos[3] = new_rx

# Move to the box position
arm.movel_to_position(new_pos)
# move down and grab
new_pos[2] = -0.1
arm.movel_to_position(new_pos)
# Wait until it reaches the box
time.sleep(1)
# Close the gripper
gripper.gripper_close()

# Move up
new_pos[2] = 0.2
arm.movel_to_position(start_position)

print('Congratultation!!!')

