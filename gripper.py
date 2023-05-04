import socket , time 

class Gripper:
    def __init__(self, gripper_ip='10.10.0.14', gripper_port=63352):
        self.gripper_ip = gripper_ip
        self.gripper_port = gripper_port
        self.gripper_recv = None
        self.gripper = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.gripper.connect((self.gripper_ip, self.gripper_port))
        time.sleep(2)
        self.gripper.send(b'GET ACT\n')
        self.gripper_recv = str(self.gripper.recv(10), 'UTF-8')
        print(self.gripper_recv)
        if '1' in self.gripper_recv:
            print('Gripper Activated')
        else:
            print('Gripper is not Activated')

    def gripper_open(self):
        '''Open the gripper'''
        self.gripper.send(b'SET POS 0\n')
        # self.gripper_recv = str(self.gripper.recv(255), 'UTF-8')
        # print(self.gripper_recv)
        print('Open Gripper!')
        time.sleep(0.5)

    def gripper_close(self):
        '''Close the gripper'''
        self.gripper.send(b'SET POS 255\n')
        print('Close Gripper!')
        # self.gripper_recv = str(self.gripper.recv(255), 'UTF-8')
        # print(self.gripper_recv)
        time.sleep(0.5)

    def main(self):
        '''Main function'''
        while True:
            self.gripper_open()
            self.gripper_close()

# if __name__ == '__main__':
#     gripper = Gripper()
#     gripper.gripper_open()
#     gripper.gripper_close()
#     gripper.main()
