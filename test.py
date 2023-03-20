from Spiro_package.spiro import Spiro
import matplotlib.pyplot as plt
s = Spiro()

data = s.read_data('Test_data.csv')
plt.plot(data)
plt.show()
