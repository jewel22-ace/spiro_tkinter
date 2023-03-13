import tkinter as tk
import random
from collections import deque
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading
import serial


class RealTimeGraphApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Real Time Graph")

        # Create the plot
        self.fig = plt.Figure()
        self.ax = self.fig.add_subplot(111)
        self.ax.set_ylim([-100, 100])
        self.line, = self.ax.plot([], [], lw=2)

        # Create a deque to hold the data points
        self.data = deque([0] * 100, maxlen=100)

        # Create the canvas to display the plot
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        # Create a label to display the data
        self.data_label = tk.Label(self, text="", font=("Helvetica", 14))
        self.data_label.pack(side=tk.BOTTOM, padx=10, pady=10)

        # Create a text box to display the plotted data
        self.text_box = tk.Text(
            self, height=10, width=30, font=("Helvetica", 14))
        self.text_box.pack(side=tk.RIGHT, padx=10, pady=10)

        # Create a start button
        self.start_button = tk.Button(
            self, text="Start", command=self.start_animation)
        self.start_button.pack(side=tk.BOTTOM, padx=10, pady=10)

        # Create a stop button
        self.stop_button = tk.Button(
            self, text="Stop", command=self.stop_animation)
        self.stop_button.pack(side=tk.BOTTOM, padx=10, pady=10)

        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
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

        self.read_thread = threading.Thread(target=self.read_from_serial)
        self.read_thread.daemon = True
        self.read_thread_flag = True
        self.read_thread.start()

        self.thread = threading.Thread(target=self.animation_thread)
        self.thread_flag = True
        self.thread.daemon = True
        self.thread.start()

    def stop_animation(self):
        # Stop the animation thread
        # self.read_thread.join()
        #self.read_thread = None
        self.read_thread_flag = False

        # self.thread.join()
        #self.thread = None
        self.thread_flag = False

        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def animation_thread(self):
        while self.thread_flag:
            # Generate a new data point
            data = self.data[-1]

            # Add the data to the deque
            self.data.append(data)

            self.line.set_data(range(len(self.data)), self.data)
            self.ax.relim()
            self.ax.autoscale_view(True, True, True)
            self.canvas.draw()

            # Update the data label
            self.data_label.config(text="Data: {}".format(data))

            # Update the text box with the plotted data

            self.text_box.delete('1.0', tk.END)
            self.text_box.insert(tk.END, data)

            # Wait for a short amount of time to avoid overloading the system
            self.after(10)


if __name__ == '__main__':
    print("Changes")
    app = RealTimeGraphApp()
    app.mainloop()
