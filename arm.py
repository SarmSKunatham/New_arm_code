#!/usr/bin/env python
# encoding: utf=8

# IMPORT
import socket, struct , time
import config

# SET UP
arm_ip   = '10.10.0.14'
arm_port = 30003  

buffer_size = 1140
get_pos_buffer_size=1116
joint_deg = [0.0,0.0,0.0,0.0,0.0,0.0]
joint_tcp = [0.0,0.0,0.0,0.0,0.0,0.0]    ####Base Ref

joint_speed = 0.1


class Arm:
        def __init__(self, arm_ip='10.10.0.14', arm_port=30003):
            '''Establish connection to control arm'''
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
        
        def arm_status(self):
            '''Get arm status'''
            arm_recv = self.arm.recv(self.buffer_size)
            self.arm_data = struct.unpack('!i142d',arm_recv)
            self.arm_mode = self.arm_data[95]
            for i in range (0,6) :
                    joint_tcp[i] = round(self.arm_data[56+i],3)
                    joint_deg[i] = round((self.arm_data[32+i])/0.01745,2)
            print ('arm mode    : ' + str(self.arm_mode))  
            print ('arm Joint Pos    : ' + str(joint_tcp))
            print ('arm Joint Deg    : ' + str(joint_deg))

        def send_command(self, command):
             self.arm.send(bytes(command, 'UTF-8'))
             print("Command sent: " + command)
            #  self.arm_recv = str(self.arm.recv(self.buffer_size))
            #  print(self.arm_recv)

        def movej_to_position(self, position, speed = 1, acceleration = 0.25):
            command = "movej(p{}, {}, {}, 3, 0)\n".format(position, speed, acceleration)
            self.send_command("movej(p{}, {}, {}, 3, 0)\n".format(position, speed, acceleration))
            # time.sleep(3)

        def movel_to_position(self, position, speed = 1, acceleration = 0.25):
            command = "movel(p{}, {}, {}, 3, 0)\n".format(position, speed, acceleration)
            self.send_command("movel(p{}, {}, {}, 1, 0)\n".format(position, speed, acceleration))
            # time.sleep(3)
        
        def main(self):
            '''Main function'''
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
 
# if __name__ == '__main__':
#     arm = Arm()
#     arm.main()

