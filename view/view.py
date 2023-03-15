import tkinter as Tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class TopFrameView(Tk.Frame):
     
    def __init__(self, parent, **kwargs):
        
        super().__init__(parent, **kwargs)
        self.application_alive=True
        self.signals = None

        fig = plt.gcf()
        fig.set_size_inches(8.5, 4.5)
        plt.gcf().subplots(2, 1)

        self.setup_views()
        self.start_ui_update()

    def setup_views(self):
        # Column 2
        Tk.Label(self, text="BreathOut").grid(
            column=0, row=0)
        self.canvas = FigureCanvasTkAgg(plt.gcf(), master=self)
        self.canvas.get_tk_widget().grid(column=0, row=1, rowspan=10, padx=20, pady=20)
        

    def set_signals(self, signals):
        self.signals = signals


    def start_ui_update(self):
        self.update_graph()
        pass

    def update_graph(self):
        if self.signals:
            # Generate values
            ax1, ax2 = plt.gcf().get_axes()

            # Clear current data
            ax1.cla()
            ax2.cla()

            ax1.set_ylim(-1500, 2000)
            ax2.set_ylim(-100, 100000)
            # Plot new data
            ax1.plot(self.signals.raw_rand_data)
            
            self.canvas.draw()

            
        if self.application_alive:
            self.after(10, self.update_graph)


    def set_controller(self, controller):
        self.controller = controller
        