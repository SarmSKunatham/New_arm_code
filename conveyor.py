####### Command for control conveyor #################
#### activate tcp        = activate,tcp
#### power on servo      = pwr_on,conv,0
#### power off servo     = pwr_off,conv,0
#### set velocity x mm/s = set_vel,conv,x   # x = 0 to 200
#### jog forward         = jog_fwd,conv,0
#### jog backward        = jog_bwd,conv,0
#### stop conveyor       = jog_stop,conv,0
#########################################################

import socket,time
import config

class Conveyor():
   def __init__(self, host='10.10.0.98', conveyor_port = 2002):
      self.host = host
      self.conveyor_port = conveyor_port
      self.conveyor_recv = None
      self.conveyor = None
      print("Conveyor init")
      print(f"HOST: {self.host}, PORT: {self.conveyor_port}")
      socket_server = socket.socket()
      socket_server.bind((self.host, self.conveyor_port))
      print('Conveyor bind')
      socket_server.listen()
      print('Conveyor listen on port ', self.conveyor_port)
      self.conveyor, addr = socket_server.accept()
      time.sleep(0.5)
      print("Conveyor accept")
      print("Connection from: " + str(addr))
      # Activate tcp
      self.send_command("activate,tcp")
      print("Conveyor activate tcp")
      self.send_command("pwr_on,conv,0")
      print("Conveyor power on")
   
   def send_command(self, cmd):
       self.conveyor.sendall(f"{cmd}\n".encode())
       time.sleep(0.5)

   def run_conveyor(self, speed=10):
      self.send_command("jog_stop,conv,0")
      print("Reset conveyor")
      # self.send_command(f"set_vel,conv,{speed}")
      print("Set speed to 10")

      self.send_command("jog_fwd,conv,0")
      print('Start Moving')
   
   def stop_conveyor(self):
      self.send_command("jog_stop,conv,0")
      print('Stop conveyor')

   def main(self):
      # Move conveyor
      self.run_conveyor()
      time.sleep(10)
      self.stop_conveyor()


if __name__ == '__main__':
   
      conveyor = Conveyor()
      conveyor.stop_conveyor()
