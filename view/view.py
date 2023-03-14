import Tkinter as Tk
from matplotlib.backends.backend_Tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class TopFrameView(Tk.Frame):
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

    def __init__(self,parent,**kwargs):
        super().__init__(parent, **kwargs)

        self.max_val = Tk.StringVar()
        self.min_val = Tk.StringVar()
        self.median25_val = Tk.StringVar()
        self.median75_val = Tk.StringVar()
        self.median_val = Tk.StringVar()
        self.mode_val = Tk.StringVar()
        self.mean_val = Tk.StringVar()
        self.sample_rate_val = Tk.StringVar()
        self.transfer_speed_val = Tk.StringVar()

        fig = plt.gcf()
        fig.set_size_inches(8.5, 4.5)

        fig = plt.gcf()
        fig.set_size_inches(8.5, 4.5)

        self.title("Real Time Graph")

        # Create the plot
        self.fig = plt.gcf()
        self.ax = self.fig.add_subplot(111)
        self.ax.set_ylim([-100, 100])
        self.line, = self.ax.plot([], [], lw=2)

        # Create a deque to hold the data points

        Tk.Label(self, text="", height=self.ROW0_HEIGHT, width=self.COL0_WIDTH).grid(
            column=self.START_COL, row=0)  # This is for col padding

        Tk.Label(self, text="PnuemoZ").grid(
            column=self.GRAPH_COL, row=0)

        # Create the canvas to display the plot
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_Tk_widget().grid(column=self.GRAPH_COL, row=1, rowspan=10)

        Tk.Label(self, text="", height=self.BUTTOM_ROW_HEIGHT, width=self.COL0_WIDTH).grid(
            column=self.GRAPH_COL, row=11)  # This is for col padding

        # Column 3
        Tk.Label(self, text="", height=self.ROW0_HEIGHT, width=self.LABEL_COL_WIDTH).grid(
            column=self.LABLE_COL, row=0)  # This is for col padding
        Tk.Label(self, text="Max val", height=self.LABEL_HEIGHT,
                 width=self.LABEL_WIDTH).grid(column=self.LABLE_COL, row=1)
        Tk.Label(self, text="Min val", height=self.LABEL_HEIGHT,
                 width=self.LABEL_WIDTH).grid(column=self.LABLE_COL, row=2)
        Tk.Label(self, text="Median25 val", height=self.LABEL_HEIGHT,
                 width=self.LABEL_WIDTH).grid(column=self.LABLE_COL, row=3)
        Tk.Label(self, text="Median75 val", height=self.LABEL_HEIGHT,
                 width=self.LABEL_WIDTH).grid(column=self.LABLE_COL, row=4)
        Tk.Label(self, text="Median val", height=self.LABEL_HEIGHT,
                 width=self.LABEL_WIDTH).grid(column=self.LABLE_COL, row=5)
        Tk.Label(self, text="Mode val", height=self.LABEL_HEIGHT,
                 width=self.LABEL_WIDTH).grid(column=self.LABLE_COL, row=6)
        Tk.Label(self, text="Mean val", height=self.LABEL_HEIGHT,
                 width=self.LABEL_WIDTH).grid(column=self.LABLE_COL, row=7)
        Tk.Label(self, text="Sample Rate", height=self.LABEL_HEIGHT,
                 width=self.LABEL_WIDTH).grid(column=self.LABLE_COL, row=8)
        self.start_button = Tk.Button(self, text="Start", state=Tk.NORMAL,
                                      command=self.start_animation)
        self.start_button.grid(column=self.LABLE_COL, row=9)
        # Column 4
        Tk.Label(self, text="", height=self.ROW0_HEIGHT, width=self.ENTRY_COL_WIDTH).grid(
            column=self.ENTRY_COL, row=0)  # This is for col padding
        txt = Tk.Entry(self, state=Tk.DISABLED, textvariable=self.max_val,
                       width=self.ENTRY_WIDTH).grid(column=self.ENTRY_COL, row=1)
        Tk.Entry(self, state=Tk.DISABLED, textvariable=self.min_val,
                 width=self.ENTRY_WIDTH).grid(column=self.ENTRY_COL, row=2)
        Tk.Entry(self, state=Tk.DISABLED, textvariable=self.median25_val,
                 width=self.ENTRY_WIDTH).grid(column=self.ENTRY_COL, row=3)
        Tk.Entry(self, state=Tk.DISABLED, textvariable=self.median75_val,
                 width=self.ENTRY_WIDTH).grid(column=self.ENTRY_COL, row=4)
        Tk.Entry(self, state=Tk.DISABLED, textvariable=self.median_val,
                 width=self.ENTRY_WIDTH).grid(column=self.ENTRY_COL, row=5)
        Tk.Entry(self, state=Tk.DISABLED, textvariable=self.mode_val,
                 width=self.ENTRY_WIDTH).grid(column=self.ENTRY_COL, row=6)
        Tk.Entry(self, state=Tk.DISABLED, textvariable=self.mean_val,
                 width=self.ENTRY_WIDTH).grid(column=self.ENTRY_COL, row=7)
        Tk.Entry(self, state=Tk.DISABLED, textvariable=self.sample_rate_val,
                 width=self.ENTRY_WIDTH).grid(column=self.ENTRY_COL, row=8)
        self.stop_button = Tk.Button(self, text="Stop", state=Tk.DISABLED,
                                     command=self.stop_animation)
        self.stop_button.grid(column=self.ENTRY_COL, row=9)
        # Last Column
        Tk.Label(self, text="", height=self.ROW0_HEIGHT, width=self.LAST_COL_WIDTH).grid(
            column=self.LAST_COL, row=0)  # This is for col padding

        # Initialize the animation thread
        self.thread_flag = False
        self.read_thread_flag = False

        # establishing serial communication


        def set_controller(self,controller):
            self.controller = controller

        def get_canvas(self):
            return self.canvas
        
        def set_signals(self, signals):
            self.signals = signals



