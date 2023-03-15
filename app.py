from model.signal import signal
from SpiroDriver.SpiroDriver import spirodriver
import tkinter as Tk
import random
from collections import deque
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading
from view.view import TopFrameView
from controller import controller
import serial

plt.style.use('ggplot')


class constant:
    handler = None


constant()


class app(Tk.Tk):
    def __init__(self, ):
        super().__init__()
        self.title('BreathOut')
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.model = signal()

        self.controller = controller(self, self.model)

        self.top_frame = TopFrameView(self)
        self.top_frame.pack(side=Tk.TOP, pady=20)
        self.top_frame.set_signals(self.model)
        self.top_frame.set_controller(self.controller)

        self.start_data_worker_thread()

    def start_data_worker_thread(self):
        print("In")
        # start worker threads
        self.process_hardware_data_thread = threading.Thread(
            target=self.process_hardware_data)
        self.process_hardware_data_thread.daemon = True
        self.process_hardware_data_thread.start()

    def process_hardware_data(self):
        print("In")
        while True:
            self.model.raw_rand_signal = constant.handler.get_buffer()
            print(self.model.raw_rand_data)

    def on_closing(self):
        print('Quit')
        self.start_data_worker_thread.join()
        self.destroy()


if __name__ == '__main__':

    constant.handler = spirodriver()
    constant.handler.start_acquisition()

    app = app()
    app.mainloop()
