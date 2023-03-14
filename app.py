import tkinter as Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

from view.view import TopFrameView
from model.signal import signal

plt.style.use('ggplot')

class constant:
    handler = None
    live_feature = None
constant()


class app(Tk.tk):
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
    def __init__(self):
        super().__init__()
        self.title('BreathOut')

        self.signals = Signals([], [], 0, 0)
        self.dp_features = DpFeatures()
        
        self.max_val = Tk.StringVar()
        self.min_val = Tk.StringVar()
        self.median25_val = Tk.StringVar()
        self.median75_val = Tk.StringVar()
        self.median_val = Tk.StringVar()
        self.mode_val = Tk.StringVar()
        self.mean_val = Tk.StringVar()
        self.sample_rate_val = Tk.StringVar()
        self.transfer_speed_val = Tk.StringVar()

        self.ui_update_loop = True

        self.top_frame= TopFrameView()
        self.top_frame = TopFrameView(
            self, highlightbackground="gray", highlightthickness=1)
        self.top_frame.pack(side=Tk.TOP, padx=20, pady=20)
        self.top_frame.set_dp_features(self.dp_features)
        self.top_frame.set_signals(self.signals)

        self.thread_flag = False
        self.read_thread_flag = False


        def animation_thread(self):
            while self.thread_flag:
                
                pass


        