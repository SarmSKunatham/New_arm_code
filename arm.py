# Import all packages
import socket, struct , time
import config
# Construct arm class
class Arm:
        def __init__(self, arm_ip='10.10.0.14', arm_port=30003):
            '''Establish connection to control arm'''
            # All attributes
            self.arm_ip = arm_ip
            self.arm_port = arm_port
            self.buffer_size = 140
            self.get_pos_buffer_size = 1116
            self.joint_deg = [0.0,0.0,0.0,0.0,0.0,0.0]
            self.joint_tcp = [0.0,0.0,0.0,0.0,0.0,0.0]
            self.joint_speed = 0.1
            self.robot_mode = None
            self.arm_recv = None
            self.buffer_size = 1140
            self.arm = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.arm.connect((self.arm_ip, self.arm_port))
            time.sleep(1)
            if self.arm.recv(self.buffer_size) :
                print('Connected to Primary interfaces....SUCCESSFULLY!')
            else :
                print('Connected to Primary interfaces...FAILED!')

        def send_command(self, command):
            '''Send command to arm'''
            self.arm.send(bytes(command, 'UTF-8'))
            print("Command sent: " + command)

        def movej_to_position(self, position, speed = 1, acceleration = 0.25):
            '''Function to move arm to position using movej'''
            self.send_command("movej(p{}, {}, {}, 3, 0)\n".format(position, speed, acceleration))

        def movel_to_position(self, position, speed = 1, acceleration = 0.25):
            '''Function to move arm to position using movel with a specific time period equal to 1 second'''
            self.send_command("movel(p{}, {}, {}, 1, 0)\n".format(position, speed, acceleration))
        
        def main(self):
            '''Main function to test arm'''
            self.arm_status()
            print('Robot start moving')
            # from config
            # Move to Start position
            print(f'Start position: {config.start_pos}')
            self.movej_to_position(config.start_pos)
            time.sleep(2)
            # Move to End position
            print(f'End position: {config.end_pos}')
            self.movej_to_position(config.end_pos)
            time.sleep(2)
            # Move back to Start position
            self.movej_to_position(config.start_pos)
            time.sleep(2)

