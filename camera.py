import socket , time
# Construct camera class
class Camera():
    def __init__(self, camera_ip = '10.10.1.10', camera_port = 2023):
        '''Establish connection to control camera'''
        # All attributes
        self.info = None
        self.angle = None
        self.x = None
        self.y = None
        self.numberObj = 0
        self.camera_ip = camera_ip
        self.camera_port = camera_port
        self.camera = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to camera
        self.camera.connect((self.camera_ip, self.camera_port))
        print('Camera Activated')

    def get_camera_info(self):
        '''Get the camera detect information'''
        self.camera.send(b'get info!')
        # Get the data from camera
        data = self.camera.recv(30)
        # Convert data to string
        self.info = str(data)[2:-1]
        # Split data to use
        self.x, self.y, self.angle, self.numberObj = [num for num in self.info.split(',')]

    def main(self):
        '''Main function to test the camera'''
        while True:
            self.get_camera_info()
            print(f'Angle: {self.angle}, X: {self.x}, Y: {self.y}, numberObj: {self.numberObj}')