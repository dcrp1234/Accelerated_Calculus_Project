import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Initial setup
x = np.linspace(0, 10, 100)
frequency = 1.0  # initial frequency
y = np.sin(frequency * x)

# Create figure and axis
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)  # Adjust to make room for the slider
line, = ax.plot(x, y, label='Sine Wave')
ax.set_title('Sine Wave with Adjustable Frequency')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.legend()

# Create slider
ax_freq = plt.axes([0.25, 0.1, 0.65, 0.03])  # [left, bottom, width, height]
slider_freq = Slider(ax_freq, 'Frequency', 0.1, 5.0, valinit=frequency)

# Update function for the slider
def update(val):
    frequency = slider_freq.val
    y = np.sin(frequency * x)
    line.set_ydata(y)
    fig.canvas.draw_idle()  # Update the canvas

# Connect the slider to the update function
slider_freq.on_changed(update)

# Show the plot
plt.show()
