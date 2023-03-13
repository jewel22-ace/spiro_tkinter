import tkinter as tk
import random
from collections import deque
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading
import serial
from SpiroDriver import spirodriver

plt.style.use('ggplot')


class constant:
    handler = None


constant()


class RealTimeGraphApp(tk.Tk):

    labelx = 300
    labely = 300

    START_COL = 0
    GRAPH_COL = 1
    LABLE_COL = 2
    ENTRY_COL = 3
    LAST_COL = 4

    COL0_WIDTH = 5
    LABEL_COL_WIDTH = 20
    LABEL_WIDTH = 10
    ENTRY_WIDTH = 20
    ENTRY_COL_WIDTH = 20
    BUTTOM_COL_WIDTH = COL0_WIDTH
    LAST_COL_WIDTH = 5

    ROW0_HEIGHT = 2
    BUTTOM_ROW_HEIGHT = 2
    LABEL_HEIGHT = 2
    max_val = None

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.max_val = tk.StringVar()
        self.min_val = tk.StringVar()
        self.median25_val = tk.StringVar()
        self.median75_val = tk.StringVar()
        self.median_val = tk.StringVar()
        self.mode_val = tk.StringVar()
        self.mean_val = tk.StringVar()
        self.sample_rate_val = tk.StringVar()

        fig = plt.gcf()
        fig.set_size_inches(8.5, 4.5)

        self.title("Real Time Graph")

        # Create the plot
        self.fig = plt.gcf()
        self.ax = self.fig.add_subplot(111)
        self.ax.set_ylim([-100, 100])
        self.line, = self.ax.plot([], [], lw=2)

        # Create a deque to hold the data points

        tk.Label(self, text="", height=self.ROW0_HEIGHT, width=self.COL0_WIDTH).grid(
            column=self.START_COL, row=0)  # This is for col padding

        tk.Label(self, text="PnuemoZ").grid(
            column=self.GRAPH_COL, row=0)

        # Create the canvas to display the plot
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().grid(column=self.GRAPH_COL, row=1, rowspan=10)

        tk.Label(self, text="", height=self.BUTTOM_ROW_HEIGHT, width=self.COL0_WIDTH).grid(
            column=self.GRAPH_COL, row=11)  # This is for col padding

        # Column 3
        tk.Label(self, text="", height=self.ROW0_HEIGHT, width=self.LABEL_COL_WIDTH).grid(
            column=self.LABLE_COL, row=0)  # This is for col padding
        tk.Label(self, text="Max val", height=self.LABEL_HEIGHT,
                 width=self.LABEL_WIDTH).grid(column=self.LABLE_COL, row=1)
        tk.Label(self, text="Min val", height=self.LABEL_HEIGHT,
                 width=self.LABEL_WIDTH).grid(column=self.LABLE_COL, row=2)
        tk.Label(self, text="Median25 val", height=self.LABEL_HEIGHT,
                 width=self.LABEL_WIDTH).grid(column=self.LABLE_COL, row=3)
        tk.Label(self, text="Median75 val", height=self.LABEL_HEIGHT,
                 width=self.LABEL_WIDTH).grid(column=self.LABLE_COL, row=4)
        tk.Label(self, text="Median val", height=self.LABEL_HEIGHT,
                 width=self.LABEL_WIDTH).grid(column=self.LABLE_COL, row=5)
        tk.Label(self, text="Mode val", height=self.LABEL_HEIGHT,
                 width=self.LABEL_WIDTH).grid(column=self.LABLE_COL, row=6)
        tk.Label(self, text="Mean val", height=self.LABEL_HEIGHT,
                 width=self.LABEL_WIDTH).grid(column=self.LABLE_COL, row=7)
        tk.Label(self, text="Sample Rate", height=self.LABEL_HEIGHT,
                 width=self.LABEL_WIDTH).grid(column=self.LABLE_COL, row=8)
        self.start_button = tk.Button(self, text="Start", state=tk.NORMAL,
                                      command=self.start_animation)
        self.start_button.grid(column=self.LABLE_COL, row=9)
        # Column 4
        tk.Label(self, text="", height=self.ROW0_HEIGHT, width=self.ENTRY_COL_WIDTH).grid(
            column=self.ENTRY_COL, row=0)  # This is for col padding
        txt = tk.Entry(self, state=tk.DISABLED, textvariable=self.max_val,
                       width=self.ENTRY_WIDTH).grid(column=self.ENTRY_COL, row=1)
        tk.Entry(self, state=tk.DISABLED, textvariable=self.min_val,
                 width=self.ENTRY_WIDTH).grid(column=self.ENTRY_COL, row=2)
        tk.Entry(self, state=tk.DISABLED, textvariable=self.median25_val,
                 width=self.ENTRY_WIDTH).grid(column=self.ENTRY_COL, row=3)
        tk.Entry(self, state=tk.DISABLED, textvariable=self.median75_val,
                 width=self.ENTRY_WIDTH).grid(column=self.ENTRY_COL, row=4)
        tk.Entry(self, state=tk.DISABLED, textvariable=self.median_val,
                 width=self.ENTRY_WIDTH).grid(column=self.ENTRY_COL, row=5)
        tk.Entry(self, state=tk.DISABLED, textvariable=self.mode_val,
                 width=self.ENTRY_WIDTH).grid(column=self.ENTRY_COL, row=6)
        tk.Entry(self, state=tk.DISABLED, textvariable=self.mean_val,
                 width=self.ENTRY_WIDTH).grid(column=self.ENTRY_COL, row=7)
        tk.Entry(self, state=tk.DISABLED, textvariable=self.sample_rate_val,
                 width=self.ENTRY_WIDTH).grid(column=self.ENTRY_COL, row=8)
        self.stop_button = tk.Button(self, text="Stop", state=tk.DISABLED,
                                     command=self.stop_animation)
        self.stop_button.grid(column=self.ENTRY_COL, row=9)
        # Last Column
        tk.Label(self, text="", height=self.ROW0_HEIGHT, width=self.LAST_COL_WIDTH).grid(
            column=self.LAST_COL, row=0)  # This is for col padding

        # Initialize the animation thread
        self.thread_flag = False
        self.read_thread_flag = False

        # establishing serial communication

    def read_from_serial(self):
        # Read data from the serial port and add it to the deque
        ser = serial.Serial('COM4', 9600)
        while self.read_thread_flag:
            try:
                data = int(ser.readline().decode().strip())
                self.data.append(data)
                print(data)
            except ValueError:
                pass

        ser.close()

    def start_animation(self):
        # Create a new thread for the animation process

        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        self.thread = threading.Thread(target=self.animation_thread)
        self.thread_flag = True
        self.thread.daemon = True
        self.thread.start()

        constant.handler.start_acquisition()

    def stop_animation(self):
        # Stop the animation thread
        # self.read_thread.join()
        #self.read_thread = None
        constant.handler.stop_acquisition()
        self.read_thread_flag = False

        # self.thread.join()
        #self.thread = None
        self.thread_flag = False

        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def animation_thread(self):
        while self.thread_flag:
            # Generate a new data point
            self.data = (constant.handler.get_buffer())
            #data = self.data[-1]
            #print('In', data)

            # Add the data to the deque
            # self.data.append(data)

            self.line.set_data(range(len(self.data)), self.data)
            self.ax.relim()
            self.ax.autoscale_view(True, True, True)
            self.canvas.draw()

            # Update the data label
            #self.data_label.config(text="Data: {}".format(self.data[-1]))

            # Update the text box with the plotted data

            #self.text_box.delete('1.0', tk.END)
            #self.text_box.insert(tk.END, self.data[-1])

            # Wait for a short amount of time to avoid overloading the system
            self.after(10)


if __name__ == '__main__':
    print("Changes")
    constant.handler = spirodriver()
    constant.handler.connect_device('COM4')
    app = RealTimeGraphApp()
    app.mainloop()
