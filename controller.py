class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def start_acquisition(self):
        self.model.connect_device('COM4')
        self.model.start_acquisition()
