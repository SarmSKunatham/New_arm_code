gripper_ip = "10.10.0.14"
gripper_port = 63352  
camera_ip = "10.10.1.10"
camera_port = 2023
conveyor_port = 2002
arm_ip   = '10.10.0.14'
arm_port = 30003    ####RTDE
buffer_size = 140
get_pos_buffer_size=1116
joint_deg = [0.0,0.0,0.0,0.0,0.0,0.0]
joint_tcp = [0.0,0.0,0.0,0.0,0.0,0.0]    ####Base Ref

joint_speed = 0.1

# Start position
# start_pos = [0.11527,-0.29319,0.18998,0.014,-3.126,0.06]
start_pos = [0.116,-0.3,0.2,0,-3.143,0]

# Grab position
end_pos = start_pos.copy()
end_pos[2] -= 0.305

# Box position
box_pos = [0.00632,-0.33138,-0.105,0.014,-3.126,0.06]

# Released position
# released_pos = [0.008,-0.507,-0.18,0.014,-3.126,0.06]
released_pos = [0.00629,-0.491,-0.105,0.014,-3.126,0.06]

released_path = [
    # Move z direction
    [pos if idx != 2 else end_pos[2]+0.1 for idx,pos in enumerate(released_pos) ],
    released_pos,
]

back_to_start_path = [
    # Move z direction
    [pos if idx != 2 else start_pos[2]-0.2 for idx,pos in enumerate(released_pos) ],
    start_pos,
]
