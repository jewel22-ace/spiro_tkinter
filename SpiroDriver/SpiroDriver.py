import serial
import threading
from collections import deque
import random
import time


class spirodriver():

    def __init__(self) :
        
        self.read_thread_flag=False 
        self.ser=None
        self.data = deque([0] * 100, maxlen=100)
        
    
    def connect_device(self,comp_port,baud_rate=9600):

        self.ser=serial.Serial(str(comp_port),baud_rate)
        print('Device Connected')
    

    def signal_acquisition(self):

        while self.read_thread_flag:
            try:
                data = int(self.ser.readline().decode().strip())
                self.data.append(data)
                print(data)
            except ValueError:
                pass
    
    def signal_acquisition_rand(self):
        while self.read_thread_flag:
            try:
                data=random.randint(-100, 100)
                self.data.append(data)
                print(data)
                time.sleep(0.1)
            except ValueError:
                pass
        
    
    def get_buffer(self):

        print(self.data)
        return self.data
        
    
    def start_acquisition(self):
        self.read_thread_flag=True 
        self.read_thread = threading.Thread(target=self.signal_acquisition_rand)
        self.read_thread.daemon = True
        self.read_thread.start()

    def stop_acquisition(self):
        self.read_thread_flag=False
        self.read_thread.join()
        
        


    